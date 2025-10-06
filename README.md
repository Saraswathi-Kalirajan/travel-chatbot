# 🌏 Travel Assistant Chatbot

## 🔹 Project Overview
The **Travel Assistant Chatbot** is a conversational AI web application built with **Streamlit**, **FastAPI**, and **Google Gemini LLM**.  
It provides users with travel-related information, answers general queries, and offers empathetic, context-aware responses.  
The system includes both a **frontend UI** and a **backend API** for seamless interaction.

---

## 🔹 Features
- Interactive chatbot interface built with **Streamlit**
- Backend API powered by **FastAPI**
- AI-generated responses using **Google Gemini LLM**
- Session-based chat history
- Empathetic and context-aware answers
- Customizable conversation flow with LangGraph

---

## 🔹 Technologies Used
- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **AI Model:** Google Gemini  
- **Conversation Flow:** LangGraph  
- **Language:** Python  
- **Environment:** `.env` configuration file  

---

## 🔹 How to Run Locally

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Saraswathi-Kalirajan/travel-chatbot.git
   cd travel-chatbot
   ```

2. **Create a Virtual Environment (recommended):**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**
   Create a `.env` file in the root directory and add:
   ```
   GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
   GOOGLE_MODEL=models/gemini-2.5-flash
   BACKEND_URL=http://localhost:8000
   ```

5. **Run the Backend (FastAPI):**
   ```bash
   python -m uvicorn backend:app --reload --port 8000
   ```

6. **Run the Frontend (Streamlit):**
   ```bash
   python -m streamlit run frontend.py
   ```

7. **Open in Browser:**
   Go to [http://localhost:8501](http://localhost:8501) to chat with your Travel Assistant!

---

## 🔹 Project Structure

```
travel-chatbot/
│
├── backend.py         # FastAPI backend (handles chat requests)
├── frontend.py        # Streamlit UI for chatbot interaction
├── listmodels.py      # Lists available Gemini models
├── run_all.bat        # (Optional) Script to start backend & frontend
├── requirements.txt   # Project dependencies
├── .env               # Environment variables (not shared publicly)
└── README.md          # Project documentation
```

---

## 🔹 Future Improvements

- Add user authentication and personalized travel recommendations
- Show destination images or maps via APIs
- Integrate real-time weather or currency conversion APIs
- Deploy the chatbot online using **Render**, **Vercel**, or **Google Cloud**

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
