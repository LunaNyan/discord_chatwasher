#!/usr/env python3
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
 
@client.event
async def on_message(message):
    if message.content.startswith('~세탁'):
        await client.send_message(message.channel, '이쪽 코드는 아직 안 짰음')
    else:
        await client.send_message(message.channel, msg.content)

# 토큰은 여기다 싸질러주세요
client.run('XXXXXXXXXX')

