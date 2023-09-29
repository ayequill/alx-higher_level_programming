#!/usr/bin/python3
""" Gets all commits for a specific repository """
if '__name__' == '__main__':
    from sys import argv
    from requests import get

    repo, user = argv[1], argv[2]

    response = get(f"https://api.github.com/repos/{user}/{repo}/commits")
    if response.status_code == 200:
        data = response.json()
        for commit in data[:10]:
            author = commit.get('commit').get('author').get('name')
            print(f"{commit.get('sha')}: {author}")
