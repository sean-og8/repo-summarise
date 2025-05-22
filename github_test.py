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

# To close connections after use
g.close()