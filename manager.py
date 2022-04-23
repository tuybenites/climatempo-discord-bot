from discord.ext.commands.errors import CommandNotFound
from discord.ext.commands.errors import MissingRequiredArgument
from discord.ext import commands


class Manager(commands.Cog):
    """ Commands to do the weather configs """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"EU SOU UM TESTE. ME CHAMO {self.bot.user}")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.channel.send(
                """Comando não encontrado.
                Digite !!help para obter ajuda"""
            )
        elif isinstance(error, MissingRequiredArgument):
            await ctx.channel.send(
                """Favor enviar todos os argumentos.
                Digite !!help para obter ajuda"""
            )
        else:
            raise error


def setup(bot):
    bot.add_cog(Manager(bot))
