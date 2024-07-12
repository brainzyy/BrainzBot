import discord
from discord import bot
from dotenv import load_dotenv
from games.rps import rps
from games.coinflip import coinflip
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

@bot.command()
async def rps(ctx, *, choice: str):
    choice = choice.capitalize()  # Capitalize the first letter to match the options in the rps function
    valid_choices = ["Rock", "Paper", "Scissors"]
    
    if choice in valid_choices:
        result = rps(choice)  # Call your rps function with the user's choice
        await ctx.send(result)
    else:
        await ctx.send("Invalid choice. Please choose Rock, Paper, or Scissors.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$bye'):
        await message.channel.send('Goodbye!')  # Updated message for appropriateness

    if message.content.startswith('$hi'):
        await message.channel.send('Hello!')

    if message.content.startswith('$rps Rock'):
        await message.channel.send(rps("Rock"))

    if message.content.startswith('$rps Paper'):
    await message.channel.send(rps("Paper"))


    if message.content.startswith('$coinflip Tails'):
        await message.channel.send('Russian Roulet, You feeling lucky punk?')
        await message.channel.send(coinflip("Tails"))

client.run(token)