from settings import *
import logic
import os
import random
from math import pi

import asyncio
import discord
from discord.ext import commands

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable bot y transferirle los privilegios
bot = commands.Bot(command_prefix=setting["prefix"], intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.event
async def joined(ctx, member: discord.Member):
    # Says when a member joined.
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.event
async def on_message_edit(before, after):
    msg = f'**{before.author}** edited their message:\n{before.content} -> {after.content}'
    await before.channel.send(msg)

@bot.command()
async def editme(ctx):
    msg = await ctx.send('10')
    await asyncio.sleep(3.0)
    await msg.edit(content='40')

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
async def meme(ctx):
    ind = random.randint(1, 7)
    img_name = os.listdir('images')
    img_name.remove('rare')
    rare_name = os.listdir('images/rare')
    img = f'rare/{(random.choice(rare_name))}' if ind == 7 else random.choice(img_name)
    with open(f'images/{img}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

    if ind == 7:
        await ctx.send('Tienes suerte! Acaba de salir un meme de pocas probabilidades!')

@bot.command()
async def sine_function(ctx, amp=1, per=pi * 2, x_shift=0, y_shift=0):
    await ctx.send(logic.do_sine_func(amp=amp, per=per, x_shift=x_shift, y_shift=y_shift))

@bot.command()
async def random_anime(ctx):
    await ctx.send(logic.get_anime_name())

@bot.command()
async def help(ctx):
    await ctx.send("""$hello - el bot saludara
$heh # - el bot dira he # veces
$password # - generara una password con la longitud indicada
$editme - un mensaje para flexear
$meme - manda un meme aleatorio
$random_anime - manda un nombre de anime aleatorio
$sine_function # # # # - devuelve una funcion de seno
nota - comandos con # significa que aceptan un numero pero no es obligatorio""")    

bot.run(setting["token"])
