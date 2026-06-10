from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import create_agent
from decouple import config



db_connection = SQLDatabase.from_uri() # Realiza a conexão com o banco

model = ChatGoogleGenerativeAI(model= "gemini-3.1-flash-lite",
                             api_key = config("GOOGLE_API_KEY"))


tools_db = SQLDatabaseToolkit(
    db= db_connection,
    llm=model
)

agent = create_agent(
    model = model,
    tools= tools_db.get_tools(),
    system_prompt=("Você é especialista em banco de dados e precisa pegar e retornar a imagem da solicitação do usuario na tabela garagem_permanencia. Filtre pelos ultimos dois registros e retorne a foto de entrada")
)

# chain = agent | StrOutputParser()

response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Retorne os dois últimos registros"
        }
    ]
})

print(response["messages"][-1].content)