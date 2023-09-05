import io
import os
import re
import typing

import discord
from discord.ext import commands
from dotenv import load_dotenv
from PIL import Image

import code_stego

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


FORMATTED_CODE_REGEX = re.compile(
    r"(?P<delim>(?P<block>```)|``?)"  # code delimiter: 1-3 backticks; (?P=block) only matches if it's a block
    r"(?(block)(?:(?P<lang>[a-z]+)\n)?)"  # if we're in a block, match optional language (only letters plus newline)
    r"(?:[ \t]*\n)*"  # any blank (empty or tabs/spaces only) lines before the code
    r"(?P<code>.*?)"  # extract all code inside the markup
    r"\s*"  # any more whitespace before the end of the code markup
    r"(?P=delim)",  # match the exact same delimiter from the start again
    re.DOTALL | re.IGNORECASE,  # "." also matches newlines, case insensitive
)


@bot.event
async def on_ready():
    print("Authentication . {0.user}  online!".format(bot))  # TODO: logging


@bot.command()
async def encode(ctx: commands.Context, *, msg: str):
    if match := FORMATTED_CODE_REGEX.match(msg):
        code = match.group("code")
    else:
        code = msg
    image = code_stego.encode(code)  # TODO handle errors
    image_file = io.BytesIO()
    image.save(image_file, "png")
    image_file.seek(0)
    await ctx.send(file=discord.File(image_file, "image.png"))


@bot.command()
async def decode(
    ctx: commands.Context, attachment: typing.Optional[discord.Attachment]
):
    if not (attachment and attachment.content_type.startswith("image")):
        await ctx.send("Could not find image attachment!")
        return
    image = Image.open(io.BytesIO(await attachment.read()))
    code = code_stego.decode(image)  # TODO handle errors
    await ctx.send(f"```\n{code}\n```")  # TODO escape potential ` in code


bot.run(os.getenv("TOKEN"))
