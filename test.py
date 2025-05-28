import ollama
from ollama import chat
from pydantic import BaseModel

from github_repo_parser import get_repo_content

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the input prompt
model = "gemma3:12b"  # Replace model name
model_settings = {"temperature": 0.1, "top_k": 64, "top_p": 0.95}
model_settings = {}

# now need to pull in contents and pass to llm with a prompt, ask to summarise
# then can use ollama to structure the llm output into a json
# convert json to table and save
repo_structure, repo_code_dict = get_repo_content(repo_owner="communitiesuk", repo_name="auto-ml-pipeline")

prompt = f"Please examine the following code repository and explain what it does and how it works. Do not suggest ways the code could be improved. Here a list of files in the repo with the file paths: {repo_structure}, here is a dictionary of each of the code files and the corresponding code{repo_code_dict}"

response = client.generate(model=model, prompt=prompt, options=model_settings)

# Print the response from the model
print("Response from model:")
print(response.response)

print("now using structured output")

prompt = f"Here a list of files in the repo with the file paths: {repo_structure}, here is a dictionary of each of the code files and the corresponding code {repo_code_dict}. Tell me about this repository"

class SummaryTable(BaseModel):
  repo_summary: str
  file_list: list[str]
  programming_languages: list[str]
  how_it_works: str


response = chat(
  messages=[
    {
      'role': 'user',
      'content': prompt,
    }
  ],
  model=model,
  format=SummaryTable.model_json_schema(),
)

summary = SummaryTable.model_validate_json(response.message.content)
print(summary)



repo_structure, repo_code_dict = get_repo_content(repo_owner="sean-og8", repo_name="sudoku_solver")

prompt = f"Please examine the following code repository and explain what it does and how it works. Do not suggest ways the code could be improved. Reference specific files and functions in your response. Here a list of files in the repo with the file paths: {repo_structure}, here is a dictionary of each of the python files and the code{repo_code_dict}"

response = client.generate(model=model, prompt=prompt, options=model_settings)

# Print the response from the model
print("Response from model:")
print(response.response)

print("now structured output:")

prompt = f"Here a list of files in the repo with the file paths: {repo_structure}, here is a dictionary of each of the code files and the corresponding code {repo_code_dict}. Tell me about this repository"

class SummaryTable(BaseModel):
  repo_summary: str
  file_list: list[str]
  programming_languages: list[str]
  how_it_works: str


response = chat(
  messages=[
    {
      'role': 'user',
      'content': prompt,
    }
  ],
  model=model,
  format=SummaryTable.model_json_schema(),
)

summary = SummaryTable.model_validate_json(response.message.content)
print(summary)

bug

# make dummy output table, json to csv? json to html table?

repo_structure, repo_code_dict = get_repo_content(repo_owner="sean-og8", repo_name="inat-amls2-project")

prompt = f"Please examine the following code repository and explain what it does and how it works. Do not suggest ways the code could be improved. Reference specific files and functions in your response. Here a list of files in the repo with the file paths: {repo_structure}, here is a dictionary of each of the python files and the code{repo_code_dict}"

response = client.generate(model=model, prompt=prompt, options=model_settings)

# Print the response from the model
print("Response from model:")
print(response.response)

repo_structure, repo_code_dict = get_repo_content(repo_owner="sean-og8", repo_name="repo-summarise")

prompt = f"Please examine the following code repository and explain what it does and how it works. Do not suggest ways the code could be improved. Reference specific files and functions in your response. Here a list of files in the repo with the file paths: {repo_structure}, here is a dictionary of each of the python files and the code{repo_code_dict}"

response = client.generate(model=model, prompt=prompt, options=model_settings)

# Print the response from the model
print("Response from model:")
print(response.response)

# repo 2
#repo_structure, repo_code_dict = get_repo_content(repo_owner="communitiesuk", repo_name="scrolly-data-story-template", options=model_settings)

#prompt = f"Please examine the following code repository and explain what it does and how it works. Do not suggest ways the code could be improved. Reference specific files and functions in your response. Here a list of files in the repo with the file paths: {repo_structure}, here is a dictionary of each of the python files and the code{repo_code_dict}"

#response = client.generate(model=model, prompt=prompt)

## Print the response from the model
#print("Response from model:")
#print(response.response)

