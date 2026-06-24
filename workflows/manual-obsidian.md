# 🗺️ Guia de Implementação e Uso do Obsidian: Projeto Antigravity

Este guia orienta como utilizar o seu cofre do **Obsidian** integrado com as pesquisas do Antigravity (IA), unificando a teoria clínica e somática com a prática multidimensional do SACM na sua rotina de atendimentos.

---

## 1. Como Abrir o Cofre no Obsidian
1. Abra o aplicativo **Obsidian** no seu computador.
2. Clique em **"Open folder as vault"** (Abrir pasta como cofre).
3. Selecione o diretório do projeto: `C:\Users\leoco\OneDrive\Desktop\cosba.infinitando`.
4. O Obsidian vai carregar automaticamente toda a estrutura de pastas que organizamos.

---

## 2. A Estrutura de Pastas no seu Painel Lateral

Dentro do Obsidian, você verá as seguintes pastas na barra lateral esquerda:

*   📂 **`context/`** (A sua base de dados central)
    *   📂 **`leonardo/`** — O seu Dossiê de Alma, Mapa Astrológico, Numerologia e Oráculo Galáctico.
    *   📂 **`sacm/`** — A descrição dos 28 Símbolos Arcturianos (Níveis I a IV) e protocolos das Câmaras de Luz.
    *   📂 **`psicologia/`** — Artigos de apoio sobre a Experiência Somática (Levine), Esquemas (Young) e Sombra (Jung).
    *   📂 **`pesquisas-livros/`** — **A sua Biblioteca Inteligente**. Onde cada livro pesquisado pela IA é salvo de forma organizada por categorias (`psicologia/`, `espiritualidade/`, `desenvolvimento-pessoal/`, etc.).
*   📂 **`workflows/`** — Onde ficam as receitas das suas tarefas de negócios e guias operacionais (como este manual).

---

## 3. Passo a Passo do Uso Prático no Atendimento

### Passo 1: Abertura e Leitura de Campo (Sua Presença)
Antes da sessão começar, abra o seu Obsidian:
1. Abra a pasta **`context/clientes/`** e crie a nota do cliente da semana (use o arquivo `[[clientes/_template-cliente|template-cliente]]`).
2. Sintonize a egrégora fazendo a respiração de limiar siriana e visualize os **7 símbolos do SACM** ao redor da sua casa para blindar Stephanie e o lar contra vazamentos.

### Passo 2: O Diálogo e Diagnóstico sutil (O "Hack")
Durante a conversa com o cliente:
1. Use a sensibilidade da **Serpente Vermelha (Chicchan)** para ler a tensão corporal dele (bloqueio somático) e as crenças de escassez/medo.
2. Anote as palavras-chave na nota do cliente.

### Passo 3: O Cruzamento no Obsidian (Linkando a Teoria)
1. Para linkar a dor do cliente a um livro ou conceito do seu acervo no Obsidian, digite colchetes duplos `[[`. O Obsidian abrirá uma lista suspensa para autocompletar.
   * *Exemplo:* Se o cliente tem problemas de entrega afetiva e medo de rejeição, digite `[[tudo-sobre-o-amor-bell-hooks]]` na ficha dele.
   * *Exemplo:* Se ele tem um bloqueio de congelamento por trauma físico, digite `[[levine-experiencia-somatica]]`.
2. Adicione os símbolos que você projetou privadamente no chakra cardíaco dele (ex: `[[sacm/nivel-1/KALYSHMAN]]`).

---

## 4. O Poder Visual do Obsidian: O Visualizador de Grafos

Esta é a parte mais mágica da integração. No menu lateral esquerdo do Obsidian, clique no ícone que se parece com uma teia de aranha (ou aperte `Ctrl + G`) para abrir o **Graph View (Visualizador de Grafos)**.

```
       [Ficha do Cliente 001]
             │         │
             ▼         ▼
  [[KALYSHMAN]] ◄──► [[Tudo Sobre o Amor]]
```

### O que o Gráfico vai te revelar ao longo do tempo:
*   Você verá nós (bolinhas) representando seus clientes, livros e símbolos.
*   **Conexões Naturais:** Com o tempo, você notará que o símbolo `KALYSHMAN` se conecta tanto à ficha do `Cliente X` quanto ao livro `O Despertar do Tigre (Peter Levine)`.
*   **Seu Mapa de Aprendizado:** O gráfico revelará visualmente quais símbolos Arcturianos você mais usa para quais tipos de bloqueios somáticos humanos de forma empírica, virando a sua maior fonte de estudos prática.

---

## 5. Como Atualizar a sua Biblioteca com Novos Livros
1. Se você quiser que o robô pesquise novos livros, basta abrir o arquivo [lista_livros.txt](file:///c:/Users/leoco/OneDrive/Desktop/cosba.infinitando/lista_livros.txt) e escrever no final dele: `Título do Livro - Nome do Autor`.
2. Abra o terminal na pasta raiz do projeto e digite:
   `python antigravity_core.py`
3. O script vai ler a lista, pular os mais de 330 livros que já estão salvos e pesquisar apenas as novidades, criando os novos Markdown e gerando os links bidirecionais no Obsidian imediatamente de graça!
4. O índice central [pesquisas-livros/_indice.md](file:///c:/Users/leoco/OneDrive/Desktop/cosba.infinitando/context/pesquisas-livros/_indice.md) será atualizado na hora em formato de tabela interativa.
