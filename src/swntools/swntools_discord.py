import os
import subprocess

import discord

# subprocess.run(["ls", "-l"])

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!swntools") or message.content.startswith("!plunder"):
        response_str = "Opps, I made an oof!"
        query = ""

        if message.content.startswith("!swntools"):
            query = str(message.content)[len("!swntools") :]
        elif message.content.startswith("!plunder"):
            query = " " + str(message.content)[1:]

        try:
            response_str = subprocess.check_output("swntools" + query, stderr=subprocess.STDOUT).decode("utf-8")
        except subprocess.CalledProcessError as e:
            response_str = e.output.decode("utf-8")
            # print(e.output)

        await message.channel.send(response_str)


client.run(os.getenv("DISCORD_TOKEN"))
