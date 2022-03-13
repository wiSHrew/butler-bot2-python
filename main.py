import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()

swearwords = [
  "yawa",
  "piste",
  "animal",
  "putang ina",
  "putang ina mo",
  "fuck you",
  "shit",
  "pakshet",
  "bwisit",
  "leche",
  "hayop",
  "gago",
  "yawa ka piste kang animala ka putang ina mong leche ka gago hayop ka",
  "tite",
  "puke",
  "puta"
]

def get_qoute():
  response = requests.get

def update_swearwords(new_swearwords):
  if "swearwords" in db.keys():
    swearwords = db["swearwords"]
    swearwords.appen(new_swearwords)
    db["swearwords"] = swearwords
  else:
    db["swearwords"] = [new_swearwords]

def delete_swearwords(index):
  swearwords = db["swearwords"]
  if len(swearwords) > index:
    del encouragements[index]
  db["swearwords"] = swearwords

@client.event
async def on_ready():
    print('{0.user} is ready to yawa'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('~hello'):
    await message.channel.send('saman yawa')

  options = swearwords
  if "swearwords" in db.keys():
    options = options + db["swearwords"]
    
  if msg.startswith('~teachme'):
    await message.channel.send('ok class repeat after me: ' + random.choice(choice))

  if msg.startswith("~tudluantika"):
    new_swearwords = msg.split("~tudluantika ",1)[1]
    update_swearwords(swearwords)
    await message.channel.send('puta mas yawa pa mn ka nako bai, murag wa najud kay chance muadtog langit ba')

    if msg.startswith("~~delete"):
      swearwords = []
      if "swearwords" in db.keys():
        index = int(msg.split("~~delete ", 1)[1])
        delete_swearwords(index)
        encouragements = db["swearwords"]
      await message.channel.send(swearwords)

client.run(os.getenv('token'))