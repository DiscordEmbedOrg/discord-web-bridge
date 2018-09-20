import asyncio
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from bot.config import config
from discord.ext.commands import Bot
from discord import Embed
from datetime import datetime
import random
import json

event_loop = asyncio.get_event_loop()
client = Bot(command_prefix=">>")


def datetime_to_string(datetime_object):
    epoch = datetime.utcfromtimestamp(0)
    return (datetime_object - epoch).total_seconds()


class Component(ApplicationSession):
    async def onJoin(self, details):
        @client.event
        async def on_ready():
            def send_message(payload):
                payload = json.loads(payload)

                random.seed(payload["author_name"])
                embed = Embed(colour=random.randint(0, 16777215),
                              description=payload["content"])
                embed.set_author(name=payload["author_name"],
                                 icon_url=payload["author_avatar_url"])

                channel = client.get_channel(payload["channel"])
                event_loop.create_task(channel.send(embed=embed))

                return "nntin"

            await self.register(send_message, "nntin.github.discord-web-bridge.rpc")

        @client.event
        async def on_message(message):
            if message.author.id == client.user.id:
                payload = {
                    "user": message.embeds[0].author.name,
                    "user_avatar": message.embeds[0].author.icon_url,
                    "content": message.embeds[0].description,
                    "id": message.id,
                    "created_at": datetime_to_string(message.created_at)
                }
                print(message.embeds[0].author)
                print(type(message.embeds[0].author))

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

            # self.publish("nntin.github.discord-web-bridge.message", payload)
            self.publish("nntin.github.discord-web-bridge.message.{channel_id}".format(
                channel_id=message.channel.id
            ), json.dumps(payload))

        event_loop.create_task(client.start(config["discord"]["bot_token"], bot=True, reconnect=True))


if __name__ == '__main__':
    url = config["crossbar"]["ws"]
    realm = config["crossbar"]["realm"]
    runner = ApplicationRunner(url, realm)
    runner.run(Component)

