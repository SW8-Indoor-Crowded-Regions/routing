from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class MessageRequest(BaseModel):
    msg: str


@router.get("/test")
async def get_test():
    return {"message": "API is working!"}


@router.post("/test")
async def post_test(request: MessageRequest):
    return {"message": f"Received: {request.msg}"}
