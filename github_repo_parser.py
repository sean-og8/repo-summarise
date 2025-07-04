# Authentication is defined via github.Auth
from github import Auth
from github import Github
import datetime

from access_token import pat_token


def authorise_github_login():
    # authorise using an access token
    auth = Auth.Token(pat_token)
    g = Github(auth=auth)
    g.get_user().login
    print(g.get_users())
    return g


def get_repo_meta_data(g, repo, repo_owner, repo_name):
    repo_metadata = {}
    commits = repo.get_commits()
    commit_dates = [commit.commit.author.date for commit in commits]
    repo_metadata["Repository"] = repo_name
    repo_metadata["Owner"] = repo_owner
    repo_metadata["Collaborators"] = ", ".join([user.login for user in repo.get_collaborators()])
    repo_metadata["Langauges"] = list(repo.get_languages().keys())
    repo_metadata["Last commit date"] = commit_dates[0].strftime('%d/%m/%Y')
    return repo_metadata


def get_repo_content(repo_owner, repo_name):
    code_file_dict = {}
    repo_metadata = {}
    repo_structure = []
    g = authorise_github_login()
    repo = g.get_repo(repo_owner + "/" + repo_name)
    contents = repo.get_contents("")
    repo_metadata = get_repo_meta_data(g, repo, repo_owner, repo_name)
    while contents:
        file_object= contents.pop(0)
        if file_object.type == "dir":
            contents.extend(repo.get_contents(file_object.path))
        else:
            print(file_object)
            repo_structure.append(file_object)
            if file_object.name[-3:] in [".py", ".js" , "lte"]:
                decoded_content = file_object.decoded_content
                code_file_dict[file_object.name] = decoded_content
    print(repo_metadata)
    # To close connections after use
    g.close()
    return repo_structure, code_file_dict, repo_metadata


