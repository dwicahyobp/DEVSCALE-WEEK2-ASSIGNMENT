from pydantic import BaseModel

class MessageInput (BaseModel):
    message: str

class Chat(BaseModel):
    response: str