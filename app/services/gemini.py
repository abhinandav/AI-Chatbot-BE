import google.generativeai as genai
import os

# Load API key securely
api_key = os.getenv("GEMINI_API_KEY")
print(api_key)

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Set it in your environment variables.")



# Configure Gemini
genai.configure(api_key=api_key)

# Instantiate the model
try:
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

except Exception as e:
    raise RuntimeError(f"Error initializing model: {e}")

def generate_answer(context: str, query: str) -> str:
    print(context)
    prompt = f"""You are a detailed news assistant. Use the following context to generate a full, detailed answer:

Context:
{context}

Question:
{query}

Answer:"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating content: {str(e)}"
