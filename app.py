import os
from re import T
import openai
import dotenv
from dotenv import load_dotenv

# Imports

openai.api_key_path = '/home/endeavour/Github/Dennis-the-discord-bot/openai.env'
api_key = os.getenv('key')
openai.api_key =api_key
#API key

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

response = (openai.Completion.create(
  engine="text-davinci-001",
  prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, what do you like to do?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: \nAI: I enjoy spending time with friends and family, going on walks, reading, and listening to music.\nHuman: what is your age\nAI: I am 26 years old.\nHuman: do you like anime?\nAI: I do enjoy anime.\nHuman: what anime do you enjoy?\nAI: I enjoy Attack on Titan, Naruto, and Fullmetal Alchemist.\nHuman: what scenes did you like in naruto?\nAI: I enjoyed the fight scenes and the character development.\nHuman: what fight scenes did you like in particular?\nAI: I liked the fight scenes between Naruto and Sasuke the best.\nHuman: Who do you like more, naruto or sasuke?",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
))
text = str(response.choices)
text = text.split("\n")[4]
print(text)
