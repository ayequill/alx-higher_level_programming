#!/usr/bin/python3
""" Gets all commits for a specific repository """
from sys import argv
from requests import get

repo, user = argv[1], argv[2]
token = "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"
headers = {
    "Authorization": "Bearer " + token
}
response = get(f"https://api.github.com/repos/{user}/{repo}/commits")
if response.status_code == 200:
    data = response.json()
    for commit in data[:10]:
        author = commit.get('commit').get('author').get('name')
        print(f"{commit.get('sha')}: {author}")
