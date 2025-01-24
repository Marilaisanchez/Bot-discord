import discord, os, logic as l, random as r, commandapi as ca, ambiente as am
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv("dt")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='*', intents=intents, help_command=None)

#Shows in the console that the bot has logged in Discord 
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

#El bot se presenta (*hello)
@bot.command()
async def hello(ctx):
    """El bot se presenta (*hello)"""
    await ctx.send(f'¡Hola! Soy {bot.user}! Un bot. ¿En qué puedo ayudarte hoy?')

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

#Generates an emoji
@bot.command(name = "random_emoji")
async def random_emoji(ctx):
    """Generates an emoji (*random_emoji)"""
    await ctx.send(l.random_emoji())

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
    """Rolls a dice in NdN format. (*roll 2d6)"""
    try:
        result = l.roll(dice) 
        await ctx.send(f'{result}')  
    except Exception as e:
        await ctx.send(f"Error: {e}")

#Guess a random number from 1 to 6.
@bot.command(name = "guess")
async def guess(ctx, number: int):
    """Guess a random number from 1 to 6 (*guess 3)"""
    await l.guess_logic(ctx, number)

#Generates an especific emoji ("emoji heart")
@bot.command(name = "emoji")
async def generate_emoji(ctx, emoji_name: str):
    """Generates an especific emoji (*emoji heart)"""
    emoji = l.generate_emoji(emoji_name)
    await ctx.send(emoji)

#Piedra, papel o tijera
@bot.command(name = "ppt")
async def ppt(ctx, user_choice: str):
    """Piedra, papel o tijera (*ppt tijera)"""
    result = l.piedra_papel_tijera(user_choice)
    await ctx.send(result)

#Generates the same meme
@bot.command(name = "meme")
async def memes(ctx):
    """Generates the same meme (*meme)"""
    a = l.meme()
    await ctx.send(file = a)

#Generates random meme
@bot.command(name = "momo")
async def memes(ctx):
    """Generates random memes (*momo)"""
    a = l.momo()
    await ctx.send(file = a)

#Generates duck photos
@bot.command(name = "duck")
async def ducks(ctx):
    """Generates duck photos (*duck)"""
    a = ca.duck_image()
    await ctx.send(a)

#Sends a meme of an especific category
@bot.command(name = "memes")
async def meme(ctx, categoria: str):
    """Sends a meme of an especific category (*memes dogs)"""
    meme_path = l.categ_memes(categoria)
    if meme_path:
        with open(meme_path, "rb") as file:
            await ctx.send(file=discord.File(file, filename=os.path.basename(meme_path)))
    else:
        await ctx.send(f"Category not found '{categoria}'.")

@bot.command(name = "eco")
async def ecologia(ctx, opc:int):
    """Generates a solution or recommendations to reduce pollution (*eco 1,2 or 3) the number depends on the problematic"""
    if opc == 1:
        await ctx.send(embed = am.sol_emisión_gases())

    elif opc == 2:
        await ctx.send(embed = am.sol_calentamientoglo())

    elif opc == 3:
        await ctx.send(embed = am.consejos_rrr())

    else:
        await ctx.send("Esta opción no existe")

help_categories = {
    "⚙️ General Commands": [
        ("*hello", "El bot se presenta"),
        ("*help", "Shows the help menu"),
        ("*joined <@user>", "Writes the date and hour a member joined"),
],

    "🛠️ Useful Commands": [
        ("*add <num1> <num2>", "Adds numbers"),
        ("*cool <subcommand>", "Checks if a subcommand has been invoked or not"),
        ("*eco <number/problematic>", "Generates a solution or recommendations to reduce pollution"),
        ("*repeat <times> <phrase>", "Repeats a phrase or number x times"),
        ("*psw <length>", "Generates a password with x items"),
        ("*choose <list>", "Chooses one chooice in a list"),
],

    "🎉 Fun Commands": [
        ("*duck", "Generates duck photos"),
        ("*emoji <category>", "Generates an especific emoji"),
        ("*heh <times>", "Repeats heh x amount of times"),
        ("*meme", "Generates the same meme"),
        ("*memes <category>", "Sends a meme of a specific category"),
        ("*momo", "Generates random memes"),
        ("*random_emoji", "Generates an emoji"),
],
    
    "🎮 Games": [
        ("*guess <number>", "Guess a random number from 1 to 6"),
        ("*ppt <choice>", "Play rock, paper, scissors"),
        ("*roll <NdN>", "Rolls a dice in NdN format"),
        ("*coin", "Flips a coin/chooses randomly TAILS OR HEADS"),
    ],
    
    "Type *help <command> to find more info and examples of the command.":[],
}

@bot.command(name="help")
async def help(ctx, command=None):
    """Muestra el mensaje de ayuda con los comandos disponibles o detalles de un comando específico."""
    if command:  # Si el usuario pasa un comando específico
        embed = l.create_command_help_embed(command.lower())  # Convertir a minúsculas para evitar problemas de mayúsculas
        if embed:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"No help found for the command: `{command}`.")
    else:  # Si no pasa ningún comando, muestra el menú general
        embed = l.create_help_embed(help_categories)
        await ctx.send(embed=embed)

bot.run(token)