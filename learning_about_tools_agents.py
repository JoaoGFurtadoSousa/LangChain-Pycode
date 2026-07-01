from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_classic.agents import AgentExecutor
from langchain_core.tools import Tool
from langchain_core.prompts import PromptTemplate
from decouple import config


model = ChatGoogleGenerativeAI(model = "gemini-3.1-flash-lite",
                             api_key = config("GOOGLE_API_KEY"))


@Tool('calculadora', description= "Realiza operações matematicas",)
def calculadora(nums, tipo_operacao:str):
    match tipo_operacao:
        case '+':
            result = 0
            for num in nums:
                result += num
            return result

tools = [calculadora, ]


agent = create_agent(llm= model,
                     tools= tools)

agent_executor = AgentExecutor(
    agent = agent,
    tools = tools
)

prompt_template = PromptTemplate(
    template = '''Responda de forma amigavel esse calculo: {numeros}'''
)

prompt = prompt_template.format({
    'numeros':[1,2]
})

response = agent_executor.invoke(prompt)

print(response)

