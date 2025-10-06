# listmodels.py
import os
try:
    # Some installs expose as: from google import genai
    from google import genai as genai_client  # preferred if present
    client = genai_client.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    models = client.models.list()
    for m in models:
        print(m.name, "-", getattr(m, "supported_generation_methods", "n/a"))
except Exception:
    try:
        import google.generativeai as genai
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        # different SDK, try listing via introspection (may not be supported)
        print("google.generativeai available; listing via example request - requesting a small completion to verify connection.")
        resp = genai.chat.completions.create(model=os.getenv("GOOGLE_MODEL", "models/chat-bison-001"),
                                             messages=[{"role":"user","content":[{"type":"text","text":"hello model list test"}]}])
        print("Response OK — SDK works. Sample response:")
        print(resp)
    except Exception as e:
        print("Could not list models. SDK not installed or GOOGLE_API_KEY missing/invalid.")
        print("Error:", e)

# from google import genai

# # Replace with your Gemini API key
# client = genai.Client(api_key="AIzaSyBhmTIU_29JlUYrPDavsa2L5U_tvKgRlw0")

# # List all models
# models = client.models.list()
# for model in models:
#     print(model.name)

