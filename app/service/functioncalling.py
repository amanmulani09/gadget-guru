## function calling allows llms to call external tools, APIs, & DBs.
# the model decides when and how to use functions based on the conversation. 


from openai import OpenAI
import json
import os
from typing import Literal
client = OpenAI(api_key="##")

## Step 1 :  define available functions 
def get_weather(location:str,unit:str="fahrenheit"):
    """ get current weather for a location"""
    
    # in real app a call weather api 
    
    return {
        "location":location,
        "temprature":"72",
        "unit":unit,
        "conditions":"sunny"
    }
    
def get_stock_price(stocks:list[str]) -> dict[str, Literal[]]:
    "get latest stock price for a perticular stock"
    
    # in real app call a stock checker api 
    
    prices = {"AAPL":"178.5", "GOOGL":"88.11","MSFT":"1122"}
    return {"stocks":stocks,"prices":prices}

# Step 2 : function schemas for model

tools = [
    {
        "type":"function",
        "function":{
            "name":"get_weather",
            "description":"Get Weather",
            "parameters":{
                "type":"object",
                "properties":{
                    "location":{"type":"string"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "name": "get_stock_price",
        "description": "Get stock price",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"}
            },
            "required": ["symbol"]
        }
    }
]

# step 3 ask the model 
response = client.responses.create(
    model="gpt-4o",
    input="what is the weather in pune and HDFC stock price"
)

# Step 4: Execute tool calls based on LLM Response
outputs = []

for tool_call in response.output:
    if tool_call.type == "tool_call":
        
        name = tool_call.name
        args = json.loads(tool_call.arguments)
        
        if name =="get_weather":
            result = get_weather(**args)
        elif name == "get_stock_price":
            result = get_stock_price(**args)
            
        
        outputs.append({
           "tool_call_id": tool_call.id,
            "output": json.dumps(result)
        })
        
        
# Step 5 : send the result back to LLM 

final_response = client.responses.create(
    model="gpt-4",
    input=outputs,
    previous_response_id=response.id
)

print(final_response.output_text)