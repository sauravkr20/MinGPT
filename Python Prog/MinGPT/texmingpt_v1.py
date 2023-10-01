import openai
import json
import os
import sys
import constants

os.environ["OPENAI_API_KEY"] = constants.APIKEY

class Chatbot:
    def __init__(self, api_key, index):
        self.index = index
        openai.api_key = api_key
        self.chat_history = []

    def generate_response(self, user_input):
        prompt = "\n".join([f"{message['role']}: {message['content']}" for message in self.chat_history[-5:]])
        prompt += f"\nUser: {user_input}"
        response = self.index.query(user_input)

        message = {"role": "assistant", "content": response}
        self.chat_history.append({"role": "user", "content": user_input})
        self.chat_history.append(message)
        return message
    
    def load_chat_history(self, filename):
        try:
            with open(filename, 'r') as f:
                self.chat_history = json.load(f)
        except FileNotFoundError:
            pass

    def save_chat_history(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.chat_history, f)

from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator

loader = DirectoryLoader("./data")
index_creator = VectorstoreIndexCreator()
index = index_creator.from_loaders([loader])

bot = Chatbot("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", index=index)
bot.load_chat_history("chat_history.json")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye"]:
        print("TEXMiN: Goodbye!")
        bot.save_chat_history("chat_history.json")
        break
    response = bot.generate_response(user_input)
    print(f"TEXMiN: {response['content']}")
