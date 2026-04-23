from pydantic import BaseModel, Field, validator

class ChatRequest(BaseModel):
    message:str = Field(..., min_length=1, max_length=2000)
    
    @validator('message')
    def validate_message(cls,v:str):
        if not v.strip():
            raise ValueError("message cannot be empty")
        return v 