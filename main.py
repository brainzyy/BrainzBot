import discord
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve the token
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$bye'):
        await message.channel.send('Goodbye!')  # Updated message for appropriateness

    if message.content.startswith('$hi'):
        await message.channel.send('Hello!')

client.run(token)