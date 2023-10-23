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
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory, ConversationTokenBufferMemory, ConversationSummaryBufferMemory

MODEL_PATH = os.environ["LLAMACPP_MODEL"]
TEMP = os.environ["TEMP"]
NCTX = os.environ["N_CTX"]

llm = LlamaCpp(
    model_path=f"models/{MODEL_PATH}/model.bin", temperature=TEMP, n_ctx=NCTX
)

#memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=4098) #Token Limit Memory
memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=4098) #Summary and Token Limit Memory
#memory = ConversationSummaryMemory(llm=llm) #Summary Memory
#memory = ConversationBufferMemory(memory_key="history") #Default Memory

#llm = LlamaCpp(model_path="models/"+MODEL_PATH, temperature=TEMP, n_ctx=NCTX)

tools = load_tools(["google-search","requests_all","wikipedia","human"], llm=llm)

print("Initializing agent...")
react = initialize_agent(tools, llm, memory=memory, n_batch=8, agent="zero-shot-react-description", verbose=True, return_intermediate_steps=True)

goal = os.environ["AI_GOAL"]
print(f"Goal: {goal}")

try:
    response = react({"input":goal})
except Exception as e:
    response = str(e)
    if response.startswith("Could not parse LLM output: `"):
        response = response.removeprefix("Could not parse LLM output: `").removesuffix("`")
        print(f"Corrected: {response}")

executionTime = (time.time() - startTime)
print(f'Execution time in seconds: {str(executionTime)}')
