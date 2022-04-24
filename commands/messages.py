from discord.ext import commands
from configure_embed import embed_cat, embed_weather


class Messages(commands.Cog):
    """ Commands to do the weather configs """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="clima",
        help="Informações do clima (não recebe parâmetros)"
    )
    async def send_weather(self, ctx):
        embed = embed_weather(self.bot)
        await ctx.channel.send(embed=embed)

    @commands.command(
        name="gato",
        help="Foto aleatória de um gato (não recebe paramêtros)"
    )
    async def send_cat(self, ctx):
        embed = embed_cat(self.bot)
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Messages(bot))
