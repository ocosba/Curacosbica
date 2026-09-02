const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 5001;
const DB_PATH = path.join(__dirname, 'db.json');

// Define cabeçalhos padrão para habilitar CORS
function setCorsHeaders(res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
}

const server = http.createServer((req, res) => {
  setCorsHeaders(res);

  // Responde imediatamente a requisições de preflight do CORS (OPTIONS)
  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  const url = new URL(req.url, `http://${req.headers.host}`);

  // Endpoint de status
  if (url.pathname === '/api/status' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ status: 'online', timestamp: new Date().toISOString() }));
    return;
  }

  // Endpoint para carregar o banco de dados simulado local
  if (url.pathname === '/api/load-db' && req.method === 'GET') {
    if (fs.existsSync(DB_PATH)) {
      fs.readFile(DB_PATH, 'utf8', (err, data) => {
        if (err) {
          res.writeHead(500, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ error: 'Erro ao ler o banco de dados.' }));
          return;
        }
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(data);
      });
    } else {
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({})); // Retorna banco vazio
    }
    return;
  }

  // Endpoint para salvar o banco de dados local
  if (url.pathname === '/api/save-db' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => {
      body += chunk.toString();
    });
    req.on('end', () => {
      try {
        const parsed = JSON.parse(body);
        fs.writeFile(DB_PATH, JSON.stringify(parsed, null, 2), 'utf8', (err) => {
          if (err) {
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Erro ao gravar no banco de dados.' }));
            return;
          }
          res.writeHead(200, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ success: true, message: 'Dados salvos com sucesso.' }));
        });
      } catch (err) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'JSON inválido.' }));
      }
    });
    return;
  }

  // Endpoint para gravação direta de notas Markdown no projeto
  if (url.pathname === '/api/save-file' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => {
      body += chunk.toString();
    });
    req.on('end', () => {
      try {
        const { filePath, content } = JSON.parse(body);
        if (!filePath || !content) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ error: 'filePath e content são obrigatórios.' }));
          return;
        }
        
        // Validação básica de segurança de diretório
        const safePath = path.resolve(__dirname, filePath);
        if (!safePath.startsWith(__dirname)) {
          res.writeHead(403, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ error: 'Acesso negado fora da raiz do projeto.' }));
          return;
        }

        // Garante a existência da pasta mãe
        const dir = path.dirname(safePath);
        if (!fs.existsSync(dir)) {
          fs.mkdirSync(dir, { recursive: true });
        }

        fs.writeFile(safePath, content, 'utf8', (err) => {
          if (err) {
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Erro ao salvar o arquivo físico.' }));
            return;
          }
          res.writeHead(200, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ success: true, message: 'Arquivo salvo no projeto.' }));
        });
      } catch (err) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'JSON inválido.' }));
      }
    });
    return;
  }

  // Rota desconhecida
  res.writeHead(404, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ error: 'Rota não encontrada.' }));
});

server.listen(PORT, () => {
  console.log(`[+] Micro-Servidor Local do Antigravity rodando em http://localhost:${PORT}`);
});
