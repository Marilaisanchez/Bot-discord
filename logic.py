import random as r, string as s

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