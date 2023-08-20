#to acess environment variables
import os

#access openai methods
import openai

#load environment variables from .env
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def explanation(topic):
    response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role" : "user", "content" : f"Explain to me, in a broad scope, what {topic} is about."}
    ])
    print("\n", "ChatGPT: " , response.choices[0].message.content)

    question = input("Would you like more information about the topic? Y/N: ")
    if question == "y" or question == "Y":
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role" : "user", "content" : f"Explain to me, in detail, what {topic} is about."}
                ])
        print("\n" , "ChatGPT: " , response.choices[0].message.content)
    else:
        print("Have a nice day!")    
