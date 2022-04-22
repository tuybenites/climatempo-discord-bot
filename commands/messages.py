import discord
from discord.ext import commands
# from api_clima import get_weather_by_id
import decouple
import requests
import json
from datetime import datetime

API_TOKEN = decouple.config("CLIMATEMPO_TOKEN")
DEFAULT_URL = "http://apiadvisor.climatempo.com.br/api/v1/"


def get_id_by_city_and_state(city="Sapucaia do Sul", state="RS"):
    # create the request url for the city
    url_parameters = f"locale/city?name={city}&state={state}&token={API_TOKEN}"
    url_full = DEFAULT_URL + url_parameters

    response = requests.get(url_full)  # get the response
    reponse_dict = json.loads(response.text)[0]  # convert to a dictonary

    return reponse_dict["id"]


def get_weather_by_id(id=5195):

    climate_url = f"weather/locale/{id}/current?token={API_TOKEN}"
    full_url = DEFAULT_URL + climate_url

    response = requests.get(full_url)
    data_raw = json.loads(response.text)
    data = data_raw["data"]
    temperature = data["temperature"]
    humidity = data["humidity"]
    condition = data["condition"]

    return temperature, humidity, condition


def register_city(city="Sapucaia do Sul", state="RS"):
    URL_MANAGER = "http://apiadvisor.climatempo.com.br/api-manager/"
    URL_USER = f"user-token/{API_TOKEN}/locales"

    id = get_id_by_city_and_state(city, state)
    url_full_register = URL_MANAGER + URL_USER
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = f"localeId[]={id}"

    requests.put(url_full_register,
                 headers=headers, data=payload)


class Messages(commands.Cog):
    """ Commands to do the weather configs """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clima")
    async def send_weather(self, ctx):
        # data => temperature, humidity, condition, date
        temperature, humidity, condition = get_weather_by_id()

        now = datetime.now()
        hour = int(now.strftime(r"%H"))
        date = now.strftime(r"%d/%m - %H:%M")

        title_emoji = '🌤️'
        if temperature < 10:
            title_emoji = '❄️'
        elif hour > 12:
            title_emoji = '🌞'
        elif hour > 19:
            title_emoji = '🌃'

        embed = discord.Embed(
            title=f"{title_emoji} Clima em Sapucaia do Sul {title_emoji}",
            description='''" Prefiro o paraíso pelo clima
            e o inferno pela companhia. "'''.replace('\n', ''),
            color=0x00b0f5
        )

        embed.set_author(
            name=self.bot.user.name  # , icon_url=self.bot.user.avatar
        )
        embed.add_field(name="Umidade 💧",
                        value=f" {humidity}%")

        embed.add_field(name="Temperatura 🌡️",
                        value=f" {temperature}° C")
        embed.add_field(name="Condição 📝",
                        value=str(condition))
        embed.add_field(name="Data 📅", value=str(date))

        # GOOGLE_URL = "https://play.google.com/store/apps/details"
        # climatempoIM = GOOGLE_URL+"?id=com.mobimidia.
        # climaTempo&hl=pt_BR&gl=US"
        # embed.set_image(url=climatempoIM)

        # climatempo_png = GOOGLE_URL+"?id=com.mobimidia.
        # climaTempo&hl=pt&gl=GB"
        embed.set_footer(
            text="Dados retirados da API Climatempo",
            # icon_url=climatempo_png
        )

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Messages(bot))
