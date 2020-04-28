import argparse
import json
import requests
import base64
import os
import sys

# TODO: ADD YOUR OAUTH TOKEN HERE
oauth_token = "Add your token here"

# Grab repo name from command line, will raise if not present
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--repo", help="Repo name in format of user/name-of-repo", required=True)
repo = parser.parse_args().repo

# Get Notebook from GitHub API
headers = {"Authorization": f"token {oauth_token}"}
response = requests.get(f"http://api.github.com/repos/{repo}/contents/index.ipynb?ref=master", headers=headers)

if response.status_code == 200:
    encoded_content = json.loads(response.content)['content']
    notebook = json.loads(base64.b64decode(encoded_content))
else:
    print(f"{response.content}\n")
    sys.exit()

# Write to index.ipynb file
f = open("index.ipynb", "w")
f.write(json.dumps(notebook))
f.close()

# Runs the tests
os.system("pytest")
