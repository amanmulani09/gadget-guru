from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()

class ResearchPaperExtraction(BaseModel):
    title:str
    author:str
    date: str 
    tags:list[str]
    
    
response = client.responses.parse(
    model="chatgpt-4o-latest",
    input=[
        {
            "role":"system",
            "content": "You are an expert at structured data extraction. You will be given unstructured text from a research paper and should convert it into the given structure.",
        },
        {
            "role":"user",
            "content":"..."
        }
    ]
)

research_paper = response.output_parsed