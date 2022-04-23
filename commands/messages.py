import discord
from discord.ext import commands
from api_clima import get_weather_by_id
from datetime import datetime


class Messages(commands.Cog):
    """ Commands to do the weather configs """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="clima",
        help="Informações do clima (não recebe parâmetros)"
    )
    async def send_weather(self, ctx):

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
        elif hour > 19:
            title_emoji = '🌃'

        # Configuring the embed

        embed = discord.Embed(
            title=f"{title_emoji} Clima em Sapucaia do Sul {title_emoji}",
            description='''" Prefiro o paraíso pelo clima
            e o inferno pela companhia. "'''.replace('\n', ''),
            color=0x00b0f5,
            url="https://github.com/tuybenites/climatempo-discord-bot"
        )

        embed.set_author(
            name=self.bot.user.name
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

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Messages(bot))
