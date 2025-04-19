# Scraper API

Uma API simples de raspagem de dados para o site da Intelbras.

## Como usar:

1. Envie uma requisição `GET` para `/raspar?url=<URL_DO_SITE>`.
2. A resposta será um JSON com o título da página.

Exemplo:

```bash
curl "https://your-deployed-api-url/raspar?url=https://www.intelbras.com.br"
