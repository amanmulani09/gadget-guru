from pydantic import BaseModel
from typing import Optional
class PromptBase(BaseModel):
    model:str = "gpt-4"
    user_prompt:str
    temperature:Optional[float] = 0.7
    max_tokens:int = 500