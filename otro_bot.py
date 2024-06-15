import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='contaminacion')
async def contaminacion(ctx):
    await ctx.send('La contaminación ambiental es un problema grave que afecta a todo el mundo. ¡Es importante que tomemos medidas para reducir nuestra huella de carbono!')

@bot.command(name='tips')
async def tips(ctx):
    await ctx.send('Aquí te dejo algunos consejos para reducir tu impacto ambiental:\n'
                    '- Reduce, Reusa, Recicla\n'
                    '- Usa transporte público o bicicleta\n'
                    '- Apaga las luces y los electrodomésticos cuando no los estés usando\n'
                    '- Usa productos ecológicos')

bot.run('token')
