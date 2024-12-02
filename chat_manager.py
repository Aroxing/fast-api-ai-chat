import openai
from typing import Dict, List
import os
from dotenv import load_dotenv

load_dotenv()

class ChatManager:
    def __init__(self):
        self.chat_histories: Dict[str, List[Dict]] = {}
        openai.api_key = os.getenv("OPENAI_API_KEY")
    
    def remove_chat_history(self, client_id: str):
        if client_id in self.chat_histories:
            del self.chat_histories[client_id]
    
    async def get_ai_response(self, message: str, client_id: str) -> str:
        if client_id not in self.chat_histories:
            self.chat_histories[client_id] = []
        
        # Add user message to history
        self.chat_histories[client_id].append({
            "role": "user",
            "content": message
        })
        
        try:
            response = openai.Completion.create(
                # model name used here is text-davinci-003
                # there are many other models available under the
                # umbrella of GPT-3
                model="gpt-3.5-turbo-0125",
                # passing the user input
                prompt=message,
                # generated output can have "max_tokens" number of tokens
                max_tokens=150,
                # number of outputs generated in one call
                n=1
            )
            
            return response
            
        except Exception as e:
            return f"Error: {str(e)}" 