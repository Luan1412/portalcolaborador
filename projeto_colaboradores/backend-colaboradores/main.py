from fastapi import FastAPI

app = FastAPI(
    title="API de Colaboradores",
    description="Backend para o sistema de gestão de funcionários"
)

@app.get("/")
def home():
    return{"MENSAGEM":"API RODANDO COM SUCESSO!"}