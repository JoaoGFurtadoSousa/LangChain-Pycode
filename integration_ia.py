import os
from langchain_google_genai import GoogleGenerativeAI
from decouple import config

question_user = input("Faça sua pergunta sobre Django:\n")

client = GoogleGenerativeAI(model="gemini-3.1-flash-lite",
                             api_key = config("GOOGLE_API_KEY"))


messages = [
    {"role": "system", "content": "Você é um profissional em django e django rest framework"},
    {"role": "user", "content": f"{question_user}"}
]

response = client.invoke(messages)

print(response)