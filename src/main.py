import os
from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv

load_dotenv()

intents = Intents.all()

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    intents=intents,
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = "Mathmat#9030"  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author)

@bot.command()
async def count(ctx):
    statuslist = { "online": 0, "offline": 0, "idle": 0, "dnd": 0 }
    for member in ctx.guild.members:
        statuslist[member.raw_status] = statuslist[member.raw_status] + 1
    
    await ctx.send(f"{statuslist['online']} are online, {statuslist['idle']} are idle, {statuslist['dnd']} are dnd and {statuslist['offline']} are off")


token = os.getenv("TOKEN_BOT")
bot.run(token)  # Starts the bot