from langchain_tavily import TavilyExtract
from decouple import config


tool = TavilyExtract(tavily_api_key=config('TAVILY_API_KEY'))

response = tool.invoke({"urls" : ['https://www.adorocinema.com/filmes/filme-1000028234/']})

print(response)