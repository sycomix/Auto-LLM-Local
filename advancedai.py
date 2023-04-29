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

MODEL_PATH = os.environ["LLAMACPP_MODEL"]

llm = LlamaCpp(model_path=MODEL_PATH, temperature=0.5, n_ctx=4098)

tools = load_tools(["google-search","requests_all","wikipedia","human"], llm=llm)

print("Initializing agent...")
react = initialize_agent(tools, llm, n_batch=8, agent="zero-shot-react-description", verbose=True, return_intermediate_steps=True)

goal = os.environ["AI_GOAL"]
print("Goal: "+goal)

try:
    response = react({"input":goal})
except Exception as e:
    response = str(e)
    if response.startswith("Could not parse LLM output: `"):
        response = response.removeprefix("Could not parse LLM output: `").removesuffix("`")
        print("Corrected: "+response)

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
