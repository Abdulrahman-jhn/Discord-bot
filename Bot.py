
import discord
import random
from discord import Member
from discord.ext import commands
import os

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.listen()
async def on_message(message, member: Member = None):  # when someone messages
    chk_idt_words = ["floppa", "yazeed", "potata"]
    rply_idt_words = ["is a Man", "LEEESSS GOOOOOOOOO", "BrUh Get a life"]
    if message.author == client.user:  # to avoid the bot using the calling it self
        return
    if message.channel.id == 884859072833282048:

      if any(word in message.content.lower() for word in chk_idt_words):
        await message.channel.send(random.choice(rply_idt_words))
        return

    if message.content.startswith('meme' or 'memes'):
      if message.channel.id == 884859072833282048:
        await message.channel.send('I am not the real yazeed please go to le-meemees or contact @yazeemdzee for more')
      
  
keep_alive()
client.run("Token")
