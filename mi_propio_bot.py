import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='$')

quotes = [
    "Cree que puedes y estarás a mitad del camino.",
    "La única manera de hacer un gran trabajo es amar lo que haces.",
    "El éxito no es definitivo, el fracaso no es fatal: lo que cuenta es el coraje de continuar.",
    "No mires el reloj; haz lo que hace. Sigue adelante.",
    "Eres capaz de hacer cosas increíbles"
]

def get_quote():
    return random.choice(quotes)

@bot.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.send(quote)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run("Ingresa tu token")
