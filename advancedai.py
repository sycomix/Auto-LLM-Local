import time
startTime = time.time()
import os
import json
from langchain.utilities import BashProcess
from langchain import Wikipedia
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.agents import load_tools
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.llms import LlamaCpp

os.environ["GOOGLE_CSE_ID"] = "CSE_ID" #Put your google cse id
os.environ["GOOGLE_API_KEY"] = "API-KEY" #Put your google api key

MODEL_PATH = "alpaca13b.bin" #Put your model here

llm = LlamaCpp(model_path=MODEL_PATH, temperature=0.5, n_ctx=4098)

tools = load_tools(["google-search","requests_all","wikipedia","human"], llm=llm)

print("Initializing agent...")
react = initialize_agent(tools, llm, n_batch=8, agent="zero-shot-react-description", verbose=True, return_intermediate_steps=True)

question = "Who was the US president in 2020?"
print("Asking: "+question)

try:
    response = react({"input":question})
except Exception as e:
    response = str(e)
    if response.startswith("Could not parse LLM output: `"):
        response = response.removeprefix("Could not parse LLM output: `").removesuffix("`")
        print("Corrected: "+response)

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
