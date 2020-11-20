import discord
import asyncio
import NaverWeather
import LOL_Total
import Random_Menu
import openpyxl
from discord.ext import commands, tasks
from datetime import datetime
import time
import Random_msg
import kmsg

TOKEN = ''
client = discord.Client()

@client.event
async def on_ready():
    print("Bot is on ready!")
    @tasks.loop(seconds=1)
    async def helping():
        if datetime.now().minute == 0 and datetime.now().second == 0:
            await client.change_presence(activity=discord.Game("굶주려"))
            time.sleep(1)
    helping.start()
    await client.change_presence(activity=discord.Game("수영"))

@client.event
async def on_message(message):
    author = message.author
    #content = message.content
    #channel = message.channel
    if author == client.user:
        return

    if message.content.startswith("$help"):
        embed = discord.Embed(
            title = "상어못 명령어 리스트",
            description = "모든 명령어 앞에는 '$'표시가 있어야합니다.",
            colour = 0x2EFEF7
        )
        embed.add_field(name="ping", value="해당 봇의 지연시간입니다.", inline=False)
        embed.add_field(name="안녕", value="인사하고 싶을 때 하십시오.", inline=False)
        embed.add_field(name="날씨", value="뒤에 지역을 적으면 대한민국(전국) 날씨를 알려줍니다.", inline=False)
        embed.add_field(name="롤", value="뒤에 롤 닉네임을 적으면 해당 유저의 롤 전적을 알려줍니다.", inline=False)
        embed.add_field(name="먹이", value="해당 봇에게 먹이를 줍니다. 굶주림 상태에서 주십시오.", inline=False)
        embed.add_field(name="아쿠아리움", value="해당 봇의 본진을 알려줍니다.", inline=False)
        embed.add_field(name="메뉴추천", value="47개의 메뉴 중 하나를 랜덤으로 추천해줍니다.", inline=False)
        embed.add_field(name="종", value="해당 봇의 종을 알려줍니다.", inline=False)
        embed.add_field(name="능지", value="당신의 능지는?", inline=False)
        embed.add_field(name="소련", value="위대했던 국가의 찬가", inline=False)
        embed.add_field(name="와!", value="샌즈!", inline=False)
        embed.add_field(name="갈고리수집가", value="정수 수집한다", inline=False)
        embed.add_field(name="ㄹㅇㅋㅋ", value="ㄹㅇㅋㅋ", inline=False)
        embed.add_field(name="버그", value="Yes, It's a bug. but also 'Zerg'", inline=False)
        embed.add_field(name="버그제보", value="화염차와 화염기갑병을 보내드리지요.", inline=False)
        embed.add_field(name="난죽택", value="??? : 난 죽음을 택하겠다.", inline=False)
        
        await message.channel.send(embed=embed)

    if message.content.startswith("$ping"):
        await message.channel.send("pong {0}ms".format(int(client.latency * 10000)))

    if message.content.startswith("$안녕"):
        await message.channel.send("안녕하세요 " + "<@{}> 님".format(str(author.id)))
    
    if message.content.startswith("$날씨"):
        weather = NaverWeather.NaverWeather()
        msg = message.content[4:]
        weather.set_keyword(msg + "날씨")
        weather.run()
        r = weather.get_result()
        embed = discord.Embed(title = "현재 " + str(msg) + " 의 날씨", description = "날씨는 위치/시각/날씨 어제보다 비교/현재 온도 순서입니다.", colour = 0x2EFEF7)
        if r['loc'] == None:
            embed.add_field(name="존재하지않는 위치거나 외국입니다.", value=None, inline=False)
            pass
        else:
            embed.add_field(name="해당 위치", value=r['loc'], inline=False)
            embed.add_field(name="시각", value=r['time'], inline=False)
            embed.add_field(name="날씨", value=r['status'], inline=False)
            embed.add_field(name="현재 온도", value=r['degree'], inline=False)
        await message.channel.send(embed=embed)
        
    
    if message.content.startswith("$롤"):
        crawler = LOL_Total.LOL_Total()
        msg = message.content[3:]
        crawler.set_userName(msg)
        crawler.run()
        r = crawler.get_result()

        embed = discord.Embed(
            title = "롤 정보",
            description = str(msg) + "님의 롤 정보입니다.",
            colour = 0x2EFEF7
        )
        if r['Tier'] == None:
            embed.add_field(name = "존재하지않는 롤 닉네임입니다.", value = None, inline=False)
        
        elif r['Tier'].strip() == "Unranked" or r['Tier'] == "Unranked":
            embed.add_field(name = "당신의 티어", value = r['Tier'], inline=False)
            embed.add_field(name = "당신은 언랭", value = "언랭은 더이상의 정보를 제공하지 않습니다.", inline = False)

        else:
            embed.add_field(name = "당신의 티어", value = r['Tier'], inline = False)
            embed.add_field(name = "당신의 LP(점수)", value = r['Score'], inline = False)
            embed.add_field(name = "당신의 승패 정보", value = r['Win'] +" "+r['Lose'], inline = False)
            embed.add_field(name = "당신의 승률", value = r['Odds'], inline = False)
        
        await message.channel.send(embed=embed)

    if message.content.startswith("$메뉴추천"):
        s = Random_Menu.Random_Menu()
        r = s.select()
        embed = discord.Embed(
            title = str(author) + "님에게 추천드립니다.",
            description = "",
            colour = 0x2EFEF7
        )
        embed.add_field(name = "추천 메뉴 : ", value = r + "입니다. 잘 드시길 바랍니다.", inline = False)
        await message.channel.send(embed=embed)

    if message.content.startswith("$아쿠아리움"):
        await message.channel.send("상어 봇의 본진은 '멀티 아쿠아리움'입니다.")

    if message.content.startswith("$종"):
        embed = discord.Embed(
            title = "상어 봇의 모델과 종입니다.",
            description = "상어 봇의 모델과 종은 '백상어리'입니다.",
            colour = 0x2EFEF7
        )
        embed.add_field(name = "모델 특성상 아쿠아리움등에서 키우는 게 불가능합니다.", value = "탈출하려는 경우가 다반수이기에 ", inline=False)
        embed.add_field(name = "하지만 모델이 '백상어리'이지", value = "봇이기에 컨트롤이 가능합니다.", inline=False)
        embed.add_field(name = "특징", value = "자기보다 레벨이 낮다면 잡아먹기도 합니다. (수동)", inline=False)

        await message.channel.send(embed=embed)

    if message.content.startswith("$먹이"):
        s = Random_msg.Random_msg()
        r = s.msg()
        await message.channel.send(str(r))
        await client.change_presence(activity=discord.Game("배불러"))
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game("수영"))

    if message.content.startswith("$능지"):
        await message.channel.send("처참")

    if message.content.startswith("$갈고리수집가"):
        await message.channel.send("<@{}> 님은 갈고리 수집가 칭호를 획득하셨습니다.".format(str(author.id)))

    if message.content.startswith("$와!"):
        await message.channel.send("와! 샌즈! 아시는 구나!")
        
    if message.content.startswith("$소련"):
        await message.channel.send("https://youtu.be/qlwr6FS6K10")
    
    if message.content.startswith("$ㄹㅇㅋㅋ"):
        await message.channel.send("ㄹㅇㅋㅋ")

    if message.content.startswith("$버그"):
        await message.channel.send("대부분이 버그입니다.")

    if message.content.startswith("$버그제보"):
        await message.channel.send("<@654344568111890462>로 DM보내세요 또는 <@691850256622813255>으로 보내세요.")

    if message.content.startswith("$난죽택"):
        s = kmsg.kmsg()
        r = s.msg()
        await message.channel.send(str(r))

    if message.content.startswith("$사냥"):
        msg = message.content[4:]
        await message.channel.send("<@{}> 님은 갈고리 수집가 칭호를 획득하셨습니다.".format(str(msg)))

client.run(TOKEN)
