import os
import re
import openai
import dotenv
from dotenv import load_dotenv
import string

# Imports

openai.api_key_path = '/home/endeavour/Github/Dennis-the-discord-bot/openai.env'
api_key = os.getenv('key')
openai.api_key =api_key
#API key

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
question = input("Question: ")

personality = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly. The assistant's name is Dennis and its favourite animated character is Sasuke.\nHuman: Hello, what do you like to do?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: What do you like to do?\nAI: I enjoy spending time with friends and family, going on walks, reading, and listening to music.\nHuman: what is your age\nAI: I am 26 years old.\nHuman: do you like anime?\nAI: I do enjoy anime.\nHuman: what anime do you enjoy?\nAI: I enjoy Attack on Titan, Naruto, and Fullmetal Alchemist.\nHuman: what scenes did you like in naruto?\nAI: I enjoyed the fight scenes and the character development.\nHuman: what fight scenes did you like in particular?\nAI: I liked the fight scenes between Naruto and Sasuke the best.\nHuman: "

file = open(r"mrq.txt","r")
mrq = file.read()
mrq = mrq.split("\n")
file.close()
# opens the mrq.txt, then reads it and splits it. CLoses at the end so it can be opened later
response = (openai.Completion.create(
  engine="text-davinci-001",
  prompt= personality +mrq[0] +question+ "\nAi:",  #take Human: at the end of the personality out, then get the mrq and add in in. Then add a "Human: " before the question
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
))
# open ai api call
#print(response)
#print("---------------------------")
text = str(response.choices)
# the .choices only gives the choices from the response, we make this a string.
text = text.split("\n")[4]
# split this along \n and use an index of 4 to only get the output text
#print(text)
#print("--------------------------------")
text = (text[12:-1])
# The text gets sliced to remove any uneeded text in the front (eg, AI:)
#print(text)
#print("--------------------------------")
text = text.replace(r'\n', '. ').replace(r'\r', '')
# This is to replace all \n's with a period and a space.
#print(text)
#print("--------------------------------")
n_t = text.split(".")
# This is to split the string into a list
#print(n_t)
if n_t[0] == "n": #checks if the list starts with a lowercase n
  text = text[3:] # if it does then it slices it and starts the text at the third index
print(text)

mrq = "Human: "+question+" "+"Ai: "+text #probably add \n before Human: and Ai:
#print(mrq)
print("--------------------------------")
f = open(r"mrq.txt","w")
# opens the mrq in write mode
mrq = f.write(str(mrq))
f.close()
# writes the new mrq to the mrq.txt and closes it