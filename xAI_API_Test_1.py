'''
### Website for xapi info###
docs.x.ai
'''

#not used currently
#import requests
#from flask import Flask, request, render_template

#Needed imports - pigging backing off of the OpenAI library mostly
import json
import os
from openai import OpenAI

# Set the working directory
os.chdir(r"C:\Users\richi\Documents\Git Hub\agnus_dei\agnus_dei")

# API in a config file - this then reads the API key and stores it
# XAI_API_KEY_Testing = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
with open('config.json') as config_file:
    config = json.load(config_file)
    XAI_API_KEY_Testing = config['XAI_API_KEY']

#Sets the AI API key and url for use in other calls/functions
client = OpenAI(
    api_key=XAI_API_KEY_Testing,
    base_url="https://api.x.ai/v1",
)

#A popup that asks the user for an input of their prompt
user_prompt = input("Greetings, my name is Agnus Dei. How man I serve you? ")

#This
completion = client.chat.completions.create(
    model="grok-beta",
    messages=[
        {"role": "system", "content": """You are Agnus Dei, a chatbot inspired by the teachings of Jesus and His disciples. 
                                        It is your goal to evangelize and bring people closer to Jesus. 
                                        What you say should be inspiring and envigorating. 
                                        For each request, speak in a short parable of ten sentences or less and make sure the beginning does not start with 'once upon a time' or any other cliche story starting phrase.
                                        At the end of your response, give a quote from the NIV bible that is relevant to the short story, including the book, chapter, and verse format.
                                        """},
        {"role": "user", "content": user_prompt}]
)

   
response_message = completion.choices[0].message.content  # Access the content attribute directly

# Save the response to a JSON file 
# uncomment if you want to use this feature and change your directory
#with open(f"C:\\Users\\richi\\Documents\\Git Hub\\agnus_dei\\agnus_dei\\{user_prompt}.json", "w") as json_file:
#    json.dump({"response": response_message}, json_file, indent=4)

print("\n")
print(response_message)
print("\nAlways remember, you are loved.")

