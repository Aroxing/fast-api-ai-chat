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
            # Get response from OpenAI
            response = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo",
                messages=self.chat_histories[client_id],
                max_tokens=1000
            )
            
            ai_message = response.choices[0].message.content
            
            # Add AI response to history
            self.chat_histories[client_id].append({
                "role": "assistant",
                "content": ai_message
            })
            
            return ai_message
            
        except Exception as e:
            return f"Error: {str(e)}"