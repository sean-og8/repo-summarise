# Authentication is defined via github.Auth
from github import Auth
from github import Github

from access_token import pat_token
# using an access token
auth = Auth.Token(pat_token)
g = Github(auth=auth)
g.get_user().login

print(g.get_users())

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)


# specifc repo, look at the contents
# repo_name = "auto-ml-pipeline"
# repo = g.get_repo("communitiesuk/auto-ml-pipeline")
# contents = repo.get_contents("")
# while contents:
#     file_content = contents.pop(0)
#     if file_content.type == "dir":
#         contents.extend(repo.get_contents(file_content.path))
#     else:
#         print(file_content)
#         print(file_content.decoded_content)

# 1. pass overall structure to llm 
# 2. if content file has py file, pass to llm as well 



def get_repo_content(repo_owner, repo_name):
    code_file_dict = {}
    repo_structure = []
    repo = g.get_repo(repo_owner + "/" + repo_name)
    contents = repo.get_contents("")
    while contents:
        file_object= contents.pop(0)
        if file_object.type == "dir":
            contents.extend(repo.get_contents(file_object.path))
        else:
            print(file_object)
            decoded_content = file_object.decoded_content
            repo_structure.append(file_object)
            print(file_object.name)
            print(file_object.name[-3:])
            if file_object.name[-3:] == ".py":
                code_file_dict[file_object.name] = decoded_content
    return repo_structure, code_file_dict

repo_structure, repo_code_dict = get_repo_content(repo_owner="communitiesuk", repo_name="auto-ml-pipeline")
print(repo_structure)
print(repo_code_dict.keys())
print(repo_code_dict)



# To close connections after use
g.close()