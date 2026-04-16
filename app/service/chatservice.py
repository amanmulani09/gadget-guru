from openai import OpenAI
from prompts.gadget import GADGET_GURU_SYSTEM_PROMPT
from app.core.security import sanitise_input, is_malicious_input

class ChatService:
    
    def __init__(self):
        self.client:OpenAI = OpenAI(api_key="")
        
    
    def get_llm_response(self,user_input:str):
        
        if is_malicious_input(user_input):
            return {
                "reply":"I'm here to help with tech related queries only"
            }
        
        clean_input = sanitise_input(user_input)
        
        response = self.client.chat.completions.create(
            model="gpt-5.3",
            messages=[
                {"role":"user","content":GADGET_GURU_SYSTEM_PROMPT},
                {"role":"system","content":clean_input}
            ],
            temperature=0.3
        )
        
        return {
            "response":response.choices[0].message.content
        }
        
        
def get_chat_service():
    return ChatService()