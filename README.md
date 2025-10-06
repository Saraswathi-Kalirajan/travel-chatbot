
---

````markdown
# 🌏 Travel Assistant Chatbot

A conversational **Travel Assistant Chatbot** built using **Streamlit**, **FastAPI**, and **Google Gemini LLM**.  
The chatbot can answer general questions, provide empathetic responses, and help users with travel-related queries.

---

## Features

- Interactive chatbot interface using **Streamlit**  
- Backend API built with **FastAPI**  
- Conversation managed by **LangGraph**  
- AI responses powered by **Google Gemini**  
- Supports session-based chat history  
- Empathetic and context-aware responses

---

## Demo

1. **Run backend**:

```bash
python -m uvicorn backend:app --reload --port 8000
```

2. **Run frontend**:

```bash
python -m streamlit run frontend.py
```

3. Open your browser at [http://localhost:8501](http://localhost:8501) and start chatting!

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/travel-chatbot.git
cd travel-chatbot
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the following content:

```
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
GOOGLE_MODEL=models/gemini-2.5-flash
BACKEND_URL=http://localhost:8000
```

---

## Project Files

* `backend.py` — FastAPI backend serving `/chat` endpoint  
* `frontend.py` — Streamlit frontend for the chatbot UI  
* `listmodels.py` — Script to list available Gemini models  
* `run_all.bat` — Optional batch file to start backend & frontend together  
* `.env` — Stores your API key and model (excluded from GitHub)

---

## Usage

1. Start backend and frontend as described in the demo section.  
2. Type a message in the Streamlit input box or test via Swagger UI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).  
3. Enjoy your interactive Travel Chatbot!

---

## Notes

* Make sure your Gemini API key is valid.  
* Use `listmodels.py` to see all available Gemini models.  
* You can customize the chatbot by modifying the LangGraph conversation flow.

---
