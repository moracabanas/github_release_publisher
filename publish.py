import requests
import json

# Easy
token = "your_github_token"

userName = "your_github_user"
repo = "your_repo_name"
version = "0.1.0-alpha" # http://semver.org/

# Advanced
url = f"https://api.github.com/repos/{userName}/{repo}/releases"

headers = {
    "User-Agent": f"{repo}/{version}", # https://developer.github.com/v3/#user-agent-required
    "Authorization": f"token {token}"
}

with open("release.md", "r", encoding="utf-8") as release_file:
    release_content = release_file.read() # This maps release.md file content to POST payload "body"

payload = { #you can configure this parameters
    "tag_name": f"v{version}",
    "target_commitish": "master",
    "name": f"Version {version}",
    "body": f"{release_content}",
    "draft": True,
    "prerelease": True,
}


r = requests.post(url, data=json.dumps(payload), headers=headers)

status = r.status_code
response = json.dumps(r.json(), indent=4)

print(f'\n status: {status} \n')
# print(f'response: \n {response}')
print(f'You can review your release on: {r.json()["html_url"]}') if status == 201 else None


# https://stackoverflow.com/questions/45240336/how-to-use-github-release-api-to-make-a-release-without-source-code
# https://requests.readthedocs.io/en/master/user/quickstart/#custom-headers
# https://developer.github.com/v3/repos/releases/#create-a-release