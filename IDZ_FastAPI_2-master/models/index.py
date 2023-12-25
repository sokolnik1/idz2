from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def F_indexh():
    return {"message": "Hello, world!"}
