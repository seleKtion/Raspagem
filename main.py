import httpx
from fastapi import FastAPI, Query
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Servidor de raspagem online!"}

@app.get("/raspar")
def raspar_intelbras(url: str = Query(..., description="https://www.intelbras.com/pt-br/energia/nobreaks/allproducts")):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = httpx.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "Sem título encontrado"
        return {"url": url, "title": title}
    except Exception as e:
        return {"erro": str(e)}
