from settings import *
import logic
import discord
from discord.ext import commands

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable bot y transferirle los privilegios
bot = commands.Bot(command_prefix=setting["prefix"], intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx, length = 8):
    await ctx.send(logic.gen_pass(length))

@bot.command()
async def joined(ctx, member: discord.Member):
    # Says when a member joined.
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


bot.run(setting["token"])
