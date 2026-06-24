import os
import re
import sys
import json
import time
import random
import argparse
from datetime import datetime
import io
import requests
from bs4 import BeautifulSoup

# Configuração de encoding para evitar erros de terminal Windows (UnicodeEncodeError)
if sys.platform.startswith("win"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Fallback para imports do DuckDuckGo Search
try:
    from duckduckgo_search import DDGS
except ImportError:
    try:
        from ddgs import DDGS
    except ImportError:
        print("[!] Bibliotecas 'duckduckgo-search' ou 'ddgs' nao encontradas.")
        print("[!] Por favor, instale usando: pip install duckduckgo-search")
        sys.exit(1)

# Caminhos padrão do sistema
PASTA_PESQUISAS = os.path.join("context", "pesquisas-livros")
ARQUIVO_CACHE = os.path.join(PASTA_PESQUISAS, ".cache.json")
ARQUIVO_INDICE = os.path.join(PASTA_PESQUISAS, "_indice.md")

# Carrega o arquivo .env manualmente para garantir portabilidade absoluta
def carregar_env():
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    parts = line.split("=", 1)
                    if len(parts) == 2:
                        key, val = parts[0].strip(), parts[1].strip()
                        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                            val = val[1:-1]
                        os.environ[key] = val

carregar_env()
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Categorias mapeadas para estruturação de pastas
CATEGORIAS_VALIDAS = [
    "Espiritualidade",
    "Apometria",
    "Psicologia",
    "Nutricao",
    "Magia",
    "Desenvolvimento Pessoal",
    "Outros"
]

def slugify(text):
    """Gera um slug amigável para nomes de arquivo a partir de um texto."""
    text = text.lower()
    # Remove acentos
    import unicodedata
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    # Substitui caracteres especiais por hífens
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text).strip('-')
    return text

def limpar_nome_livro(name):
    """Limpa o nome do arquivo/linha para gerar uma query de busca limpa."""
    # Remove extensões
    cleaned = re.sub(r'\.(epub|pdf|mobi|docx|txt|html|zip)$', '', name, flags=re.IGNORECASE)
    
    # Remove prefixos de download comuns
    cleaned = re.sub(r'^(pdfcoffee\.com|oceanofpdf\.com|z-library|1lib|sk)[_ -]+', '', cleaned, flags=re.IGNORECASE)
    
    # Remove hashes ou timestamps numéricos no início
    cleaned = re.sub(r'^\d{10,13}[-_]+', '', cleaned)
    
    # Remove qualquer conteúdo entre parênteses ou colchetes por completo (ex: (Trilogia do Amor), [Draft])
    cleaned = re.sub(r'\(.*?\)', '', cleaned)
    cleaned = re.sub(r'\[.*?\]', '', cleaned)
    
    # Separa números de letras (ex: 12camadas -> 12 camadas)
    cleaned = re.sub(r'(?<=\d)(?=[a-zA-Z])|(?<=[a-zA-Z])(?=\d)', ' ', cleaned)
    
    # Separa CamelCase (ex: MichelleGil -> Michelle Gil)
    cleaned = re.sub(r'(?<=[a-z0-9])(?=[A-Z])', ' ', cleaned)
    
    # Remove marcadores de ordem/índice no início como 4°, 1., 1- (mas mantém números comuns como 12 ou 72)
    cleaned = re.sub(r'^\d+[°oª\.]\s*', '', cleaned)
    cleaned = re.sub(r'^\d+\s*[-_]+\s*', '', cleaned)
    
    # Substitui hífens e underscores por espaços
    cleaned = cleaned.replace('_', ' ').replace('-', ' ')
    
    # Remove espaços extras
    cleaned = ' '.join(cleaned.split())
    
    # Remove palavras de ruído no final (como v1, pt, br, pdf, free, artigo, etc.) em loops
    for _ in range(3):
        cleaned = re.sub(
            r'\b(v?\d+|pt|br|en|trad|completo|volume\s*\d+|vol\s*\d+|artigo|ebook|book|livro|manual|apostila|pdf|free|copia)\b$', 
            '', 
            cleaned, 
            flags=re.IGNORECASE
        ).strip()
        
    # Remove espaços extras de novo após o strip
    cleaned = ' '.join(cleaned.split())
    
    # Capitaliza
    cleaned = cleaned.title()
    
    return cleaned

def carregar_lista_livros(caminho):
    """Carrega a lista de livros a partir de um arquivo texto, detectando encodificação."""
    if not os.path.exists(caminho):
        print(f"[!] Arquivo de lista '{caminho}' nao encontrado.")
        return []
    
    # Tenta ler como UTF-8 primeiro, se falhar ou contiver caracteres substitutos, tenta cp1252/latin1
    encodings = ['utf-8-sig', 'utf-8', 'cp1252', 'latin1']
    content = None
    
    for enc in encodings:
        try:
            with open(caminho, 'r', encoding=enc) as f:
                text = f.read()
                # Se não houver muitos caracteres de substituição Unicode (U+FFFD), assume sucesso
                if "\ufffd" not in text:
                    content = text
                    print(f"[+] Lista de livros lida com sucesso usando codificacao: {enc}")
                    break
        except UnicodeDecodeError:
            continue
            
    if content is None:
        # Fallback de segurança com cp1252
        print("[-] Nao foi possivel determinar a codificacao sem erros. Usando cp1252 como fallback.")
        with open(caminho, 'r', encoding='cp1252', errors='ignore') as f:
            content = f.read()
            
    books = []
    for line in content.splitlines():
        line = line.strip()
        # Pula cabeçalhos e linhas vazias
        if not line or line.startswith('----') or line.lower().startswith('name'):
            continue
        books.append(line)
    return books

def carregar_arquivos_pasta(caminho):
    """Lista arquivos de texto ou e-books em uma pasta física."""
    if not os.path.exists(caminho):
        print(f"[!] Pasta de origem '{caminho}' nao encontrada.")
        return []
    
    extensoes = ('.txt', '.md', '.epub', '.pdf', '.mobi')
    arquivos = [f for f in os.listdir(caminho) if f.lower().endswith(extensoes)]
    return arquivos

def buscar_duckduckgo(query, delay=3.0):
    """Realiza busca no DuckDuckGo e extrai os snippets."""
    print(f"[*] Pesquisando no DuckDuckGo: '{query}'...")
    # Delay preventivo para evitar IP block
    time.sleep(delay + random.uniform(0.5, 1.5))
    
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=4))
            return results
    except Exception as e:
        print(f"[-] Erro na busca do DuckDuckGo para '{query}': {e}")
        return []

def chamar_api_gemini_grounded(book_title, api_key, model="gemini-2.5-pro"):
    """Envia o nome do livro ao Gemini e usa Google Search Grounding para coletar e estruturar os dados."""
    print(f"[*] Pesquisando e estruturando '{book_title}' via Gemini ({model}) com Google Search Grounding...")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    
    data_atual = datetime.now().strftime("%Y-%m-%d")
    
    prompt = f"""
Você é o Antigravity, assistente de IA pessoal do terapeuta Leonardo. 
Faça uma pesquisa no Google sobre o livro "{book_title}" para coletar seus dados verdadeiros (autor, ano de publicação, sinopse e temas principais).
Em seguida, preencha o template Markdown abaixo seguindo as diretrizes estruturais e de tom da nossa egrégora.

DIRETRIZES DE TOM:
- Fale de forma direta, honesta e sem enrolação ("papo reto", tom de irmão mais velho).
- Priorize a utilidade prática das ideias do livro para o autoconhecimento, a terapia e o desenvolvimento.
- Identifique conexões com a espiritualidade de cura (como SACM, Arcturianos, apometria, mecânica de crenças de Bashar ou psicologia de Jung/Grof) se aplicável.

INSTRUÇÕES DO TEMPLATE:
- Identifique o Autor verdadeiro.
- Escolha a categoria correta entre as seguintes opções exatas: Espiritualidade, Apometria, Psicologia, Nutricao, Magia, Desenvolvimento Pessoal, Outros.
- Escreva as seções 1, 2 e 3 de forma concisa e útil.
- Retorne APENAS o bloco de código Markdown estruturado do frontmatter até a última seção, sem decorações extras de markdown ou explicações.

TEMPLATE A PREENCHER:

---
titulo: "{book_title}"
autor: "[Identifique o Autor]"
ano: "[Ano de Publicação do livro]"
categoria: "[Escolha uma das categorias listadas]"
data_coleta: "{data_atual}"
fonte: "Google Search Grounded + Gemini API"
tags: ["pesquisa_livro", "[tag1]", "[tag2]"]
---

# {book_title}

> **Nota do Sistema:** Sinopse e análise geradas por automação de pesquisa inteligente.

## 1. Conceito Central
[Explique de forma concisa e direta a tese principal do livro baseando-se nos resultados da pesquisa]

## 2. Mecanismos e Funcionamento
[Como o autor descreve que esses conceitos funcionam no plano prático ou sutil? Quais os temas chave?]

## 3. Ferramentas de Intervenção
[Quais ferramentas práticas, exercícios, decretos ou ganchos terapêuticos este livro oferece para uso clínico?]
"""

    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "tools": [{
            "googleSearch": {}
        }]
    }
    
    max_retries = 3
    backoff = 5.0
    
    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, json=data, timeout=40)
            if response.status_code == 200:
                result = response.json()
                candidate = result['candidates'][0]
                text = candidate['content']['parts'][0]['text']
                metadata = candidate.get('groundingMetadata', {})
                return text, metadata
            elif response.status_code in [429, 503]:
                print(f"[-] Gemini API retornou {response.status_code}. Aguardando {backoff}s para tentar novamente (Tentativa {attempt+1}/{max_retries})...")
                time.sleep(backoff)
                backoff *= 2
            else:
                print(f"[-] Gemini API retornou erro {response.status_code}: {response.text}")
                return None, None
        except Exception as e:
            print(f"[-] Erro ao se conectar com a API do Gemini (Tentativa {attempt+1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                time.sleep(backoff)
                backoff *= 2
            else:
                return None, None
                
    return None, None

def estruturar_offline(snippets, book_title):
    """Estrutura os dados offline caso a API do Gemini não esteja ativa."""
    data_atual = datetime.now().strftime("%Y-%m-%d")
    
    snippets_text = ""
    for idx, res in enumerate(snippets):
        snippets_text += f"- **{res.get('title')}** ({res.get('href')})\n  {res.get('body')}\n\n"
        
    template = f"""---
titulo: "{book_title}"
autor: "A Identificar"
ano: "Desconhecido"
categoria: "A_Classificar"
data_coleta: "{data_atual}"
fonte: "Busca DuckDuckGo (Offline)"
tags: ["pesquisa_livro", "legado"]
---

# {book_title}

> **Nota do Sistema:** Ficha criada offline. Conteúdo de busca reunido abaixo para classificação manual.

## 1. Conceito Central
*Espaço para processamento da tese principal do livro.*

## 2. Mecanismos e Funcionamento
*Temas-chave e funcionamento prático/sutil.*

## 3. Ferramentas de Intervenção
*Exercícios, comandos ou ganchos úteis.*

---
## Conteúdo de Referência (Pesquisa):

{snippets_text}
"""
    return template

def atualizar_indice_md():
    """Lê todos os arquivos MD gerados e cria um índice consolidado com tabela."""
    print("[*] Atualizando o índice central de livros...")
    
    livros_processados = []
    
    # Varre a pasta de pesquisas
    if os.path.exists(PASTA_PESQUISAS):
        for root, dirs, files in os.walk(PASTA_PESQUISAS):
            for file in files:
                if file.endswith('.md') and not file.startswith('_'):
                    caminho_completo = os.path.join(root, file)
                    try:
                        # Extrai frontmatter
                        with open(caminho_completo, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        frontmatter_match = re.match(r'^---(.*?)---', content, re.DOTALL)
                        if frontmatter_match:
                            fm_text = frontmatter_match.group(1)
                            titulo = re.search(r'titulo:\s*"(.*?)"', fm_text)
                            autor = re.search(r'autor:\s*"(.*?)"', fm_text)
                            if not autor:
                                autor = re.search(r'autor:\s*(.*?)\n', fm_text)
                            categoria = re.search(r'categoria:\s*"(.*?)"', fm_text)
                            if not categoria:
                                categoria = re.search(r'categoria:\s*(.*?)\n', fm_text)
                            
                            titulo_str = titulo.group(1) if titulo else file.replace('.md', '').title()
                            autor_str = autor.group(1).strip() if autor else "A Identificar"
                            cat_str = categoria.group(1).strip() if categoria else "Outros"
                            
                            rel_path = os.path.relpath(caminho_completo, PASTA_PESQUISAS).replace('\\', '/')
                            
                            livros_processados.append({
                                "titulo": titulo_str,
                                "autor": autor_str,
                                "categoria": cat_str,
                                "caminho": rel_path
                            })
                    except Exception as e:
                        print(f"[-] Erro ao indexar {file}: {e}")
                        
    # Cria o Markdown do Índice
    indice_content = f"""# 📚 Biblioteca e Acervo de Pesquisa de Livros

Este é o catálogo consolidado dos livros identificados na biblioteca de Leonardo. O sistema realiza pesquisas automatizadas sobre os temas e aplicações clínicas de cada obra.

## Acervo Geral

| Livro | Autor | Categoria | Ficha de Análise |
| :--- | :--- | :--- | :--- |
"""
    
    # Ordena os livros por categoria e título
    livros_processados.sort(key=lambda x: (x['categoria'], x['titulo']))
    
    for livro in livros_processados:
        link_md = f"[[{livro['caminho'].replace('.md', '')}]]"
        indice_content += f"| {livro['titulo']} | {livro['autor']} | {livro['categoria']} | {link_md} |\n"
        
    with open(ARQUIVO_INDICE, 'w', encoding='utf-8') as f:
        f.write(indice_content)
        
    print(f"[+] Índice atualizado com sucesso em {ARQUIVO_INDICE} ({len(livros_processados)} livros catalogados).")

def principal():
    parser = argparse.ArgumentParser(description="Antigravity Core - Automação de Pesquisa de Livros")
    parser.add_argument("--file", default="lista_livros.txt", help="Caminho para o arquivo TXT com a lista de livros")
    parser.add_argument("--folder", default=None, help="Caminho para a pasta física de arquivos antigos para refatorar")
    parser.add_argument("--limit", type=int, default=None, help="Número máximo de livros a processar nesta rodada")
    parser.add_argument("--delay", type=float, default=3.0, help="Delay (segundos) entre pesquisas no DuckDuckGo")
    parser.add_argument("--model", default="gemini-2.5-pro", help="Modelo da API Gemini a utilizar")
    args = parser.parse_args()

    print("=== ANTIGRAVITY CORE: INICIANDO AUTOMAÇÃO DE PESQUISA ===")

    # Garante a existência das pastas
    if not os.path.exists(PASTA_PESQUISAS):
        os.makedirs(PASTA_PESQUISAS)
        
    # Inicializa ou carrega o cache
    cache = {}
    if os.path.exists(ARQUIVO_CACHE):
        try:
            with open(ARQUIVO_CACHE, 'r', encoding='utf-8') as f:
                cache = json.load(f)
        except Exception:
            cache = {}

    # Define a lista de livros a processar
    livros_brutos = []
    origem_is_file = True

    if args.folder:
        print(f"[*] Escaneando arquivos físicos na pasta: '{args.folder}'")
        livros_brutos = carregar_arquivos_pasta(args.folder)
        origem_is_file = False
    else:
        print(f"[*] Carregando lista de livros do arquivo: '{args.file}'")
        livros_brutos = carregar_lista_livros(args.file)

    if not livros_brutos:
        print("[!] Nenhum livro ou arquivo para processar.")
        return

    print(f"[+] Total de {len(livros_brutos)} itens identificados.")

    # Filtra os que já estão no cache
    livros_para_pesquisa = []
    for item in livros_brutos:
        if item in cache and cache[item].get("status") == "completed":
            continue
        livros_para_pesquisa.append(item)

    print(f"[+] {len(livros_brutos) - len(livros_para_pesquisa)} itens já estavam processados no cache.")
    print(f"[*] {len(livros_para_pesquisa)} itens precisam de pesquisa.")

    if args.limit:
        livros_para_pesquisa = livros_para_pesquisa[:args.limit]
        print(f"[*] Limite de processamento definido para esta rodada: {args.limit} itens.")

    processados_nesta_rodada = 0

    for idx, item in enumerate(livros_para_pesquisa):
        print(f"\n[{idx+1}/{len(livros_para_pesquisa)}] Processando: '{item}'")
        
        query_busca = limpar_nome_livro(item)
        print(f"[*] Nome Limpo para Busca: '{query_busca}'")
        
        conteudo_md = None
        categoria_identificada = "Outros"
        titulo_identificado = query_busca
        autor_identificado = "A Identificar"
        ano_identificado = "Desconhecido"
        
        # 1. Tenta usar o Gemini com Google Search Grounding se a chave estiver configurada
        if GEMINI_API_KEY:
            print(f"[*] Usando pesquisa inteligente via Gemini + Google Search Grounding...")
            # Delay reduzido para 0.5 segundos (velocidade máxima para API com faturamento ativo)
            time.sleep(0.5)
            text_md, metadata = chamar_api_gemini_grounded(query_busca, GEMINI_API_KEY, model=args.model)
            if text_md:
                # Limpa delimitadores de bloco de código markdown
                text_md = text_md.strip()
                if text_md.startswith("```markdown"):
                    text_md = text_md[11:].strip()
                elif text_md.startswith("```"):
                    text_md = text_md[3:].strip()
                if text_md.endswith("```"):
                    text_md = text_md[:-3].strip()
                conteudo_md = text_md
                
                # Extrai dados chaves gerados pelo Gemini do Markdown para organizar as pastas
                cat_match = re.search(r'categoria:\s*"(.*?)"', conteudo_md)
                if not cat_match:
                    cat_match = re.search(r'categoria:\s*(.*?)\n', conteudo_md)
                if cat_match:
                    cat_val = cat_match.group(1).strip()
                    # Normaliza a categoria
                    for cat in CATEGORIAS_VALIDAS:
                        if cat.lower() in cat_val.lower():
                            categoria_identificada = cat
                            break
                            
                titulo_match = re.search(r'titulo:\s*"(.*?)"', conteudo_md)
                if titulo_match:
                    titulo_identificado = titulo_match.group(1)
                    
                autor_match = re.search(r'autor:\s*"(.*?)"', conteudo_md)
                if not autor_match:
                    autor_match = re.search(r'autor:\s*(.*?)\n', conteudo_md)
                if autor_match:
                    autor_identificado = autor_match.group(1).strip()
                    
                ano_match = re.search(r'ano:\s*"(.*?)"', conteudo_md)
                if not ano_match:
                    ano_match = re.search(r'ano:\s*(.*?)\n', conteudo_md)
                if ano_match:
                    ano_identificado = ano_match.group(1).strip()
                
                # Adiciona links de referência extraídos do Google Search Grounding
                if metadata and 'groundingChunks' in metadata:
                    referencias = "\n\n## Fontes de Pesquisa Google:\n"
                    seen_urls = set()
                    for chunk in metadata['groundingChunks']:
                        web_data = chunk.get('web', {})
                        uri = web_data.get('uri')
                        title = web_data.get('title', 'Fonte Web')
                        if uri and uri not in seen_urls:
                            referencias += f"- [{title}]({uri})\n"
                            seen_urls.add(uri)
                    conteudo_md += referencias
        
        # 2. Fallback para busca clássica DuckDuckGo se a API falhou ou não está configurada
        if not conteudo_md:
            print("[*] Usando busca clássica DuckDuckGo + estruturação offline...")
            queries_tentativas = [
                f"{query_busca} livro sinopse",
                f"{query_busca} livro",
                query_busca
            ]
            
            snippets = []
            for q in queries_tentativas:
                snippets = buscar_duckduckgo(q, delay=args.delay)
                if snippets:
                    break
                print(f"[*] Sem resultados para '{q}', tentando outra query...")
                
            if not snippets:
                print(f"[-] Sem resultados de busca para '{query_busca}' em nenhuma das tentativas. Pulando...")
                continue
                
            conteudo_md = estruturar_offline(snippets, query_busca)
            categoria_identificada = "Outros"
            
        # 3. Salva o arquivo md na pasta correspondente
        cat_slug = slugify(categoria_identificada)
        pasta_categoria = os.path.join(PASTA_PESQUISAS, cat_slug)
        if not os.path.exists(pasta_categoria):
            os.makedirs(pasta_categoria)
            
        nome_arquivo = f"{slugify(titulo_identificado)}.md"
        caminho_arquivo = os.path.join(pasta_categoria, nome_arquivo)
        
        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                f.write(conteudo_md)
            print(f"[+] Arquivo salvo com sucesso em: {caminho_arquivo}")
            
            # 4. Atualiza o cache de controle
            cache[item] = {
                "title": titulo_identificado,
                "author": autor_identificado,
                "year": ano_identificado,
                "category": categoria_identificada,
                "status": "completed",
                "caminho": caminho_arquivo,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Salva o arquivo de cache a cada iteração
            with open(ARQUIVO_CACHE, 'w', encoding='utf-8') as f:
                json.dump(cache, f, indent=4, ensure_ascii=False)
                
            processados_nesta_rodada += 1
            
        except Exception as e:
            print(f"[-] Erro ao salvar arquivo ou atualizar cache: {e}")

    # Ao final de todo o lote, reconstrói o índice central
    if processados_nesta_rodada > 0 or not os.path.exists(ARQUIVO_INDICE):
        atualizar_indice_md()

    print(f"\n=== PROCESSAMENTO CONCLUIDO ===")
    print(f"[+] {processados_nesta_rodada} novos livros catalogados nesta rodada.")

if __name__ == "__main__":
    principal()
