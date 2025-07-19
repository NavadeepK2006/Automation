import google.generativeai as genai
from config import GEMINI_API_KEY
genai.configure(api_key=GEMINI_API_KEY)
model=genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
def spin_content(raw_text):
    prompt=f"Rewrite this chapter in a more modern, engaging style:\n\n{raw_text}"
    response=model.generate_content([{"role": "user","parts": [prompt]}])
    return response.text