import discord
from api_clima import get_weather_by_id
from datetime import datetime
import requests

CAT_API = r"https://api.thecatapi.com/v1/images/search"


def embed_weather(bot):

    temperature, humidity, condition, date = get_weather_by_id()

    # date: "2017-10-01 12:37:00"
    date = datetime.strptime(date, r"%Y-%m-%d %H:%M:%S")
    hour = int(datetime.strftime(date, "%H"))
    date = datetime.strftime(date, r"%d/%m/%Y - %H:%M")

    title_emoji = '🌤️'
    if temperature < 10:
        title_emoji = '❄️'
    elif hour > 12:
        title_emoji = '🌞'

    # Configuring the embed

    embed = discord.Embed(
        title=f"{title_emoji} Clima em Sapucaia do Sul {title_emoji}",
        description='''" Prefiro o paraíso pelo clima
        e o inferno pela companhia. "'''.replace('\n', ''),
        color=0x00b0f5,
        url="https://github.com/tuybenites/climatempo-discord-bot"
    )

    embed.set_author(
        name=bot.user.name
    )
    embed.add_field(name="Umidade 💧",
                    value=f" {humidity}%")

    embed.add_field(name="Temperatura 🌡️",
                    value=f" {temperature}° C")

    embed.add_field(name="Condição 📝",
                    value=str(condition))

    embed.add_field(name="Data 📅", value=str(date))

    embed.set_image(url="https://i.imgur.com/sZx6LgU.png")

    embed.set_footer(
        text="Dados retirados da API Climatempo"
    )

    return embed


def embed_cat(bot):
    response = requests.get(CAT_API).json()[0]

    url_cat = response["url"]
    breeds = response["breeds"]

    embed = discord.Embed(
        title="🐈 GATO DA VEZ 🐈",
        descripton="purr",
        color=0xff8c00,
        url="https://github.com/tuybenites/climatempo-discord-bot"
    )

    embed.set_author(
        name=bot.user.name
    )

    if breeds:
        breed_name = breeds[0]["name"]
        embed.add_field(
            name="✨Raça",
            value=f"`{breed_name}`"
        )
    else:
        embed.add_field(
            name="✨ Raça",
            value="`Desconhecida`"
        )

    embed.set_image(
        url=url_cat
    )

    embed.set_footer(
        text="Fotos retiradas de 'The Cat API'"
    )

    return embed
