from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()
# @app.get(path="/", summary ="Главная ручка", tags=['основные ручки'])
# def root():
#     return"Hello world Aru"

# if __name__ == "__main__":
#     uvicorn.run("main.app", )

books = [
    {
        "id":1,
        "title": "Асинрхоронность в пайтон",
        "author": "Мэтью",
    },
    {
        "id":2,
        "title":"backend разработка пайтон",
        "author": "Артем",
    },
]

@app.get("/books")
def read_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")


if __name__ == "__main__":
    uvicorn.run("main.app", reload=True)