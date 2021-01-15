import io
import os
import shlex
import sys
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO

import discord

from swntools import console_script as cs


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up


client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!swntools") or message.content.startswith("!plunder"):
        # response_str = "Opps, I made an oof!"
        query = "swntools -h"

        if message.content.startswith("!swntools"):
            query = str(message.content[1:])  # only remove '!'
        elif message.content.startswith("!plunder"):
            query = "swntools " + str(message.content)[1:]  # remove '!' and add swntools to string

        f_err = io.StringIO()
        f_out = io.StringIO()
        with redirect_stderr(f_err):
            with redirect_stdout(f_out):
                try:
                    cs.SWNTools(shlex.split(query))
                except SystemExit:
                    pass

        output = f_out.getvalue() + "\n" + f_err.getvalue()

        await message.channel.send(output)


client.run(os.getenv("DISCORD_TOKEN"))
