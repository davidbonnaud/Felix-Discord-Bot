import discord
import os
import datetime
from datetime import datetime, date
from keep_alive import keep_alive

client = discord.Client()

def timeSince():
  lastSeen = datetime(2021, 1, 9)
  currentDay = datetime.today()
  diff = currentDay - lastSeen
  return diff.days

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.get_channel(805594931627950081).send(timeSince())

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('felix'):
    await message.channel.send('Who?')

  if message.content.startswith('$felix'):
    await message.channel.send(timeSince())


keep_alive()
client.run(os.getenv('TOKEN'))