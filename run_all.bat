start cmd /k "python -m uvicorn backend:app --reload --port 8000"
timeout /t 5
python -m streamlit run frontend.py
