import requests

response = requests.post(
    "http://127.0.0.1:8000/dreams/interpret/",
    json={"dream_description": "I had a dream I was hitting my tenant with a spade at the back of his head"},
    headers={"Content-Type": "application/json"}
)
print(response.json())