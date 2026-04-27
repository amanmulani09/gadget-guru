from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()

# define the output model 
class Step(BaseModel):
    explanation: str
    output: str
    
class MathReasoning(BaseModel):
    steps : list[Step]
    final_answer : str
    
response = client.responses.parse(
    model="gpt-5.1-2025-11-13",
    input=[
        {
            "role":"system",
            "content":"You are a helpful math tutor. Guide the user through the solution step by step."
        },
        {
            "role":"user",
            "content":"how can I solve 8x + 7 = -23"
        }
    ],
    text_format=MathReasoning
)