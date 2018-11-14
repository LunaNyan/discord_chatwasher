#!/usr/env python3
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
 
@client.event
async def on_message(message):
    if message.content.startswith('하우젠 다쓸어버려'):
        tmp = await client.send_message(message.channel, '은나노스팀으로 살균세탁중 >_<')
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)
        await client.send_message(message.channel, '살균세탁 하셨나요 하우젠~♬')

# 토큰은 여기다 싸질러주세요
client.run('?_?')