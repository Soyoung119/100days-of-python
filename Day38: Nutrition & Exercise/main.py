import requests
from datetime import datetime

USERNAME = "soyoung"
TOKEN = "abcdefg123"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url = graph_endpoint, headers = headers, json = graph_config)
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20",
}

# response = requests.post(url=pixel_creation_endpoint, headers=headers, json=pixel_data)
# print(response.text)

new_pixel_endpoint = f"{pixel_creation_endpoint}/20260807"

update_data = {
    "quantity": "50",
}

# response = requests.put(url = new_pixel_endpoint, headers = headers, json = update_data)
# print(response.text)

response = requests.delete(url=new_pixel_endpoint, headers=headers)
print(response.text)

