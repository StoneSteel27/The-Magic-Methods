import discord

from PIL import Image
from mainapp.encoder import encode
from mainapp.decoder import decode

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Authentication . {0.user}  online!".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.attachments) != 0:
        # Check if the uploaded file is an image
        attachment = message.attachments[0]
        if attachment.content_type.startswith("image"):
            with open("uploaded_image.png", "wb") as f:
                await attachment.save(f)

            image = Image.open("uploaded_image.png")

            decoded = decode(image)
            await message.channel.send(f"```{decoded}```")

    user_message = message.content
    if user_message.startswith("```"):
        print(user_message[2:])
        image = encode(user_message[3:-3])
        image.save("encoded.png")
        await message.channel.send(file=discord.File("encoded.png"))


client.run("token_here")
