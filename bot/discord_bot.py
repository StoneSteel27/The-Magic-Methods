import io
import logging
import os
import re
import typing

import discord
from discord.ext import commands
from dotenv import load_dotenv
from PIL import Image

import code_stego

# Configure logging
logging.basicConfig(
    filename='bot.log',  # Specify the name of the log file
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO  # Set the desired logging level
)

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
    """Implements on_ready"""
    print("Authentication . {0.user}  online!".format(bot))  # TODO: logging
    logging.info(f"Bot -{bot.user}- is online!")  # Log that the bot is online


@bot.command()
async def encode(ctx: commands.Context, *, msg: str):
    """Implements encode"""
    try:
        if match := FORMATTED_CODE_REGEX.match(msg):
            code = match.group("code")
        else:
            code = msg
        image = code_stego.encode(code)
        image_file = io.BytesIO()
        image.save(image_file, "png")
        image_file.seek(0)
        await ctx.send(file=discord.File(image_file, "image.png"))
    except Exception as e:
        logging.error(f"Error encoding message: {e}")  # Log the encoding error
        await ctx.send("An error occurred while encoding the message.")


@bot.command()
async def decode(
        ctx: commands.Context, attachment: typing.Optional[discord.Attachment]
):
    """Implements decode"""
    if not (attachment and attachment.content_type.startswith("image")):
        await ctx.send("Could not find image attachment!")
        return
    image = Image.open(io.BytesIO(await attachment.read()))
    try:
        code = code_stego.decode(image)
        await ctx.send(f"```\n{code}\n```")
    except Exception as e:
        logging.error(f"Error decoding image: {e}")  # Log the decoding error
        await ctx.send("An error occurred while decoding the image.")  # TODO escape potential ` in code


bot.run(os.getenv("TOKEN"))
