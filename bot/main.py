import sys
import asyncio
import random
import json
import autobahn
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from autobahn.wamp.types import PublishOptions
from discord import Embed
from discord.ext.commands import Bot
from discord.embeds import _EmptyEmbed
from datetime import datetime
from bot.config import config


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
    async def onJoin(self, details):
        @client.event
        async def on_ready():
            def send_message(payload):
                payload = json.loads(payload)
                # todo: implement check so discord bot can only posts in select few channels
                # todo: payload["token"]

                random.seed(payload["author_name"])
                embed = Embed(colour=random.randint(0, 16777215),
                              description=payload["content"])
                embed.set_author(name=payload["author_name"],
                                 icon_url=payload["author_avatar_url"] if payload["author_avatar_url"] is not ""
                                 else meepo_pictures[random.randint(0, len(meepo_pictures) - 1)])

                # todo: implement check so discord bot can only posts in select few channels
                # todo: send message over webhook?
                # todo: restrict size of message <2000
                allowed_channels = [398907517326852097, 412326162430427146]
                channel_id = int(payload["channel"])
                if channel_id in allowed_channels:
                    channel = client.get_channel(channel_id)
                    event_loop.create_task(channel.send(embed=embed))
                    return "success"
                else:
                    return "sorry. no. only works in select few channels."

            def get_channels(payload):
                payload = json.loads(payload)
                guild = client.get_guild(int(payload["guild_id"]))
                member = guild.get_member(client.user.id)

                res = []
                for text_channel in guild.text_channels:
                    if text_channel.permissions_for(member).read_messages:
                        res.append({
                            "text_channel_id": str(text_channel.id),
                            "text_channel_name": text_channel.name
                        })
                return res

            try:
                await self.register(get_channels, "nntin.github.discordwebbridge.server.get_channels_rpc")
                await self.register(send_message, "nntin.github.discordwebbridge.channel.send_message_rpc")
            except autobahn.wamp.exception.ApplicationError as error:
                print("---ERROR---")
                print(error)
                print("-----------")
                sys.exit("Remote Procedure Call could not be registered but is needed.")

        @client.event
        async def on_message(message):
            # todo: filter so only works in select few channels
            if message.author.id == client.user.id:
                payload = {
                    "user": message.embeds[0].author.name,
                    "user_avatar": message.embeds[0].author.icon_url,
                    "content": message.embeds[0].description,
                    "id": message.id,
                    "created_at": datetime_to_string(message.created_at)
                }

            else:
                avatar_url = "https://cdn.discordapp.com/avatars/{user_id}/{avatar_token}".format(
                    user_id=message.author.id,
                    avatar_token=message.author.avatar
                )
                payload = {
                    "user": message.author.display_name,
                    "user_avatar": avatar_url,
                    "content": message.content,
                    "id": message.id,
                    "created_at": datetime_to_string(message.created_at)
                }

            for key, value in payload.items():
                if isinstance(value, _EmptyEmbed):
                    payload[key] = ""

            try:
                self.publish("nntin.github.discordwebbridge.channel.{channel_id}.messages".format(
                    channel_id=message.channel.id
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
    runner = ApplicationRunner(url, realm)
    runner.run(Component)

