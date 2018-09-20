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

- [ ] Create Crossbar router
  - [x] Basic Crossbar router configuration
  - [ ] Bot Authentication: Only authenticated Discord Bot can publish to Crossbar router
- [x] Create the Discord bot
  - [x] OnMessage: Publish to Crossbar
  - [x] OnRPC: Send message
- [ ] Create the Website
  - [ ] Subscribe to Crossbar
  - [ ] OnEvent: visualize message
  - [ ] Allow web clients to perform RPC
  - [ ] Make it look good: Due to lack of experience on frontend: **Help wanted!**