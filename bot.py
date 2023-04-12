import os
import discord
import openai
from discord.ext import commands
from dotenv import load_dotenv
from io import BytesIO
import requests

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
openai.api_key = os.getenv('OPENAI_TOKEN')

# Permission to bot
intents = discord.Intents.all() 
intents.members = True
intents.messages = True

# Create a bot object with a command prefix and the same intents
client = commands.Bot(command_prefix='/', intents=intents)

# This function is called when the bot successfully connects to Discord
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

#Ping!
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!\n{round(client.latency * 1000)}ms')

@client.event
async def on_message(message):
    if client.user in message.mentions:
        content = message.content.replace(client.user.mention, '').strip()
        if content.startswith('/img'):
            prompt = content[len('/img'):].strip()
            print("image generation...")
            response = openai.Image.create(prompt=prompt, n=1, size='1024x1024')
            image_url = response['data'][0]['url']
            print("converting...")
            # Get image bytes and create file-like object - too slow
            image_bytes = BytesIO(requests.get(image_url).content)
            image_file = discord.File(image_bytes, filename='image.png')
            await message.reply(file=image_file)
        elif content.startswith('/ai'):
            prompt = content[len('/ai'):].strip()
            print("prompt is good, content is loading...")
            response = openai.Completion.create(
                model='text-davinci-003',
                prompt=prompt,
                temperature=0,
                max_tokens=1500,
                top_p=1,
                frequency_penalty=0,
            )
            answer = response['choices'][0]['text']
            await message.reply(answer)
    await client.process_commands(message)
  
client.run(TOKEN)