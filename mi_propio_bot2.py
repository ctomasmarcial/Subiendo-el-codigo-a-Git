import discord
from discord.ext import commands
import random

# Initialize the bot
bot = commands.Bot(command_prefix='$')

# Define a list of quotes
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

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Comandos disponibles", description="Aquí están los comandos disponibles en el bot:", color=discord.Color.random())
    embed.add_field(name="$help", value="Muestra este menú de ayuda", inline=False)
    embed.add_field(name="$inspire", value="Envía una cita inspiradora", inline=False)
    embed.add_field(name="$ping", value="Responde con 'pong'", inline=False)
    await ctx.send(embed=embed)

bot.run('token')
