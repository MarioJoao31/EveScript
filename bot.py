import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print("I´m on Mário! Macaco Miner activated ")

@bot.event # se tiver a palavra gay elimina a mensagem e envia o aviso 
async def on_message(message):
    # verification to not read the bot messages 
    if message.author == bot.user:
        return
    if "gay" in message.content:
        await message.channel.send(
            f"Alguem falou de gays? {message.author.name} COME O MEU PAU"
        )
        await message.delete()

@bot.command(name="funcoes")
async def funcoes(ctx):
    name = ctx.author.name

    response= "Olá " + name

    await ctx.send(response)

@bot.command(name="ola")
async def ola(ctx):
    name = ctx.author.name

    response= "Olá "+ name + " seu filho de 30 putas!" 

    await ctx.send(response)

@bot.command(name="runbot")
async def runbot(ctx):
    runbot()


load_dotenv()
bot.run(os.getenv("TOKEN"))
