from langchain_google_genai import GoogleGenerativeAI
from langchain_core.globals import set_llm_cache
from langchain_core.prompts import PromptTemplate
from langchain_community.cache import SQLiteCache
from decouple import config


set_llm_cache(SQLiteCache(database_path= 'django-questions.db'))

#question_user = input("Faça sua pergunta sobre Django:\n")

client = GoogleGenerativeAI(model="gemini-3.1-flash-lite",
                             api_key = config("GOOGLE_API_KEY"),
                             stream=True)


#template = "Exiba a diferença entre o framework {framework_1} e o framework {framework_2} para o codigo {codigo}" 

#prompt_template = PromptTemplate.from_template(template=template)

prompt = PromptTemplate.template("Exiba a diferença entre o framework {framework_1} e o framework {framework_2} para o codigo {codigo}")

# messages = [
#     {"role": "system", "content": "Você é um profissional em django e django rest framework"},
#     {"role": "user", "content": f"{question_user}"}
# ]

response = client.invoke()
print(response)