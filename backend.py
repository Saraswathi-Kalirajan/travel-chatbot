from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read keys from environment
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_MODEL = os.getenv("GOOGLE_MODEL", "models/gemini-1.5-flash")

if not GOOGLE_API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY not found. Please check your .env file!")

# Initialize the Gemini LLM
llm = ChatGoogleGenerativeAI(model=GOOGLE_MODEL, google_api_key=GOOGLE_API_KEY)

# Define the conversation state
class State(dict):
    messages: list

# Create LangGraph conversation flow
graph = StateGraph(State)

def call_model(state: State):
    try:
        user_message = state["messages"][-1]
        response = llm.invoke(user_message)
        state["messages"].append(response.content)
    except Exception as e:
        state["messages"].append(f"⚠️ Error talking to Gemini: {e}")
    return state

# Add node and edges to the graph
graph.add_node("llm", call_model)
graph.set_entry_point("llm")
graph.add_edge("llm", END)

conversation = graph.compile()

# Initialize FastAPI app
app = FastAPI(title="Travel Chatbot Backend")

# Enable CORS so Streamlit frontend can access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Define request body
class ChatRequest(BaseModel):
    message: str

# API endpoint
@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        if not request.message.strip():
            return {"response": "⚠️ Please type a message."}
        
        result = conversation.invoke({"messages": [request.message]})
        return {"response": result["messages"][-1]}
    except Exception as e:
        return {"response": f"⚠️ Backend crashed: {str(e)}"}

# Run command: uvicorn backend:app --reload --port 8000
