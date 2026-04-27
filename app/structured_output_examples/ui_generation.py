from openai import OpenAI
from pydantic import BaseModel
from typing import List
client = OpenAI()

class UIType(BaseModel):
    div = "div",
    button = "button"
    header = "header"
    footer = "footer"
    input = "input"
    section = "section"
    form = "form"
    field = "field"
    
class Attributes(BaseModel):
    name : str
    value : str

class UI(BaseModel):
    type : UIType
    label:str
    children:List["UI"]
    attributes: List[Attributes]
    
UI.model_rebuild()

class Response(BaseModel):
    ui: UI
    
    
response = client.responses.parse(
    model="chatgpt-4o-latest",
    input=[
        {
            "role":"system",
            "content":"ou are a UI generator AI. Convert the user input into a UI."
        },
        {
            "role":"user",
            "content":"Make a User Profile Form"
        }
    ],
    text_format=Response
)

ui = response.output_parsed
    