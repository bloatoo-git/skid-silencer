import os, re
from dotenv import load_dotenv
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

platforms = ["account", "instagram", "snapchat", "discord", "reddit", "steam", ]
regex_str = r"(?=.*hack)(?=.*\b(?:{})\b)".format("|".join(platforms))
pattern = re.compile(regex_str)


def run_skid_silencer():
    TOKEN = os.getenv('TOKEN')
    client = commands.Bot(command_prefix="$", intents=intents)


    # CLIENT EVENTS

    @client.event
    async def on_ready():
        print(f"{client.user} is now hunting for skids.")

    @client.event
    async def on_message(ctx):
        if ctx.author != client.user and re.match(pattern, ctx.content):
            await ctx.delete()
            await ctx.author.add_roles(ctx.guild.get_role(1082635084072505424))
            await ctx.author.kick(reason="lmao get out")

        await client.process_commands(ctx)

    # CLIENT COMMANDS

    @client.command(name="send_msg")
    async def _send_msg(ctx, id: int, msg: str):
        chnl = client.get_channel(id)
        await chnl.send(msg)

    @client.command(name="purge")
    async def _pruge(ctx, number: int):
        await ctx.channel.purge(limit=number)

    client.run(TOKEN) # starting the client


if __name__ == '__main__':
    load_dotenv() # loads .env file with token
    run_skid_silencer()