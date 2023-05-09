```diff
+ NO OPEN API / HUGGINGFACE - ONLY LOCAL GGML MODELS
! WILL BE COMBINGING THIS WITH MY MODULAR AI-TOOLS TO GIVE ACCESS TO AN UNLIMITED NUMBER OF TOOLS
```

# Auto-LLM-Local
Created my own python script similar to AutoGPT where you supply a local llm model like alpaca13b (The main one I use), and the script can access the supplied tools to achieve your objective.

Code fully works as expected in my testing. Takes me 5 minutes per chain on my slow laptop.

# Features:
	Langchain Integration
	Llamacpp Model Support
  
# Tools:
    GoogleSearchAPIWrapper
    Requests
    Wikipedia
    Human
    
# TODO:
	<b>DONE-</b>Create requirements.txt
	<b>DONE-</b>Create ENV variables
	<b>DONE-</b>Create setup and usage documentation
    <b>TESTING-</b>Add memory
	Add more tools (Have some custom ideas)
	
# SETUP / USAGE
	!choco install make
	Install https://visualstudio.microsoft.com/vs/ with C++
	!pip install -r requirements.txt
	Place alpaca13b model in /models/alpaca13b folder and rename to model.bin
	Copy .env.example to .env and edit
		Change GOOGLE_CSE_ID and GOOGLE_API_KEY to your google search api information
		Change LLAMACPP_MODEL to the name of the model folder in the models directory (ex. alpaca13b)
		Change AI_GOAL to the task you want the AI to achieve (ex. Help the human overcome a mental health struggle.)
		Run


# P.S. New to python and github, just trying to do my part as I see a lot of people are asking how to do AutoGPT locally without any OpenAPI support.
