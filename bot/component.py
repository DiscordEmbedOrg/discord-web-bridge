import sys
sys.path.append("..")  # Adds higher directory to python modules path.
import asyncio
import autobahn
from autobahn.asyncio.wamp import ApplicationSession
from autobahn.wamp.types import PublishOptions
from autobahn.wamp import auth
from discord import Embed
from discord.ext.commands import Bot
from bot.config import config


class Component(ApplicationSession):
    def onConnect(self):
        self.join(**config["CROSSBAR_AUTHENTICATION"])

    def onChallenge(self, challenge):
        if "wampcra" in config["CROSSBAR_AUTH_SECRET"].keys():
            signature = auth.compute_wcs(config["CROSSBAR_AUTH_SECRET"]["wampcra"].encode("utf8"),
                                         challenge.extra["challenge"].encode("utf8"))
            return signature.decode("ascii")
        else:
            raise NotImplementedError("No alternative authentication implemented.")

    def onJoin(self, details):
        client = Bot(command_prefix=">>")

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

        asyncio.get_event_loop().create_task(client.start(config["DISCORD"]["bot_token"], bot=True, reconnect=True))

    async def onDisconnect(self):
        super().onDisconnect()
        print("Component disconnected.")
        asyncio.get_event_loop().stop()
