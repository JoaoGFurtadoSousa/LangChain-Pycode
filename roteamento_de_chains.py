from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from decouple import config

def ai_model_instance():
     model = ChatGoogleGenerativeAI(model ='gemini-3.1-flash-lite',
                                   api_key=config('GOOGLE_API_KEY'))
     return model

def route_chain():
    model = ai_model_instance()
    question_user = input("Realize sua pergunta: ")
    prompt_template = PromptTemplate.from_template(
        'Você é um roteador para decidir qual chain deverá ser executada. As chains são:' \
        'Tecnologia da Informacao' \
        'Jogos de Videogames' \
        'Outros' \
        'Voce so poderá responder alguma dessas opções de acordo com a entrada do usuario. Responda somente qual é o nicho.' \
        'Pergunta usuario: {question_user}'
    )
    chain = (prompt_template | model | StrOutputParser())
    response = chain.invoke({
        "question_user": question_user
    })
    print(response)
    return response, question_user

def chain_games(question_user:str):
    model = ai_model_instance()
    prompt_template = PromptTemplate.from_template(
        'Voce é um especialista em Jogos de VideoGames. Com a entrada do usuario, fale com detalhes e emoção sobre a questão perguntada do usuario.' \
        'Sempre fale que é o Davy Jones 2.0' \
        'Questão usuario: {question_user}'
    )
    chain = prompt_template | model | StrOutputParser()
    response = chain.invoke({"question_user": question_user})
    return response


def chain_ti(question_user:str):
    model = ai_model_instance()
    prompt_template = PromptTemplate.from_template(
        'Voce é um especialista em Tecnologia da Informação. Com a entrada do usuario, fale com detalhes tecnicos sobre a pergunta do usuario.' \
        'Sempre fale no começo da frase que é o Bill Gates 2.0' \
        'Questão usuario: {question_user}'
    )
    chain = prompt_template | model | StrOutputParser()
    response = chain.invoke({"question_user": question_user})
    return response

def chain_others_topics(question_user:str):
    model = ai_model_instance()
    prompt_template = PromptTemplate.from_template(
        'Com a entrada do usuario, fale com detalhes e propriedades sobre a pergunta do usuario.' \
        'Fale sobre o que é, o que faz e me de o maximo de detalhes possiveis.' \
        'Sempre fale que é o Google 2.0' \
        'Questão usuario: {question_user}'
    )
    chain = prompt_template | model | StrOutputParser()
    response = chain.invoke({"question_user": question_user})
    return response


def switch_chain_for_question_user():
    response, question_user = route_chain()
    response = response
    if response == "Jogos de Videogames":
        response = chain_games(question_user)
        print(response)
    elif response == "Tecnologia da Informacao":
        response = chain_ti(question_user)
        print(response)
    else:
        chain_others_topics(question_user)
    

switch_chain_for_question_user()