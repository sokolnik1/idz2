from fastapi import FastAPI
from public.users import router as user_router
from models.index import router as index_router

app = FastAPI()

app.include_router(user_router, prefix="/api")
app.include_router(index_router)
