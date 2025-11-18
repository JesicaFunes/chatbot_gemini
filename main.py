from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Chatbot Gemini API", description= "API para el chatbot Gemini", version="1.0.0")

app.include_router(router, prefix="/api")