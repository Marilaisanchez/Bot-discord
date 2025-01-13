import random as r, string as s, discord

def contra(largo):
    elements = s.ascii_letters+s.ascii_lowercase+s.ascii_uppercase+s.digits+s.punctuation
    password = ""
    for i in range(largo):
        password += r.choice(elements)
    return password

def emoji():
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

