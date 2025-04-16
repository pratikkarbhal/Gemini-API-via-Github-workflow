import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

with open("prompt.txt", "r") as file:
    prompt = file.read()

model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")  # Replace with the one from your list

response = model.generate_content(prompt)
print(response.text)
