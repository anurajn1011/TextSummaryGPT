#to acess environment variables
import os

#access openai methods
import openai
import json

#load environment variables from .env
from dotenv import load_dotenv

openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role" : "system", "content" : "You are a helpful AI!"},
        {"role" : "user", "content" : "Hello!"}
    ],
    streaming = True
)

print(completion.choices[0].messages)