import discord

def sol_emisión_gases():
    embed = discord.Embed(
        title = "Emisión de gases de efecto invernadero",
        description = "Descubre como puedes reducir lo más posible la emisón de gases",
        color = 0x00aaff
    )

    embed.add_field(
        name = "Recomendaciones para reducir la emisión de gases",
        value = "Reducir el consumo de energía: Apagar las luces y usar focos led.",
        inline = False
    )

    embed.set_thumbnail(
        url = "https://i.postimg.cc/yNYvrvGk/gases2.webp"
    )

    return embed

def sol_calentamientoglo():
    embed = discord.Embed(
        title = "Calentamiento global",
        description = "Descubre como puedes reducir el calentamiento global",
        color = 0x00aaff
    )

    embed.add_field(
        name = "Recomendaciones para reducir el calentamiento global",
        value = "Reforestación: Plantar árboles y restaurar bosques para aumentar la absorción de CO2 de la atmósfera.",
        inline = False
    )
 
    embed.set_thumbnail(
        url = "https://i.postimg.cc/hjPCYgCF/calentamiento1.png"
    )

    return embed

def consejos_rrr():
    embed = discord.Embed(
        title = "Reciclar, reusar, reducir",
        description = "Descubre como puedes aplicar las tres erres de manera facíl",
        color = 0x00aaff
    )

    embed.add_field(
        name = "Formas de aplicar las tres erres",
        value = "Separar los residuos por tipo y depositarlos en los contenedores correspondientes.",
        inline = False
    )

    embed.set_thumbnail(
        url = "https://i.postimg.cc/P5stZFxs/reciclaje1.webp"
    )
    return embed