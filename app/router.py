from app.schema import Chat, MessageInput

from fastapi import APIRouter
from app.services import generate_response
router = APIRouter()

@router.post("/chat", response_model=Chat)
def chat(body: MessageInput):
    response = generate_response(body.message)
    return Chat(response=response)
