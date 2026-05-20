from langchain_google_genai import GoogleGenerativeAI, Gemini
from langchain_core.globals import set_llm_cache
from langchain_community.cache import SQLiteCache
from decouple import config


set_llm_cache(SQLiteCache(database_path= 'django-questions.db'))

question_user = input("Faça sua pergunta sobre Django:\n")

client = GoogleGenerativeAI(model="gemini-3.1-flash-lite",
                             api_key = config("GOOGLE_API_KEY"))


messages = [
    {"role": "system", "content": "Você é um profissional em django e django rest framework"},
    {"role": "system", "content": "Responda somente perguntas relacionadas ao Framework Django"},
    {"role": "user", "content": f"{question_user}"}
]

response = client.invoke(messages)

print(response)