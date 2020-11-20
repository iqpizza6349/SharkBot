import discord
import asyncio
import random

import sell_msg

TOKEN = ''
client = discord.Client()

@client.event
async def on_ready():
    print("Hoi, i'm Temmie!\n")

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    #message.content = 메시지 확인
    send = message.channel.send
    #message.channel.send = 메시지 보내기
    if author == client.user:
        pass

    if content.startswith("*help"):
        await send("안뇽!!(ㅓ어아!!) 나는 테미얌!")
        color = random.randrange(1, 2)
        if (color == 1):
            color = 0x82EEFD
        else:
            color = 0xFFFF00

        embed = discord.Embed(
            title = "명령어ㅓ리스트ㅡ!!",
            descrition = "모든 명령어 앞에는 '*'이 필요해ㅐ!!!",
            colour = color
        )
        embed.add_field(name = "ping", value = "`너의 핑이얗!`", inline=False)
        embed.add_field(name = "산다", value = "`테미 샵으로 가바!`", inline=False)
        embed.add_field(name = "판다", value = "`흥정은 안 합니다!`", inline=False)
        embed.add_field(name = "대화하기", value = "`테ㅔ미와 대화하자ㅏ`", inline=False)
        embed.add_field(name = "몰살", value = "`인간. 이일을 후회하게 해주자`", inline=False)
        embed.add_field(name = "두드러기", value = "`호엑!`", inline=False)
        embed.add_field(name = "몸자랑", value = "`아론`", inline=False)
        embed.add_field(name = "테미플레이크", value = "`간식⁉`", inline=False)
        embed.add_field(name = "밥", value = "`구리고 요긴 내 틘구...`", inline=False)
        embed.add_field(name = "대학등록금", value = "`테미..대학 갈 꼬다!`", inline=False)
        embed.add_field(name = "자랑스러운부모", value = "`테미.. 자랑스런 부모얏!`", inline=False)
        embed.add_field(name = "테미갑빠", value = "`비싼 갑빠옷!`", inline=False)
        embed.add_field(name = "버그제보", value = "`너의 핑이얗!(버그)`", inline=False)
        embed.add_field(name = "샌즈 or 팝 or 파피루스 or 해골", value = "`해골들`", inline=False)
        embed.add_field(name = "도둑", value = "`소총을 들어라`", inline=False)
        embed.add_field(name = "copyright or author or 개발자", value = "`개발자`", inline=False)
        embed.add_field(name = "테미생일", value = "`테미의 태어난 날!!`", inline=False)
        embed.add_field(name = "나가기", value = "`테미봇을 끄는 명령어는 아닙니다.`", inline=False)

        await send(embed=embed)

    if content.startswith("*ping"):
        ping = int(client.latency * 10000)
        await send("너의 핑은 {}ms이야!".format(ping))
        if ping >= 200:
            await send("너무ㅡ 느려ㅓ!!")
    
    if content.startswith("*안녕"):
        coice = random.randint(1,2)
        if coice == 1:
            await send("안뇽!")
        else:
            await send("Hoi!")
    
    if content.startswith("*산다"):
        buy_item = str(content[4:])
        color = random.randrange(1, 2)
        if (color == 1):
            color = 0x82EEFD
        else:
            color = 0xFFFF00
        if (buy_item == "물품"):
            await send("안뇽! 여기는.. 테미 샵이얗!")
            embed = discord.Embed(
                title = "*TEMSHOP",
                description = "구매 목록들",
                colour = color
            )
            embed.add_field(name="`3G - 템 플레이크`", value="[80%확률로 구매한다]", inline=False)
            embed.add_field(name="`1G - 템 플레이크 (할인)`", value="[90%확률로 구매한다]", inline=False)
            embed.add_field(name="`20G - 템 플레이크 (비쌈!)`", value="[60%확률로 구매한다]", inline=False)
            embed.add_field(name="`10000G - 대하꾜등록금`", value="[20%확률로 구매한다]", inline=False)
            embed.add_field(name="`7000G - 테미갑빠옷!!!`", value="[1%확률로 구매한다]", inline=False)
            await send(embed=embed)
        
        elif (buy_item == "템 플레이크 3G"):
            can = random.randrange(10)
            if (can >= 3):
                await send("사줘서 고마어!")
            else:
                await send("너 돈 ㅇ벗어.")
        
        elif (buy_item == "템 플레이크 1G"):
            can = random.randrange(10)
            if (can >= 2):
                await send("사줘서 고마어!")
            else:
                await send("너 돈 ㅇ벗어.")
        
        elif (buy_item == "템 플레이크 20G"):
            can = random.randrange(10)
            if (can >= 5):
                await send("사줘서 고마어!")
            else:
                await send("너 돈 ㅇ벗어.")

        elif (buy_item == "대하꾜등록금 10000G"):
            can = random.randrange(10)
            if (can >= 9):
                await send("사줘서 고마어!")
            else:
                await send("너 돈 ㅇ벗어.")

        elif (buy_item == "테미갑빠옷!!! 7000G"):
            can = random.randrange(100)
            if (can == 99):
                await send("<@{}>님 잭팟!".format(str(author.id)))
                await send("사줘서 고마어!")
            if (can == 98):
                await send("<@{}>님 잭팟!".format(str(author.id)))
                await send("사줘서 고마어!")
            if (can == 97):
                await send("<@{}>님 잭팟!".format(str(author.id)))
                await send("사줘서 고마어!")
            if (can == 96):
                await send("<@{}>님 잭팟!".format(str(author.id)))
                await send("사줘서 고마어!")
            if (can == 95):
                await send("<@{}>님 잭팟!".format(str(author.id)))
                await send("사줘서 고마어!")
            else:
                await send("너 돈 ㅇ벗어.")

        else:
            await send("안뇽! 여기는.. 테미 샵이얗!")
            await send("물품 보는 방식은 `*산다 물품`")
            await send("구매 방식은 `*산다 (물품 가격)`")
            await send("구매 아이템의 설명을 보는 방식은 `*설명 (물품 가격)`")

    if content.startswith("*설명"):
        item_type = str(content[4:])
        if (item_type == "템 플레이크 3G"):
            await send("2HP 회복 테미바ㅃ")
        elif (item_type == "템 플레이크 1G"):
            await send("2HP 회복 테미바ㅃ 할인 중!!!")
        elif (item_type == "템 플레이크 20G"):
            await send("2HP 회복 테미바ㅃ (비싸오)")
        elif (item_type == "대하꾜등록금 10000G"):
            await send("대학교 테미가 더 공부하도록 돕는다")
        elif (item_type == "테미갑빠옷!!! 7000G"):
            await send("갑옷 20DF\n전투를 너무 쉽게 만들어 준다.")
        else:
            await send("구매 아이템의 설명을 보는 방식은 `*설명 (물품 가격)`")

    if content.startswith("*판다"):
        s = sell_msg.sell()
        r = s.msg()
        await send("{}를 팔았다!\n사져서 고마어!".format(str(r)))

    if content.startswith("*대화하기"):
        msg_type = str(content[6:])
        if (msg_type == "인사하기"):
            await send("안뇽!!! \n 나는 테미에오!!")
        elif (msg_type == "자기소개"):
            await send("안뇽!!! \n 나는 테미에오!!")
        elif (msg_type == "테미의역사"):
            await send("우리 테미 력사 짱기퍼!!!")
        elif (msg_type == "가게에관해"):
            await send("구랭구랭 \n 테미샵 가바!")
        elif (msg_type == "테미갑옷에대해"):
            await send("테미 갑옷 넘 조아오!\n누구랑 싸오도!\n쉽게 이교오!")
            await send("긍데 후우우우움,\n테미 생각에능요...갑옷 까묜요, 싸움이 넘 시어서 잼 없어질거가타오...")
            await send("긍데, 테미...\n조은 생각 이또!")
            await send("테미가...\n**장학금 주께!**")
            await send("만약 **쌈에서 많이 지묜,** 테미가 가격을 **까까줄꼐효**!")
            await send("구래섭 덩말 어려운 싸움에서 도저히 못 깰 거 가트면, 마듸막 수단으루 테미 갑옷을 사는 고양.")
            await send("근데 테미 갑옷 넘 죠아.\n꼭 피료할 때만 살 꼬라궁 약소캐줘.")
        elif (msg_type == "테미의역사2"):
            await send("구랭구랭!\n테미가 테미학에서 학위 받아써!\n이제 테미가 테미의 깊픈 력사 말해쥴 수 이써!!!")
        else:
            await send("`대화하기` 뒤ㅜ에 (5가지 중 하나를 덧붙여서 말해줘ㅓ)")
            await send("`(인사하기/자기소개/테미의역사/가게에관해/테미갑옷에대해/테미의역사2`")
            await send("예를 들면 `*대화하기 인사하기`처럼!")

    if content.startswith("*몰살"):
        await send("테미ㅣ 친구 ㅇ벗어")

    if content.startswith("*두드러기"):
        await send("호엑!")

    if content.startswith("*몸자랑"):
        await send("안대!!!!! 근육웅.. 안 기여어ㅓ!!!!")

    if content.startswith("*테미플레이크"):
        await send("머글꺼!!")

    if content.startswith("*대학등록금"):
        await send("*호엑!! ㄸ..떼미가 그렇게 킁 돈 받이도 되는 고까?")

    if content.startswith("*밥"):
        await send("안녕")
        await send("난 밥이야.")

    if content.startswith("*자랑스러운부모"):
        await send("테미... 달걀 본다!")
        await send("달걀... 부화햇!")
        await send("테미... 자랑스런 부모얏!")
        await send("(삶은 달걀이다)")

    if content.startswith("*테미갑빠"):
        await send("테미 갑빠옷!")

    if content.startswith("*버그제보"):
        await send("개발자한테 dm보내주세요ㅕ.")

    if content.startswith("*샌즈"):
        await send("인간 기여ㅕ 해골 안 기여ㅕ")
    
    if content.startswith("*팝"):
        await send("인간 기여ㅕ 해골 안 기여ㅕ")
    
    if content.startswith("*파피루스"):
        await send("인간 기여ㅕ 해골 안 기여ㅕ")
    
    if content.startswith("*해골"):
        await send("인간 기여ㅕ 해골 안 기여ㅕ")

    if content.startswith("*도둑"):
        await send("인간. 자네 죽고 싶나?")
    
    if content.startswith("*copyright"):
        await send("`(c) 2020 IQPIZZA6349#8983. All rights reserved.`")
    
    if content.startswith("*author"):
        await send("`(c) 2020 IQPIZZA6349#8983. All rights reserved.`")

    if content.startswith("*개발자"):
        await send("`(c) 2020 IQPIZZA6349#8983. All rights reserved.`")

    if content.startswith("*테미생일"):
        await send("본체 생일 : 1993년 4월 3일. 테미의 생일 : 2015년 9월 15일.")
    
    if content.startswith("*나가기"):
        await send("ㅃㅑㅃㅑ이!!")
    
    if content.startswith("*토비"):
        await send("My friend Toby Fox!")
        
    if content.startswith("*삭제"):
        await send("안돼ㅐㅐㅐㅐㅐㅐㅐ")
        
            
client.run(TOKEN)
