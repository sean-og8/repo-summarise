import ollama
from ollama import chat
from pydantic import BaseModel
import pandas as pd
import plotly.graph_objects as go
import json

from github_repo_parser import get_repo_content

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the input prompt
model = "gemma3:12b"  # Replace model name
model_settings = {"temperature": 0.1, "top_k": 64, "top_p": 0.95}
model_settings = {}



repo_structure, repo_code_dict = get_repo_content(repo_owner="sean-og8", repo_name="sudoku_solver")

# prompt = f"Please examine the following code repository and explain what it does and how it works. Do not suggest ways the code could be improved. Reference specific files and functions in your response. Here a list of files in the repo with the file paths: {repo_structure}, here is a dictionary of each of the python files and the code{repo_code_dict}"

# response = client.generate(model=model, prompt=prompt, options=model_settings)

# # Print the response from the model
# print("Response from model:")
# print(response.response)

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
print(response.message.content)

table = response.message.content


def json_to_plotly_table(json_data, output_filename="plotly_table.html"):
    """
    Converts JSON data to a Pandas DataFrame and outputs it as a Plotly HTML 
table.

    Args:
        json_data (str or list or dict): The JSON data to convert.  Can be a 
JSON string, 
                                         a Python list, or a Python 
dictionary.
        output_filename (str): The name of the HTML file to save the Plotly 
table to.
                                 Defaults to "plotly_table.html".
    
    Returns:
        None.  Saves a Plotly HTML table to the specified file.  Prints an 
error message if 
                there's an issue parsing JSON.
    """

    try:
        # Load JSON data if it's a string
        if isinstance(json_data, str):
            data = json.loads(json_data)
        else:
            data = json_data  # Assume it's already a list or dictionary

        # Convert the JSON data to a Pandas DataFrame
        df = pd.DataFrame(data)

        # Create a Plotly HTML table

        fig = go.Figure(data=[go.Table(header=dict(values=df.columns), cells=dict(values=[df[col] for col in df.columns]))])
        
        # Save the Plotly table to an HTML file
        fig.write_html(output_filename)
        print(f"Plotly HTML table saved to: {output_filename}")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return

json_to_plotly_table(json_data=table, output_filename="test.html")
bug
# repo 2

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

