from fastapi import APIRouter, Depends
from app.service.chatservice import get_chat_service, ChatService
from app.model.chat import ChatRequest
router = APIRouter()

@router.post("/chat")
def get_completion(body:ChatRequest, chat_service:ChatService=Depends(get_chat_service)):
    return chat_service.get_llm_response(body.message)