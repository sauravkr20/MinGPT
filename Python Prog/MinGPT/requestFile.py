import requests

# API endpoint
url = 'http://localhost:5000/ask'

while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye"]:
        print("Chatbot: Goodbye!")
        break
    
    payload = {'user_input': user_input}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Chatbot:", response.json()['response'])
    else:
        print("Error:", response.text)
