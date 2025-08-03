from fastapi import FastAPI

app = FastAPI()
@app.get(path="/", summary ="Главная ручка", tags=['основные ручки'])
def root():
    return"Hello world Aru"
