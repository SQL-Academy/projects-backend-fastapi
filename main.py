from fastapi import FastAPI

app = FastAPI()


@app.get("/tasks")
def get_tasks():
    return [
        {"id": 1, "title": "Купить хлеб", "done": False},
        {"id": 2, "title": "Позвонить врачу", "done": False},
        {"id": 3, "title": "Закончить курс", "done": False},
    ]
