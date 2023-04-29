NO OPEN API / HUGGINGFACE - ONLY LOCAL GGML MODELS

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
    Add memory
	Add more tools (Have some custom ideas)
	
# SETUP / USAGE
	!pip install -r requirements.txt
	Place alpaca13b model in models folder
	Copy .env.example to .env and edit
		Change GOOGLE_CSE_ID and GOOGLE_API_KEY to your google search api information
		Change LLAMACPP_MODEL to the name of the model in the models directory (ex. alpaca13b.bin)
		Change AI_GOAL to the task you want the AI to achieve (ex. Help the human overcome a mental health struggle.)
		Run


# P.S. New to python and github, just trying to do my part as I see a lot of people are asking how to do AutoGPT locally without any OpenAPI support.
