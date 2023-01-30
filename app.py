from fastapi import FastAPI
from views.main.router import main_router


app = FastAPI()
app.include_router(main_router)