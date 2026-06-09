from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from decouple import config

def route_chain():
    model = ChatGoogleGenerativeAI(model ='gemini-3.1-flash-lite',
                                   api_key=config('GOOGLE_API_KEY'))
    prompt_template = PromptTemplate.from_template(
        'Você é um roteador para decidir qual chain deverá ser executada. As chains são:' \
        'Tecnologia da Informacao' \
        'Jogos' \
        'Outros' \
        'Voce so poderá responder alguma dessas opções de acordo com a entrada do usuario. Responda somente qual é o nicho.' \
        'Pergunta usuario: {question_user}'
    )
    chain = (prompt_template | model | StrOutputParser())
    response = chain.invoke({
        "question_user": "Me fale sobre a linguagem python"
    })
    print(response)
    return response

route_chain()