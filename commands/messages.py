import discord
from discord.ext import commands
from api_clima import get_weather_by_id
from datetime import datetime


class Messages(commands.Cog):
    """ Commands to do the weather configs """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clima")
    async def send_weather(self, ctx):
        # data => temperature, humidity, condition, date
        temperature, humidity, condition, date = get_weather_by_id()

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


if __name__ == "__main__":
    print(get_weather_by_id())
