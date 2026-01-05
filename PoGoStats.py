from datetime import datetime
import discord
from discord.ext import commands
from dotenv import load_dotenv
from mongoPoGo import CharmanderStats, CharmeleonStats, CharizardStats, CharizardXStats, CharizardYStats
import os

# Connection URI
uri = 'mongodb://localhost:27017'
client = (uri)

load_dotenv()

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def Charmander(ctx):
    Charmander = CharmanderStats
    await ctx.send(Charmander)

@bot.command()
async def Charmeleon(ctx):
    Charmeleon = CharmeleonStats
    await ctx.send(Charmeleon)

@bot.command()
async def Charizard(ctx):
    Charizard = CharizardStats
    await ctx.send(Charizard)

@bot.command()
async def CharizardX(ctx):
    CharizardX = CharizardXStats
    await ctx.send(CharizardX)

@bot.command()
async def CharizardY(ctx):
    CharizardY = CharizardYStats
    await ctx.send(CharizardY)

bot.run("BotToken")
