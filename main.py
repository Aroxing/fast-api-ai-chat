import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
from chat_manager import ChatManager
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add this near the top of the file after creating the FastAPI app
app.mount("/static", StaticFiles(directory="static"), name="static")

chat_manager = ChatManager()

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    try:
        while True:
            # Receive message from client
            message = await websocket.receive_text()
            
            # Get AI response
            ai_response = await chat_manager.get_ai_response(message, client_id)
            
            # Send response back to client
            await websocket.send_text(ai_response)
            
    except WebSocketDisconnect:
        chat_manager.remove_chat_history(client_id) 

@app.get("/", response_class=HTMLResponse)
async def get_chat_page():
    with open(os.path.join(os.path.dirname(__file__), "templates", "index.html")) as f:
        return f.read()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)