import sys
sys.path.append("..")  # Adds higher directory to python modules path.
import asyncio
import random
import json
import autobahn
import ssl
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from autobahn.wamp.types import PublishOptions
from autobahn.wamp import auth
from discord import Embed
from discord.ext.commands import Bot
from discord.embeds import _EmptyEmbed
from datetime import datetime
from bot.config import config

# todo: protected servers may only allow access if you have a token
# todo: raise NotImplementedError

event_loop = asyncio.get_event_loop()
client = Bot(command_prefix=">>")

meepo_pictures = [
    "https://i.imgur.com/9Gqi54C.png",
    "https://i.imgur.com/qtRrDI8.png",
    "https://i.imgur.com/e4Gnvgw.png",
    "https://i.imgur.com/x7GN6oO.png",
    "https://i.imgur.com/Hqq6ii1.png"
]


def datetime_to_string(datetime_object):
    epoch = datetime.utcfromtimestamp(0)
    return (datetime_object - epoch).total_seconds()


class Component(ApplicationSession):
    def onConnect(self):
        self.join(config["crossbar"]["realm"],
                  list(config["crossbar"]["auth"].keys()),
                  config["crossbar"]["role"])

    def onChallenge(self, challenge):
        assert challenge.method == "wampcra", "don't know how to handle authmethod {}".format(challenge.method)

        signature = auth.compute_wcs(config["crossbar"]["auth"][challenge.method]["secret"].encode("utf8"),
                                     challenge.extra["challenge"].encode("utf8"))
        return signature.decode("ascii")

    def onJoin(self, details):
        @client.event
        async def on_ready():
            async def send_message(payload):
                try:
                    print(payload)
                    channel_id = int(payload["channel_id"])
                    channel = client.get_channel(channel_id)
                    await channel.send(content=payload["content"], embed=Embed.from_data(payload["embed"]))
                    return {"info": "success"}
                except:
                    return {"info": "failure"}

            def get_channels(payload):
                guild = client.get_guild(int(payload.get("guild_id", 0)))

                if guild:
                    res = [channel.to_dict()
                           for channel in guild.channels
                           if channel.permissions_for(guild.me).read_messages]
                    return res
                else:
                    return {}

            def get_info():
                res = {
                    "guilds": [guild.to_dict() for guild in client.guilds]
                }
                return res

            try:
                await self.register(get_info, "discordembedorg.github.bridge.basic.get_info_rpc")
                await self.register(get_channels, "discordembedorg.github.bridge.guild.get_channels_rpc")
                await self.register(send_message, "discordembedorg.github.bridge.channel.send_message_rpc")

            except autobahn.wamp.exception.ApplicationError as error:
                print("---ERROR---")
                print(error)
                print("-----------")
                sys.exit("Remote Procedure Call could not be registered but is needed.")

        @client.event
        async def on_message(message):
            payload = message.to_dict()
            print(payload)
            try:
                self.publish("discordembedorg.github.bridge.server.{server_id}.channel.{channel_id}.message".format(
                    server_id=message.guild.id, channel_id=message.channel.id
                ), payload, options=PublishOptions(retain=True))
            except autobahn.wamp.exception.TransportLost as error:
                print("---ERROR---")
                print(error)
                print(message)
                print(payload)
                print("-----------")

        event_loop.create_task(client.start(config["discord"]["bot_token"], bot=True, reconnect=True))


if __name__ == '__main__':
    url = config["crossbar"]["ws"]
    realm = config["crossbar"]["realm"]
    ssl = ssl.SSLContext()
    runner = ApplicationRunner(url=url, realm=realm, ssl=ssl)
    runner.run(Component)

