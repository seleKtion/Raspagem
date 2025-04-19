from fastapi import FastAPI, Query
from bs4 import BeautifulSoup
import httpx

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Servidor de raspagem online!"}

@app.get("/raspar")
def raspar_site(url: str = Query(..., description="URL do site a ser raspado")):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = httpx.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "Sem título encontrado"
        return {"url": url, "title": title}
    except Exception as e:
        return {"erro": str(e)}
