from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from decouple import config


model = ChatGoogleGenerativeAI(model ="gemini-3.1-flash-lite",
                             api_key = config("GOOGLE_API_KEY"))

runnable_sequence = (PromptTemplate.from_template("Me fale as diferenças entre as linguagens: {linguagem_1} x {linguagem_2}") | model | StrOutputParser())

response = runnable_sequence.invoke({"linguagem_1": "Javascript", 
                        "linguagem_2":"Golang"})
print(response)