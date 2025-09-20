import google.generativeai as genai

def setup_gemini(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-1.5-pro")  # ✅ modelo atualizado

def get_response(model, prompt):
    response = model.generate_content(prompt)
    return response.text

