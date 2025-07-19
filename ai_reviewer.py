import google.generativeai as genai
from config import GEMINI_API_KEY
genai.configure(api_key=GEMINI_API_KEY)
model=genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
def review_text(spun_text):
    prompt=f"Edit this text to improve clarity, grammar, and flow:\n\n{spun_text}"
    response=model.generate_content([{"role": "user","parts": [prompt]}])
    return response.text