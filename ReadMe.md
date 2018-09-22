# Discord Web Bridge

Connect Discord with your website!

**WIP**: Working towards proof of concept.

## How it works

This project is divided into 3 modules:
- Crossbar router
- Discord bot
- Web

Crossbar router handles the communication between Discord bot and web clients.

Discord bot "publishes" to the crossbar router when a message was posted in a text channel. A web client connects to the crossbar router and "subscribes". Anything that gets published is received by the web client.

When the web client wants to say something he does a Remote Procedure Call. Some information is passed such as username and message. The Discord Bot receives it, processes it and posts a message on behalf of the web client.

## Support

Basic knowledge about maintaining a VPS and working with Python and Node are required.

[![](https://discordapp.com/api/guilds/295528852518731786/embed.png?style=banner2)](https://discord.gg/ZVQywBg)

## Setup

Start Crossbar router. See ReadMe in crossbar folder.  
Start Discord bot. See ReadMe in bot folder.  
Start the web server. See ReadMe in webclient folder.

## TODOs

Basic:

- [x] Create Crossbar router
  - [x] Basic Crossbar router configuration
  - [x] Store message history
- [x] Create the Discord bot
  - [x] OnMessage: Publish to Crossbar
  - [x] OnRPC: Send message
- [x] Create the Website
  - [x] Subscribe to Crossbar
  - [x] OnEvent: visualize message
  - [x] Allow web clients to perform RPC
  - [x] Retrieve message history

Extended:
- [ ] Bot Authentication: Only authenticated Discord Bot can publish to Crossbar router
- [ ] Optional web client authentication: Privileged users with secret token have more power
- [ ] Make it look good: Due to lack of experience on frontend: **Help wanted!**
- [ ] RPC: Get text channels (for multi-text channel support)

## Security and Risks

The Discord Bot will broadcast **all** messages it has access to. If you don't want the message to be broadcasted, take away the read message right for the text channel.  
This means anyone can read those messages if they have the technical know how of talking to my backend.

Anyone who is connected can post a chat message and there is no tracking who did it. There is no verification in place. A spammer could abuse this and send spam messages on behalf of the bot.

I plan on addressing those issues. Just bear in mind they exist when making use of this project which is still in its very early stage.

## Public Bot

I plan on releasing a public bot that supports multiple servers. However for now I am solely focusing on a single server.  
A public bot that allows anyone to chat in any registered server without any form of authentication is at risk of being spammed at.