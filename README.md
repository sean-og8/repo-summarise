# repo-summarise

## Getting started
* This project uses ollama to run LLMs locally, please see the ollama [github](https://github.com/ollama/ollama) page for operating system specific installation instructions.
* You need to provide a Github Personal Access Token (PAT) for authentication when downloading repositories. To generate a PAT on the Github website, go to settings -> developer settings (right at the bottom on the left hand side).
* Take the generated PAT and place it in a file called access_token.py. The correct syntax to use is ```pat_token = 'YOUR_TOKEN'```

## Resources 

* ollama tools - use to trawl through git repos using github python lib: https://ollama.com/blog/functions-as-tools
* github python lib - use to allow llm to efficiently get repo info:
* ollama structured outputs - structure llm outputs in table: https://ollama.com/blog/structured-outputs
* uv cookie cutter project template: https://github.com/communitiesuk/python-cookiecutter-uv/blob/main/docs/unix.md
