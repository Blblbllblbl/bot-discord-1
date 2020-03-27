import discord
import asyncio
from token import JSP
ws_url = 'ws://Guesser-Cluster.scoder12.repl.co'
guess_url = 'https://guess-it.scoder12.repl.co/guess'
client = discord.Client()

@client.event
async def on_ready():
  print("voilà")

@client.event
async def on_message(message):
  if message.content == "!hello":
    await message.channel.send("bonjour humain!")
  if message.content == "!oe":
    await message.channel.send("On ne parle pas ici!")


client.run(JSP)
