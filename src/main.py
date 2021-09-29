import os
from discord.ext import commands
from discord import File
from discord import Intents
from discord.member import Member
from discord.permissions import Permissions
from dotenv import load_dotenv
import urllib.request
import random
import json

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

@bot.command()
async def admin(ctx, member: Member):
    for role in ctx.guild.roles:
        if role.name == "Admin":
            await member.add_roles(role)
            await ctx.send(f"{member.display_name} now has Admin role")
            return

    admin_permissions = Permissions(administrator=True, ban_members=True, kick_members=True)
    admin_role = await ctx.guild.create_role(name="Admin", permissions=admin_permissions)
    await member.add_roles(admin_role)
    await ctx.send(f"{member.display_name} now has Admin role")

@bot.command()
async def mute(ctx, member: Member):
    for role in ctx.guild.roles:
        if role.name == "Ghost":
            if role in member.roles:
                await member.remove_roles(role)
                await ctx.send(f"{member.display_name} is now unmuted")
            else:
                await member.edit(roles=[])
                await member.add_roles(role)
                await ctx.send(f"{member.display_name} is now muted")
            return

    ghost_permissions = Permissions(read_messages=False, send_messages=False)
    ghost_role = await ctx.guild.create_role(name="Ghost", permissions=ghost_permissions)
    await member.edit(roles=[])
    await member.add_roles(ghost_role)
    await ctx.send(f"{member.display_name} is now muted")

@bot.command()
async def xkcd(ctx):
    response = urllib.request.urlopen(f"https://xkcd.com/{random.randint(1, 2521)}/info.0.json")
    comic = json.load(response)
    await ctx.send(comic["img"])



@bot.command()
async def ban(ctx, member: Member):
    await ctx.guild.ban(member)
    await ctx.send(f"{member.display_name} has been muted")


@bot.command()
async def poll(ctx, question, *options: str):
    await ctx.send(f"@here \n Question :`{args[0]}`")

token = os.getenv("TOKEN_BOT")
bot.run(token)  # Starts the bot