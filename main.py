from fastapi import FastAPI

from routes import tasks

app = FastAPI()
app.include_router(tasks.router)
