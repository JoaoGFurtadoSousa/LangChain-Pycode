from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain.agents.structured_output import ToolStrategy
from langchain_core.prompts import PromptTemplate
from decouple import config


model = ChatGoogleGenerativeAI(model = "gemini-3.1-flash-lite",
                             api_key = config("GOOGLE_API_KEY"))


@tool
def calculadora(nums:list[int], tipo_operacao:str):
    '''Realiza calculos matematicos de acordo com os valores inputados e tipo de operacao'''
    match tipo_operacao:
        case '+':
            result = 0
            for num in nums:
                result += num
            return result

tools = [calculadora, ]


agent = create_agent(model= model,
                    tools= tools)



prompt_template = PromptTemplate(
    input_variables=["numeros", "tipo_operacao"],
    template = '''Responda de forma amigavel esse calculo: {numeros} e {tipo_operacao}'''
)

prompt = prompt_template.format(
    numeros = [1, 2], 
    tipo_operacao = '+')

response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ]
})

print(response['structured_output'])

