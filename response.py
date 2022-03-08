# import requests
# import http


# url='http://1be7-103-127-167-202.ngrok.io/webhooks/rest/webhook'

# data = {
#     'sender': 1,
#     'message' : 'hi'
# }

# result=requests.post(url=url, json=data)
# print(result.text)
import requests

url = "http://127.0.0.1:5005/webhooks/rest/webhook"

payload = " {\r\n    \"sender\": 1,\r\n    \"message\" : \"hi\"\r\n}\r\n"
headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)