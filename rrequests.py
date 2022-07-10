import requests

url = "https://api.green-api.com/waInstance{{idInstance}}/checkWhatsapp/{{apiTokenInstance}}"

payload = "{\r\n    \"phoneNumber\": 79001234567\r\n}"
headers = {
  'Content-Type': 'application/json'
}

print(payload)
# response = requests.request("POST", url, headers=headers, data = payload)

# print(response.text.encode('utf8'))