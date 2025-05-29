import ollama
from ollama import chat
from pydantic import BaseModel, Field
import pandas as pd
import plotly.graph_objects as go
import json

from github_repo_parser import get_repo_content

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the input prompt
model = "gemma3:12b"  # Replace model name
model_settings = {"temperature": 0.4, "top_k": 64, "top_p": 0.95}


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
        print("converting to df")
        print(data)
        # Convert the JSON data to a Pandas DataFrame
        df = data

        # Create a Plotly HTML table
        print("creating go table")
        fig = go.Figure(data=[go.Table(
        columnwidth=[100, 100, 120, 100, 100, 180, 180, 180],
        header=dict(
            values=[f'<b>{col}</b>' for col in df.columns],
            font=dict(size=12),
            fill_color='navy',
            align='left',
            font_color='white'
        ),
        cells=dict(
            values=[df[col] for col in df.columns],
            fill_color='white',
            align='left',
            font_color='black'
            )
        )])

        # Save the Plotly table to an HTML file
        fig.write_html(output_filename)
        print(f"Plotly HTML table saved to: {output_filename}")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return


class SummaryTable(BaseModel):
  repository_summary: str = Field(alias="Brief summary of the purpose of the repository, use no more than 2 sentences")
  how_it_works: str = Field(alias="Brief description of how the repository works, use no more than 2 sentences")
  main_topics: list[str] = Field(alias='Describe the top 3 topics/techniques in single words, do not use full sentences')
  class Config:
      populate_by_name = True

repos = {
        # "auto-ml-pipeline": "communitiesuk",
        # "Mobility_data_prototypes": "communitiesuk",
        # "scrolly-data-story-template": "communitiesuk",
        "repo-summarise": "sean-og8",
        "inat-amls2-project": "sean-og8",
        "sudoku_solver": "sean-og8",
        }

combined_df = pd.DataFrame()

for repo_name in repos.keys():
    repo_owner = repos[repo_name]
    print(repo_owner, repo_name)
    repo_structure, repo_code_dict, repo_data = get_repo_content(repo_owner=repo_owner, repo_name=repo_name)
    prompt = f"Here a list of files in the repo with the file paths: {repo_structure}, here is a dictionary of each of the code files and the corresponding code {repo_code_dict}. Tell me about this repository"
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
    table = response.message.content
    repo_data.update(json.loads(table))
    print("updating table")

    df = pd.DataFrame([repo_data])

    combined_df = pd.concat([df, combined_df], axis=0)
    print(combined_df)
    print(type(combined_df))


def format_list_columns(row):
    # conver list to string
    row = ', '.join(row)
    return row

# tidy list vars
combined_df["Describe the top 3 topics/techniques in single words, do not use full sentences"] = combined_df["Describe the top 3 topics/techniques in single words, do not use full sentences"].apply(format_list_columns)
combined_df["Langauges"] = combined_df["Langauges"].apply(format_list_columns)

# tidy col names
rename_map = {
    "Describe the top 3 topics/techniques in single words, do not use full sentences": "Topics",
    "Brief description of how the repository works, use no more than 2 sentences": "Method",
    "Brief summary of the purpose of the repository, use no more than 2 sentences": "Summary"
}

combined_df.rename(columns=rename_map, inplace=True)


json_to_plotly_table(json_data=combined_df, output_filename="output_table.html")
