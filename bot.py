import os
import random
from urllib import response
import discord
from discord.ext import commands
from dotenv import load_dotenv
import openai
# 1


load_dotenv()
# imports os, discord and .env
secret = os.getenv('auth')
TOKEN = secret

# fetches the token from the .env
# 2

bot = commands.Bot(command_prefix=['Dennis ', 'dennis ','!'])
# bot prefix
@bot.event
async def on_ready():
    # this is executed when the bot is ready to run
    print(f'{bot.user.name} has connected to Discord!')



@bot.command(name='ping') #ping pong
async def pong(ctx):
    response = "Pong"
    print("trying rn")
    await ctx.send(response)


personality = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly. The assistant's name is Dennis and its favourite animated character is Sasuke.\nHuman: Hello, what do you like to do?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: What do you like to do?\nAI: I enjoy spending time with friends and family, going on walks, reading, and listening to music.\nHuman: what is your age\nAI: I am 26 years old.\nHuman: do you like anime?\nAI: I do enjoy anime.\nHuman: what anime do you enjoy?\nAI: I enjoy Attack on Titan, Naruto, and Fullmetal Alchemist.\nHuman: what scenes did you like in naruto?\nAI: I enjoyed the fight scenes and the character development.\nHuman: what fight scenes did you like in particular?\nAI: I liked the fight scenes between Naruto and Sasuke the best.\nHuman: "

@bot.event
async def on_message(msg):
    print(msg.content)
    if '!chat' in msg.content:
        print('---chat---')
        openai.api_key_path = 'openai.env'
        api_key = os.getenv('key')
        openai.api_key =api_key
        #api key
        question = msg.content
        start_sequence = "\nAI:"
        restart_sequence = "\nHuman: "
        #start and end sequences
        file = open(r"mrq.txt","r")
        mrq = file.read()
        mrq = mrq.split("\n")
        file.close()
        # Opens the mrq.txt in read mode and reads it to allow the bot to access the text in there.
        question = question[6:]
        response = (openai.Completion.create(
            engine="text-curie-001",
            prompt= personality + mrq[0] + question + "\nAi:",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        ))
        # api call
        text = str(response.choices)
        # the .choices only gives the choices from the response, we make this a string.
        text = text.split("\n")[4]
        # split this along \n and use an index of 4 to only get the output text
        text = (text[12:-1])
        # The text gets sliced to remove any uneeded text in the front (eg, AI:)
        text = text.replace(r'\n', '. ').replace(r'\r', '')
        # This is to replace all \n's with a period and a space.
        n_t = text.split(".")
        # This is to split the string into a list
        if n_t[0] == "n": #checks if the list starts with a lowercase n
            text = text[3:] # if it does then it slices it and starts the text at the third index
        await msg.channel.send(text)
        
        mrq = "Human: "+question+" "+"Ai: "+text #probably add \n before Human: and Ai:
        f = open(r"mrq.txt","w")
        mrq = f.write(str(mrq))
        f.close()
        #opens the mrq.txt in write mode and writes the mrq to it.
    elif '!clear' in msg.content:
        file = open(r"mrq.txt","w+")
        mrq = file.write("")
        file.close()
        print("---clear---")
        await msg.channel.send("Cleared")
    elif '!ping' in msg.content:
        response = "Pong"
        print("---ping---")
        await msg.channel.send(response)

@bot.command(name='clear')
async def clear(ctx):
  file = open(r"mrq.txt","w+")
  mrq = file.write("")
  file.close()
  await ctx.send("Cleared")

bot.run(TOKEN)
# runs the bot with the token