#!/usr/bin/python3
import discord
import asyncio
import os

client = discord.Client()

#Strings
bot_ver = '1.1.2-final'

bot_changelog = "```v1.1.2-final (2019-07-29)\n"
bot_changelog+= "- 동작 기능 개선\n"
bot_changelog+= "v1.1.0 (2019-07-12)\n"
bot_changelog+= "- 도움말 기능 개선\n"
bot_changelog+= 'v1.0.4 (2019-07-10)\n'
bot_changelog+= '- 봇 동작 안정화\n'
bot_changelog+= 'v1.0.3a (2019-03-19)\n'
bot_changelog+= '- 봇 초대코드 수정\n'
bot_changelog+= 'v1.0.3 (2019-03-19)\n'
bot_changelog+= '- 서버 개수 카운터 추가\n'
bot_changelog+= '```'

@client.event
async def bgjob_change_playing():
    while True:
        members_sum = 0
        for s in client.guilds:
            members_sum += len(s.members)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game('하우젠 도와줘 → 도움말'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game('v' + bot_ver))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(str(len(client.guilds)) + '개의 서버에서 동작중'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(str(members_sum) + '명의 유저들과 함께하는 중'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game('이 메시지는 10초 마다 바뀌어요!'))

@client.event
async def on_ready():
    print('name    : ' + client.user.name)
    print('id      : ' + str(client.user.id))
    print('version : ' + bot_ver)
    client.loop.create_task(bgjob_change_playing())

@client.event
async def on_message(message):
    if message.content.startswith('하우젠 청소해'):
        if message.author.guild_permissions.administrator:
            await message.channel.send('은나노스팀으로 살균세탁중 >_<')
            try:
                async for msg in message.channel.history(limit=200):
                    await msg.delete()
                await message.channel.send('살균세탁 하셨나요 하우젠~♬')
            except:
                await message.channel.send('메시지 관리 권한이 없습니다')
        else:
            await message.channel.send('관리자 권한을 소유하고 있지 않습니다.')
    elif message.content.startswith('하우젠 도와줘'):
        embed=discord.Embed(title="세탁기봇을 초대해주셔서 감사합니다!", description="[민원창구](https://discordapp.com/invite/yyS9x5V) [봇 초대하기](https://discordapp.com/oauth2/authorize/?permissions=75776&scope=bot&client_id=505037489573068800) [이름 유래](https://www.youtube.com/watch?v=ohU40KhdPtE)", color=0xff0080)
        embed.add_field(name="도움말", value="하우젠 도와줘, 하우젠 업데이트내역", inline=False)
        embed.add_field(name="하우젠 청소해", value="채널에 있는 모든 메시지를 지웁니다 (서버 관리자만 가능)", inline=False)
        embed.set_footer(text="Copyright (C) 2018 - 2019 libertin | v" + bot_ver)
        await message.channel.send(embed=embed)
    elif message.content.startswith('하우젠 업데이트내역'):
        await message.channel.send(bot_changelog)

# 토큰은 여기다 싸질러주세요
client.run('')
