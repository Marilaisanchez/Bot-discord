import random as r, string as s, discord, os
from discord import Embed, Color

def contra(largo):
    elements = s.ascii_letters+s.ascii_lowercase+s.ascii_uppercase+s.digits+s.punctuation
    password = ""
    for i in range(largo):
        password += r.choice(elements)
    return password

def random_emoji():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return r.choice(emoji)

def flip_coin():
    flip = r.randint(0, 2)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"
    
def add_numbers(left: int, right: int):
    return f"{left + right}"

def choose(*choices):
    return r.choice(choices)

def repeat_message(times, content='repeating...'):
    return [content] * times

def get_joined_date(member: discord.Member):
    return discord.utils.format_dt(member.joined_at)

def check_if_cool(ctx):
    if ctx.invoked_subcommand is None:
        return f'No, {ctx.subcommand_passed} is not cool'
    else:
        return None
    
def is_bot_cool():
    return 'Yes, the bot is cool.'

def roll(dice: str):
    try:
        num_dice, sides = map(int, dice.lower().split('d'))
        results = [r.randint(1, sides) for _ in range(num_dice)]
        total = sum(results)
        return f"Tiradas: {results} | Total: {total}"
    except ValueError:
        return "Format has to be in NdN! Example: 2d6"

def guess_logic(ctx, number: int):
    value = r.randint(1, 6)
    correct = (number == value)
    return tick_logic(ctx, correct)

def tick_logic(ctx, correct: bool):
    emoji = '\N{WHITE HEAVY CHECK MARK}' if correct else '\N{CROSS MARK}'
    try:
        return ctx.message.add_reaction(emoji)
    except discord.HTTPException:
        return None

def generate_emoji(emoji_name):
    emoji_dict = {
        "smile": "😊",
        "laughing": "😆",
        "wink": "😉",
        "blush": "😊",
        "cool": "😎",
        "cry": "😭",
        "angry": "😡",
        "surprised": "😲",
        "thinking": "🤔",
        "sunglasses": "🕶️",
        "sleeping": "😴",
        "relieved": "😌",
        "party": "🥳",
        "clown": "🤡",
        "nerd": "🤓",
        "sick": "🤒",
        "devil": "😈",
        "skull": "💀",
        "heart": "❤️",
        "star": "⭐",
        "rocket": "🚀",
        "sun": "☀️",
        "moon": "🌙",
        "fire": "🔥",
        "alien": "👽",
        "cat": "🐱",
        "dog": "🐶",
        "pizza": "🍕",
        "cake": "🎂",
        "flower": "🌸",
        "car": "🚗",
        "bicycle": "🚲",
        "computer": "💻",
        "book": "📖",
        "music": "🎵",
        "camera": "📸",
        "gift": "🎁"
    }

    return emoji_dict.get(emoji_name.lower(), "Emoji not found. Try with another one.")

def piedra_papel_tijera(user_choice):
    choices = ["piedra", "papel", "tijera"]
    bot_choice = r.choice(choices)
    
    if user_choice.lower() not in choices:
        return "Por favor, elige entre 'piedra', 'papel' o 'tijera'."
    
    if user_choice.lower() == bot_choice:
        return f"Ambos elegimos {bot_choice}. ¡Es un empate!"
    
    if (user_choice.lower() == "piedra" and bot_choice == "tijera") or \
       (user_choice.lower() == "papel" and bot_choice == "piedra") or \
       (user_choice.lower() == "tijera" and bot_choice == "papel"):
        return f"Tú elegiste {user_choice}, yo elegí {bot_choice}. ¡Ganaste!"
    
    return f"Tú elegiste {user_choice}, yo elegí {bot_choice}. ¡Perdiste!"

def meme():
    with open("IMG/meme1.jpg", "rb") as IMG:
        pic = discord.File(IMG)
    return (pic)

def momo():
    listmeme = r.choice(os.listdir("IMG"))
    with open(f"IMG/{listmeme}", "rb") as IMG:
        pic = discord.File(IMG)
    return (pic)

MEMES_CATEGORIES = {
    "cats": "./memes/cats/",
    "dogs": "./memes/dogs/",
    "movies": "./memes/movies/"
}

def categ_memes(categoria):
    if categoria not in MEMES_CATEGORIES:
        return None

    folder_path = MEMES_CATEGORIES[categoria]
    images = [f for f in os.listdir(folder_path)]

    if images:
        meme_image = r.choice(images)
        file_path = os.path.join(folder_path, meme_image)
        return file_path
    else:
        return None

def create_help_embed(help_categories):
    embed = Embed(
        title="Help Menu",
        description="Available commands grouped by categories:",
        color= Color.purple()
    )
    for category, commands in help_categories.items():
        command_list = "\n".join([f"`{cmd}` - {desc}" for cmd, desc in commands])
        embed.add_field(name=category, value=command_list, inline=False)
    
    return embed

command_details = {
    #⚙️General
    "hello": {
        "description": "The bot introduces itself.",
        "usage": "*hello",
        "example": "*hello",
        "notes": "This command makes the bot introduce itself with a welcome message.",
    },
    "help": {
        "description": "Shows the help menu.",
        "usage": "*help",
        "example": "*help",
        "notes": "This command displays all available commands, grouped by categories.",
    },
    "joined": {
        "description": "Shows the date and time a member joined the server.",
        "usage": "*joined <@user>",
        "example": "*joined @username",
        "notes": "This command requires a user mention to work correctly.",
    },
    # 🛠️Utility Commands
    "add": {
        "description": "Adds two numbers.",
        "usage": "*add <num1> <num2>",
        "example": "*add 3 7",
        "notes": "This command returns the sum of the two provided numbers.",
    },
    "cool": {
        "description": "Checks if a subcommand has been invoked or not.",
        "usage": "*cool <subcommand>",
        "example": "*cool bot",
        "notes": "This command checks if a subcommand has been invoked or not. Example: *cool bot.",
    },
    "eco": {
        "description": "Generates a solution or recommendations to reduce pollution.",
        "usage": "*eco <number/problematic>",
        "example": "*eco 1",
        "notes": "This command gives you advice and information about environmental problems. \n 1. Greenhouse gas emissions \n 2. Global warming \n 3. Recycle, reuse and reduce",
    },
    "repeat": {
        "description": "Repeats a phrase or number a specified number of times.",
        "usage": "*repeat <times> <phrase>",
        "example": "*repeat 5 hello",
        "notes": "This command repeats a phrase or number the specified number of times.",
    },
    "psw": {
        "description": "Generates a password with a specified number of characters.",
        "usage": "*psw <length>",
        "example": "*psw 12",
        "notes": "Generates a random password of length `length`.",
    },
    "choose": {
        "description": "Chooses one option from a provided list.",
        "usage": "*choose <list>",
        "example": "*choose apple, banana, orange",
        "notes": "This command randomly selects one option from the provided list.",
    },
    # 🎉Fun Commands
    "cool bot": {
        "description": "Says the bot is cool.",
        "usage": "*cool bot",
        "example": "*cool bot",
        "notes": "This command responds with a message saying the bot is cool.",
    },
    "duck": {
        "description": "Generates duck photos.",
        "usage": "*duck",
        "example": "*duck",
        "notes": "This command generates a random photo of a duck.",
    },
    "emoji": {
        "description": "Generates a specific emoji.",
        "usage": "*emoji <category>",
        "example": "*emoji heart",
        "notes": "Available categories: smile, laughing, wink, blush, cool, cry, angry, surprised, thinking, sunglasses, sleeping, relieved, party, clown, nerd, sick, devil, skull, heart, star, rocket, sun, moon, fire, alien, cat, dog, pizza, cake, flower, car, bicycle, computer, book, music, camera, gift.",
    },
    "heh": {
        "description": "Repeats 'heh' a specified number of times.",
        "usage": "*heh <times>",
        "example": "*heh 3",
        "notes": "This command repeats 'heh' the specified number of times.",
    },
    "meme": {
        "description": "Generates the same meme every time.",
        "usage": "*meme",
        "example": "*meme",
        "notes": "This command always generates the same meme when invoked.",
    },
    "memes": {
        "description": "Sends a meme from a specific category.",
        "usage": "*memes <category>",
        "example": "*memes dogs",
        "notes": "Available categories: dogs, cats and movies.",
    },
    "momo": {
        "description": "Generates random memes.",
        "usage": "*momo",
        "example": "*momo",
        "notes": "This command generates a random meme every time it is invoked.",
    },
    "random_emoji": {
        "description": "Generates a random emoji.",
        "usage": "*random_emoji",
        "example": "*random_emoji",
        "notes": "This command generates a random emoji every time it is invoked.",
    },
    # 🎮Games
    "guess": {
        "description": "Guess a random number between 1 and 6.",
        "usage": "*guess <number>",
        "example": "*guess 3",
        "notes": "This command generates a random number between 1 and 6 to guess.",
    },
    "ppt": {
        "description": "Play rock, paper, scissors.",
        "usage": "*ppt <choice>",
        "example": "*ppt paper",
        "notes": "This command plays the classic rock, paper, scissors game.",
    },
    "roll": {
        "description": "Rolls a dice in NdN format.",
        "usage": "*roll <NdN>",
        "example": "*roll 2d6",
        "notes": "This command rolls a dice in NdN format, where N is the number of dice and the maximum value of each die.",
    },
    "coin": {
        "description": "Flips a coin/chooses randomly between HEADS OR TAILS.",
        "usage": "*coin",
        "example": "*coin",
        "notes": "This command flips a coin and randomly chooses between HEADS or TAILS.",
    },
}

def create_command_help_embed(command):
    """
    Crea un embed con los detalles de un comando específico.
    """
    if command in command_details:
        details = command_details[command]
        embed = discord.Embed(title=f"Help: {command}", color=discord.Color.green())
        embed.add_field(name="Description", value=details["description"], inline=False)
        embed.add_field(name="Usage", value=f"`{details['usage']}`", inline=False)
        embed.add_field(name="Example", value=f"`{details['example']}`", inline=False)
        embed.add_field(name="Notes", value=details.get("notes", "None"), inline=False)
        return embed
    return None 