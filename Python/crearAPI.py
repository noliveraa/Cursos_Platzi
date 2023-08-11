from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')

def get_list():
    return[1,2,3]

@app.get('/archivo', response_class=HTMLResponse)

def get_list():
    return"""
    <h1>Hola esto es un HTML traido desde un servidor creado en python</h1>
    """