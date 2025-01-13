import discord, os, logic as l, random as r
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv("dt")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='*', intents=intents)

#Shows in the console that the bot has logged in Discord 
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

#El bot se presenta (*hello)
@bot.command()
async def hello(ctx):
    """El bot se presenta (*hello)"""
    await ctx.send(f'Hola, soy un bot {bot.user}!')

#Repeats heh x amount of times (*heh 10)
@bot.command()
async def heh(ctx, count_heh = 5):
    """Repeats heh x amount of times (*heh 10)"""
    await ctx.send("he" * count_heh)

#Generates a psw with x amount of items (*psw 20)
@bot.command(name = "psw")
async def password(ctx, length=25):
    """Generates a psw with x amount of items (*psw 20)"""
    a = l.contra(length)
    await ctx.send(f"🔏Su contraseña será generada: {a}")

#Flips a coin/chooses randomly "TAILS" OR "HEADS" (*coin)
@bot.command(name = "coin")
async def luck(ctx):
    """Flips a coin/chooses randomly "TAILS" OR "HEADS" (*coin)"""
    await ctx.send(l.flip_coin())

#Adds numbers (*add 2 4)
@bot.command(name = "add")
async def add_numbers(ctx, left: int, right: int):
    """Adds numbers (*add 2 4)"""
    await ctx.send(left + right)

#Chooses one chooice in a list (*choose mom dad sis or 1 2 3)
@bot.command(name = "choose")
async def choose(ctx, *choices: str):
    """Chooses one chooice in a list (*choose mom dad sis)"""
    await ctx.send(r.choice(choices))

#Repeats a frase or # x times (*repeat 3 Holaa, cómo estás?)
@bot.command(name = "repeat")
async def repeat(ctx, times: int, *, content='repeating...'):
    """Repeats a frase or number x times (*repeat 3 Holaa, cómo estás?)"""
    messages = l.repeat_message(times, content)
    for message in messages:
        await ctx.send(message) 

#Writes the date and hour a member joined (*joined @Juan)
@bot.command(name = "joined")
async def joined(ctx, member: discord.Member):
    """Writes the date and hour a member joined (*joined @Juan)"""
    await ctx.send(f'{member.name} se unió el {discord.utils.format_dt(member.joined_at)}')

#Checks if a subcommand has been invoked or not (*cool __ )
@bot.group(name = "cool")
async def cool(ctx):
    """Checks if a subcommand has been invoked or not (*cool __ )"""
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

#Says the bot is cool (*cool bot)
@cool.command(name = 'bot')
async def is_bot_cool(ctx):
    """Says the bot is cool (*cool bot)"""
    await ctx.send('Yes, the bot is cool.')

#Throws x amount of dice and adds the results
@bot.command(name="roll")
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        result = l.roll(dice) 
        await ctx.send(f'{result}')  
    except Exception as e:
        await ctx.send(f"Error: {e}")

#Guess a random number from 1 to 6.
@bot.command(name = "guess")
async def guess(ctx, number: int):
    """Guess a random number from 1 to 6."""
    await l.guess_logic(ctx, number)

bot.run(token)