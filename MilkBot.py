import discord
import os
import random
from dotenv import load_dotenv
from botlogic import gen_pass, gen_emodji, flip_coin
from discord.ext import commands
from discord import app_commands
import json
import requests
import asyncio

load_dotenv()

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True

class Client(commands.Bot):
    async def  on_ready(self):
        print(f'We have logged in as {self.user}')
        try:
            await self.tree.sync()
            print(f'Synced commands to the bot.')
        except Exception as e:
            print(f"Error syncing commands: {e}")   

client = Client(command_prefix='!', intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

token = os.getenv('TOKEN')

@client.tree.command(name="plastic_alt", description="Generates platic alternatives")
async def plastic_alternative(interaction: discord.Interaction, item: str):
    alternatives = {
        "straw": ["metal straw", "bamboo straw", "glass straw"],
        "bag": ["cloth bag", "jute bag", "paper bag"],
        "bottle": ["reusable water bottle", "glass bottle", "stainless steel bottle"],
        "cutlery": ["bamboo cutlery", "metal cutlery", "compostable cutlery"]
    }
    item_lower = item.lower()
    if item_lower in alternatives:
        alternative = random.choice(alternatives[item_lower])
        await interaction.response.send_message(f"A good alternative to plastic {item} is: {alternative}.")
    else:
        await interaction.response.send_message(f"Sorry, I don't have alternatives for {item}.", ephemeral=True)

@client.tree.command(name="oil_alt", description="Generates oil alternatives")
async def oil_alternative(interaction: discord.Interaction, product: str):
    alternatives = {
        "energy": ["solar power", "wind power", "hydropower", "geothermal energy"],
        "fuel": ["ethanol", "biodiesel", "biogas"],
        "cosmetic": ["natural oils", "plant-based ingredients", "mineral-based products"],
        "cleaning_products": ["vinegar solutions", "baking soda mixtures", "castile soap"]
    }
    product_lower = product.lower()
    if product_lower in alternatives:
        alternative = random.choice(alternatives[product_lower])
        await interaction.response.send_message(f"A good alternative to oil-based {product} is: {alternative}.")
    else:
        await interaction.response.send_message(f"Sorry, I don't have alternatives for {product}.", ephemeral=True)

@client.tree.command(name="alt_info", description="Provides information on alternatives")
async def alternative_info(interaction: discord.Interaction, alternative: str):
    info = {
        "solar power": "Solar power is a renewable energy source that harnesses sunlight to generate electricity.",
        "wind power": "Wind power uses wind turbines to convert wind energy into electricity.",
        "hydropower": "Hydropower generates electricity by using the energy of flowing water.",
        "geothermal energy": "Geothermal energy utilizes heat from the Earth's interior for power generation and heating.",
        "ethanol": "Ethanol is a biofuel made from fermenting plant materials like corn and sugarcane.",
        "biodiesel": "Biodiesel is a renewable fuel made from vegetable oils or animal fats.",
        "biogas": "Biogas is produced from the anaerobic digestion of organic matter such as food waste and manure.",
        "natural oils": "Natural oils like coconut oil and almond oil are used in cosmetics for their moisturizing properties.",
        "plant-based ingredients": "Plant-based ingredients in cosmetics are derived from plants and are often more sustainable.",
        "mineral-based products": "Mineral-based products use minerals like zinc oxide and titanium dioxide for skin protection.",
        "vinegar solutions": "Vinegar solutions are effective natural cleaners that can disinfect and remove odors.",
        "baking soda mixtures": "Baking soda mixtures can be used for scrubbing surfaces and deodorizing.",
        "castile soap": "Castile soap is a vegetable-based soap that is biodegradable and gentle on the skin."
    }
client.run("")
