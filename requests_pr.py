#here we will practice on request library
import requests

#making a get request
r = requests.get('https://api.github.com/users/workingacc800-asad')

if r.status_code == 200:
    data = r.json()
    print("User Name: ",data.get("name"))
    print("Public Repos" , data.get("public_repos"))
else:
    print("Failed to fetch data:" , r.status_code)


url = "https://httpbin.org/post"
payload = {
    "agent_name": "ResearchBot",
    "status": "active"
}

# Sending JSON data using the `json` parameter
response = requests.post(url, json=payload)

print(response.status_code)  # 200
print(response.json())       # Displays echoed JSON payload