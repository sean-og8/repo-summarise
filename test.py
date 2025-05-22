import ollama

from github_test import get_repo_content

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the input prompt
model = "gemma3:12b"  # Replace model name
prompt = "What is Python?"

# Send the query to the model
response = client.generate(model=model, prompt=prompt)

# Print the response from the model
print("Response from Ollama:")
print(response.response)

# now need to pull in contents and pass to llm with a prompt, ask to summarise
# then can use ollama to structure the llm output into a json
# convert json to table and save
repo_structure, repo_code_dict = get_repo_content(repo_owner="communitiesuk", repo_name="auto-ml-pipeline")

prompt = f"Please examine the following code repository and explain what it does and how it works. Reference specific files and functions in your response. Here a list of files in the repo with the file paths: {repo_structure}, here is a dictionary of each of the python files and the code{repo_code_dict}"
response = client.generate(model=model, prompt=prompt)

# Print the response from the model
print("Response from model:")
print(response.response)
