#!/usr/bin/python3
import discord
import asyncio

client = discord.Client()

#Strings
#일체형으로 작성해야 하기에 라이센스 전문을 하드코딩합니다
license = '```MIT License\n\n'
license+= 'Copyright (c) 2018 ItsLunaNyan\n\n'
license+= 'Permission is hereby granted, free of charge, to any person obtaining a copy\n'
license+= 'of this software and associated documentation files (the "Software"), to deal\n'
license+= 'in the Software without restriction, including without limitation the rights\n'
license+= 'to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n'
license+= 'copies of the Software, and to permit persons to whom the Software is\n'
license+= 'furnished to do so, subject to the following conditions:\n\n'
license+= 'The above copyright notice and this permission notice shall be included in all\n'
license+= 'copies or substantial portions of the Software.\n\n'
license+= 'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n'
license+= 'IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n'
license+= 'FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n'
license+= 'AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n'
license+= 'LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n'
license+= 'OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n'
license+= 'SOFTWARE.```'

help = '하우젠봇 v' + bot_ver + '\n초대하기 : ' + bot_invite_url + '\n문의는 libertin#2340에 갠챗으로 주시기 바랍니다.\n\n' + help + '\n\n이름의 어원은 ' + hauzen_yt + '에서 착안했습니다.\n\n'
help+= '하우젠봇 명령어 목록\n'
help+= '하우젠 다쓸어버려 : 채널에 있는 메시지를 전부 삭제(세탁)합니다.\n'
help+= '하우젠 도와줘 : 이 도움말을 표시합니다.\n'
help+= '하우젠 라이센스 : 하우젠봇의 라이센스를 표시합니다.\n'
help+= '하우젠 소스코드 : 하우젠봇의 소스코드 주소를 표시합니다.'

source_repo = 'https://github.com/lunanyan/discord_chatwasher'
bot_invite_url = 'https://discordapp.com/oauth2/authorize?client_id=505037489573068800&scope=bot'
hauzen_yt = 'https://www.youtube.com/watch?v=ohU40KhdPtE'

bot_ver = '1.0.0'

@client.event
async def on_ready():
    print('name : ' + client.user.name)
    print('id   : ' + client.user.id)

@client.event
async def on_message(message):
    if message.content.startswith('하우젠 다쓸어버려'):
        tmp = await client.send_message(message.channel, '은나노스팀으로 살균세탁중 >_<')
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)
        await client.send_message(message.channel, '살균세탁 하셨나요 하우젠~♬')
    elif message.content.startswith('하우젠 도와줘'):
        await client.send_message(message.channel, help)
    elif message.content.startswith('하우젠 라이센스'):
        await client.send_message(message.channel, license)
    elif message.content.startswith('하우젠 소스코드'):
        await client.send_message(message.channel, source_repo)

# 토큰은 여기다 싸질러주세요
client.run('?_?')
