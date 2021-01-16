import discord
import random
import requests
import os


class chatbot(discord.Client):

    async def on_ready(self):
        game = discord.Game("하루하루의 추억을 수집")

        await client.change_presence(status=discord.Status.online, activity=game)

        print("BOT IS READY")
        print("Logged in as ")
        print(client.user.name)
        print(client.user.id)
        print("=========================")
        print("다음으로 로그인 합니다 : ")
        print(client.user.name)
        print("connection was successful")
        print("=========================")

    async def on_message(self, message):
        if message.author.bot:
            return None

        if message.content == "!정보봇":
            channel = message.channel
            msg = "**안녕하세요 로우패밀리 정보봇입니다**  :robot:"
            await channel.send(msg)
            msg = "`!정보봇 도움말 을 입력하셔서 도움말을 확인 하실 수 있습니다`"
            await channel.send(msg)
            return None
        
        if message.content == "!정보봇 도움말":
            channel = message.channel
            embed = discord.Embed(title="**로우패밀리 정보봇**  :robot:", description="정보봇 도움말입니다.", color=0xFFBB00)
            embed.add_field(name="명령어 리스트", value="`!정보봇 안녕`, `!정보봇 바보`, `!정보봇 핑`, `!정보봇 리스트`, `!정보봇 무작위엽사`", inline=True)
            embed.set_footer(text="개발자 : 옥동자")
            embed.set_thumbnail(url="https://i.esdrop.com/d/JN7gwn39DI.jpg")
            await message.channel.send("**로우패밀리 정보봇이 도움말을 펼쳤습니다.**", embed=embed)
            return None

        if message.content == "!정보봇 안녕":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description="안녕하세요 :)", color=0xFFBB00)
            embed.set_image(url="https://i.esdrop.com/d/j1v8KDdbV0.jpg")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 김경빈":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description="김경빈님의 프로필", color=0xFFBB00)
            embed.add_field(name="이름", value="김경빈", inline=False)
            embed.add_field(name="롤 닉네임", value="주혁이꼬튜99센티", inline=False)
            embed.add_field(name="특기", value="축구, 똥 싸기, 가렌 내려찍기, 바리깡으로 삭발", inline=False)
            embed.add_field(name="별명", value="게이삭발, 삭발게이, 삭발, BJ고경자, 고경자, 병신", inline=False)
            embed.add_field(name="롤 관련사항", value="가렌, 말파이트, 오른과 같은 탱커만 사용하는 탱커충", inline=False)
            embed.add_field(name="특이사항", value="https://youtu.be/T5oVRMSGhwg 을 보면 알 수 있음.", inline=False)
            embed.set_image(url="https://i.esdrop.com/d/UzLRR9mJsB.jpg")
            embed.set_footer(text="(위 사진은 김경빈의 대표사진 입니다.)")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 이동현":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description="이동현님의 프로필", color=0xFFBB00)
            embed.add_field(name="이름", value="이동현", inline=False)
            embed.add_field(name="롤 닉네임", value="옥동자맛있어, DARKNESSSPACE(삭제 된 계정)", inline=False)
            embed.add_field(name="특기", value="잉여짓, 코딩, 마크, 아리로 킬딸해서 펜타킬하기", inline=False)
            embed.add_field(name="별명", value="나무늘보, 노인정, 아이번, 옥동자, 아리충", inline=False)
            embed.add_field(name="롤 관련사항", value="원래는 DARKNESSSPACE라는 계정을 사용하였으나, 자신이 원챔으로 사용하던 아리 1ㄷ1을 이준서에게 패배하며 현타가 와 충동적으로 아리 올스킨인 해당 계정을 삭제함. 그리고 몇주 뒤 옥동자맛있어라는 계정을 새로 생성. 아리 원챔이며, 가끔씩 제드나 요네 등 질릴 때마다 재밌는 걸 찾아봄", inline=False)
            embed.add_field(name="특이사항", value="로우패밀리 정보봇을 창조한 창조주임. 결론적으로 완벽남 (?????)", inline=False)
            embed.set_image(url="https://i.esdrop.com/d/uoHzJHINss.jpg")
            embed.set_footer(text="(위 사진은 이동현의 대표사진 입니다.)")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 김태연":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description="김태연님의 프로필", color=0xFFBB00)
            embed.add_field(name="이름", value="김태연", inline=False)
            embed.add_field(name="롤 닉네임", value="아임불주먹", inline=False)
            embed.add_field(name="특기", value="농구 할 때 은근슬쩍 빠지기, 롤 레벨링, 살 찌우기", inline=False)
            embed.add_field(name="별명", value="로아랍", inline=False)
            embed.add_field(name="롤 관련사항", value="과거엔 아칼리를 원챔 삼아 하였지만 요즘은 에코, 블리츠크랭크 등 여러 챔프를 많이 사용 중임.", inline=False)
            embed.add_field(name="특이사항", value="유일하게 별명이 한개인 애임.", inline=False)
            embed.set_image(url="https://i.esdrop.com/d/JN7gwn39DI.jpg")
            embed.set_footer(text="(위 사진은 김태연의 대표사진 입니다.)")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 김연성":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description="김연성님의 프로필", color=0xFFBB00)
            embed.add_field(name="이름", value="김연성", inline=False)
            embed.add_field(name="롤 닉네임", value="부평구스타", inline=False)
            embed.add_field(name="특기", value="잘생긴 척, 귀여운 척, 착한 척", inline=False)
            embed.add_field(name="별명", value="꿀벌, 왕눈이", inline=False)
            embed.add_field(name="롤 관련사항", value="로우패밀리 롤 세계관 최약체", inline=False)
            embed.add_field(name="특이사항", value="눈이 대따 큼", inline=False)
            embed.set_image(url="https://i.esdrop.com/d/77cnQbVxGj.jpg")
            embed.set_footer(text="(위 사진은 김연성의 대표사진 입니다.)")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 김유민":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description="김유민님의 프로필", color=0xFFBB00)
            embed.add_field(name="이름", value="김유민", inline=False)
            embed.add_field(name="롤 닉네임", value="악다아아아앙", inline=False)
            embed.add_field(name="특기", value="코딩, 교정기 청소, 치과 가기", inline=False)
            embed.add_field(name="별명", value="교정기, 교딱, 교정기딱딱, 교정기사우르스, 엽사 생성기 1호", inline=False)
            embed.add_field(name="롤 관련사항", value="사용중인 롤 계정이 최은서가 준 계정임. 가끔씩 대리 논란이 터지기도 함", inline=False)
            embed.add_field(name="특이사항", value="디스코드 방장임. 세계관 최강자", inline=False)
            embed.set_image(url="https://i.esdrop.com/d/O2Tk01MuKn.jpg")
            embed.set_footer(text="(위 사진은 김유민의 대표사진 입니다.)")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 이준아":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description="이준아님의 프로필", color=0xFFBB00)
            embed.add_field(name="이름", value="이준아", inline=False)
            embed.add_field(name="롤 닉네임", value="롤 사용 X", inline=False)
            embed.add_field(name="특기", value="어묵장사, 태세변환, 피파, 오징어짬뽕 같이 생긴 놈, 옵치 브론즈", inline=False)
            embed.add_field(name="별명", value="어묵, 어묵장사, 서울역 2번출구 어묵장사 하시는 분, 일본인", inline=False)
            embed.add_field(name="롤 관련사항", value="롤 사용 X", inline=False)
            embed.add_field(name="특이사항", value="이동현의 폭로로 인해 원래는 없던 별명이 생김. 그 별명은 아직까지도 회자되는 중", inline=False)
            embed.set_image(url="https://i.esdrop.com/d/i1kW00QEhA.jpg")
            embed.set_footer(text="(위 사진은 이준아의 대표사진 입니다.)")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 이준서":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description="이준서님의 프로필", color=0xFFBB00)
            embed.add_field(name="이름", value="이준서", inline=False)
            embed.add_field(name="롤 닉네임", value="다사태사, 악다아앙", inline=False)
            embed.add_field(name="특기", value="구기운동, 야스오로 펜타킬 할 뻔 하기, 이동현 놀리기", inline=False)
            embed.add_field(name="별명", value="이집트인, 과학, 달리기 :arrow_heading_up: 선수 :arrow_upper_right:", inline=False)
            embed.add_field(name="롤 관련사항", value="사실상 야스오 원챔 유저. 뭔가 있어보이려고 피지컬 챔만 사용하려는 강박이 있음. 또한 현재 본계정으로 사용 중인 다사태사라는 닉네임은 다예사랑 태민사랑 이라는 뜻을 줄여서 만든 것이며, 이 계정이 본계정이 된 이유는 이 계정에 어둠의 인도자 야스오가 뽑혔기 때문임.", inline=False)
            embed.add_field(name="특이사항", value="자칭 세계최고 미남이자 자신은 뭐든 할 수 있다고 자만하며 착각에 빠져 사는 중.", inline=False)
            embed.set_image(url="https://i.esdrop.com/d/5jO0wmLWU7.jpg")
            embed.set_footer(text="(위 사진은 이준서의 대표사진 입니다.)")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 유민선":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description="유민선님의 프로필", color=0xFFBB00)
            embed.add_field(name="이름", value="유민선", inline=False)
            embed.add_field(name="롤 닉네임", value="내스피커고오급, 이름보고서서렌침", inline=False)
            embed.add_field(name="특기", value="구기운동, 펜타킬 뺏기, 유태준 놀리기", inline=False)
            embed.add_field(name="별명", value="중국인, 로만동, 로만동뱃살통통통, 로배통, 상빵, 상빵 싱싱뽀까 만찌깡, 마오쩌동, 태준 남자친구 :heart:, 강차남", inline=False)
            embed.add_field(name="롤 관련사항", value="원래는 FIFA충이라는 형과 함께 쓰는 계정을 사용했지만 현재는 내스피커고오급이라는 본인의 독자적인 계정을 사용중임. 또한 이름보고서서렌침이라는 부부계정이 있으며 로팸 애들 사이에서 가장 많은 계정을 소유하고 있음. 모스트 챔프는 볼리베어, 헤카림 등 정글챔들을 주로 사용함.", inline=False)
            embed.add_field(name="특이사항", value="자신이 만든 별명이 많은 만큼 로팸 애들 사이에서 가장 많은 별명을 소유하고 있음. 대표적으로 중국인, 상빵 등이 있으며 특히 상빵은 애들 사이에서 가장 많이 회자되는 별명임.", inline=False)
            embed.set_image(url="https://i.esdrop.com/d/WbTtqxKRXa.jpg")
            embed.set_footer(text="(위 사진은 유민선의 대표사진 입니다.)")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 유태준":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description="유태준님의 프로필", color=0xFFBB00)
            embed.add_field(name="이름", value="유태준", inline=False)
            embed.add_field(name="롤 닉네임", value="ASlientSword, 사회의악 세트", inline=False)
            embed.add_field(name="특기", value="햄버거 먹기, 유민선 놀리기, 상빵 외치기", inline=False)
            embed.add_field(name="별명", value="햄붝, 햄버거, 햄, 함바이, 햄태식이, 함바이 하실래예? 씨입:arrow_heading_up:덕, 민선 여자친구 :heart:, 미국인, 쪽갈비, 햄틀러", inline=False)
            embed.add_field(name="롤 관련사항", value="ASlientSword 라는 계정을 먼저 사용하다가 셧다운제로 인해 사회의악 세트라는 부계정을 파게 됨. 원래는 요네 원챔이였으나 요네가 떡락 한 후 가끔씩 쓰는 모습을 보였으며 어느 순간부터 세트가 주챔이 되었음.", inline=False)
            embed.add_field(name="특이사항", value="씨입:arrow_heading_up:덕을 제외한 대부분의 별명이 음식에서부터 시작됨. 과거엔 잠시동안 쪽갈비였으며 그에 대한 이유는 유태준 본인이 가장 좋아하는 음식이 쪽갈비였다고 발언 한 적이 있었기 때문임. 또한 현재 통용되고 있는 햄버거라는 별명은 유민선이 지어줬다는 거 외에 밝혀진 바가 없음. 아마 유민선은 알듯 함.", inline=False)
            embed.set_image(url="https://i.esdrop.com/d/1blGUzhBqr.jpg")
            embed.set_footer(text="(위 사진은 유태준의 대표사진 입니다.)")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 최하린":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description="최하린님의 프로필", color=0xFFBB00)
            embed.add_field(name="이름", value="최하린", inline=False)
            embed.add_field(name="롤 닉네임", value="BRGSharin, SiroFanDeath", inline=False)
            embed.add_field(name="특기", value="엽사 만들기, 시로 덕질하기, 태주 놀리기, 별명 만들기", inline=False)
            embed.add_field(name="별명", value="엽사 생성기 2호, 부랄지에스, 경주", inline=False)
            embed.add_field(name="롤 관련사항", value="쓰레쉬, 파이크 같은 서폿챔 모스트 유저였지만 현재는 원딜 이즈리얼로 갈아탄 케이스다. 중간중간에 미드챔프들도 해보고 미드라인도 뛰어봤지만 역시 얘는 바텀 성향인가 봄. 사실상 세라핀 제외 모든 서폿챔프들을 해본 로팸 애들 사이에선 극히 드문 유저.", inline=False)
            embed.add_field(name="특이사항", value="로우패밀리에서 유통되는 엽사들의 70퍼센트 이상의 지분을 가지고 있는 엽사의 왕임. 레전드 히트짤으로는 포비태주, 저는 어장을 했습니다, 초능력자 요리왕 유민선 등이 있음.", inline=False)
            embed.set_image(url="https://i.esdrop.com/d/Cdrsop5uMw.jpg")
            embed.set_footer(text="(위 사진은 최하린의 대표사진 입니다.)")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 최은서":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description="최은서님의 프로필", color=0xFFBB00)
            embed.add_field(name="이름", value="최은서", inline=False)
            embed.add_field(name="롤 닉네임", value="악다아아앙", inline=False)
            embed.add_field(name="특기", value="독재자 인척 하기, 태주 놀리기, 시비걸기, 말도 안돼는 챔프로 정글링 하기", inline=False)
            embed.add_field(name="별명", value="이준서 바라기, 이준서 따갈, (전) 이준서 여자친구", inline=False)
            embed.add_field(name="롤 관련사항", value="로우패밀리 역사 상 지금껏 일겜에서 가장 많은 이상한 짓을 함. 특히 바위처럼 단단하게와, 아칼리 정글 등이 있음.", inline=False)
            embed.add_field(name="특이사항", value="로우패밀리에서 일어나는 싸움의 80퍼센트 정도의 지분을 가지고 있음. 그야말로 싸움의 왕 세트. 개인적으로 최은서가 유태준의 모스트챔프인 세트를 뺏고 주챔으로 기용하였으면 좋겠다는 생각이 듬 (???)", inline=False)
            embed.set_image(url="https://i.esdrop.com/d/sgo51QhQ68.jpg")
            embed.set_footer(text="(위 사진은 최은서의 대표사진 입니다.)")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 김현진":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description="김현진님의 프로필", color=0xFFBB00)
            embed.add_field(name="이름", value="김현진", inline=False)
            embed.add_field(name="롤 닉네임", value="거스윌스킴", inline=False)
            embed.add_field(name="특기", value="반에서 왕따되기, 축구, 자뻑", inline=False)
            embed.add_field(name="별명", value="호주인, 찐따, 안젤리나 졸리 남친, 호주핑, 코알라", inline=False)
            embed.add_field(name="롤 관련사항", value="로팸 애들 중에서 가장 챔프폭이 넓음. 넓은 만큼 특별하게 잘하는 챔프는 딱히 찾아보기 어려우며 과거엔 람머스를 많이 사용했음. 또한 유일하게 로팸 애들 중 롤에 현질을 안 한 인물임. 이유는 문상 사용법을 몰라서다.", inline=False)
            embed.add_field(name="특이사항", value="호주 유학중임. 근데 웃긴건 호주에서 게임을 10시간 씩 해댐.", inline=False)
            embed.set_image(url="https://i.esdrop.com/d/ojfbfnub92.png")
            embed.set_footer(text="(위 사진은 김현진의 대표사진 입니다.)")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 서태민":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description="서태민님의 프로필", color=0xFFBB00)
            embed.add_field(name="이름", value="서태민", inline=False)
            embed.add_field(name="롤 닉네임", value="축구좋아07", inline=False)
            embed.add_field(name="특기", value="턱점 케어 받기, 축구", inline=False)
            embed.add_field(name="별명", value="턱점, 서턱점, 턱다예, 소다예", inline=False)
            embed.add_field(name="롤 관련사항", value="축구좋아07이라는 닉네임은 서태민 본인이 직접 지은 닉네임이며 이 닉네임의 초딩스러움으로 인해 로팸 애들에게 두고두고 회자되며 놀림거리가 되는 부분이다. 부계정으로는 zedonetop99라는 닉네임을 가진 계정이 있었는데, 현재는 찾아 볼 수 없다. 예전엔 야스오가 모스트 챔프였지만 현재는 제드와 에코로 변하였다", inline=False)
            embed.add_field(name="특이사항", value="턱에 점이 있어서 턱점이라는 별명으로 통한다", inline=False)
            embed.set_image(url="https://i.esdrop.com/d/TyAbcSvH5M.jpg")
            embed.set_footer(text="(위 사진은 서태민의 대표사진 입니다.)")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 진은석":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description="진은석님의 프로필", color=0xFFBB00)
            embed.add_field(name="이름", value="진은석", inline=False)
            embed.add_field(name="롤 닉네임", value="민트자비자비", inline=False)
            embed.add_field(name="특기", value="양궁, 민트자비자비 챌린지", inline=False)
            embed.add_field(name="별명", value="(전) 유민선 여자친구 :smiling_face_with_3_hearts:, 민트작비, 민트자비 좀, 민작", inline=False)
            embed.add_field(name="롤 관련사항", value="지가 롤 잘하는 줄 앎 :angry:", inline=False)
            embed.add_field(name="특이사항", value="이정규와 교제 중 :heart:", inline=False)
            embed.set_image(url="https://i.esdrop.com/d/eY4jdfM0hY.jpg")
            embed.set_footer(text="(위 사진은 진은석의 대표사진 입니다.)")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 바보":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description="짜증나게 하지 마세요 ㅡ.,ㅡ", color=0xFFBB00)
            embed.set_image(url="https://i.esdrop.com/d/xjEAlxDYNU.jpg")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 핑":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='현재 핑은 ' + str(client.latency) + 'ms 입니다. :ping_pong:', color=0xFFBB00)
            embed.set_thumbnail(url="https://i.esdrop.com/d/DehiZjIv5k.jpg")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 리스트":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='로우패밀리의 정보 리스트입니다.', color=0xFFBB00)
            embed.add_field(name="기본프로필", value="`!정보봇 이동현`, `!정보봇 김경빈`, `!정보봇 김태연`, `!정보봇 김연성`, `!정보봇 김유민`, `!정보봇 이준아`, `!정보봇 이준서`, `!정보봇 유민선`, `!정보봇 유태준`, `!정보봇 최하린`, `!정보봇 최은서`, `!정보봇 김현진`, `!정보봇 진은석`, `!정보봇 서태민`", inline=False)
            embed.add_field(name="다메다네", value="`!정보봇 다메다네 태준`, `!정보봇 다메다네 태연`, `!정보봇 다메다네 준서`, `!정보봇 다메다네 태민`", inline=False)
            embed.set_image(url="https://i.esdrop.com/d/X4z5kvhxww.jpg")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 다메다네 태준":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='다메다네 카테고리 : `태준`', color=0xFFBB00)
            embed.set_image(url="https://i.esdrop.com/d/mrmwCscmyl.gif")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 다메다네 태연":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='다메다네 카테고리 : `태연`', color=0xFFBB00)
            embed.set_image(url="https://i.esdrop.com/d/3V6CIlTMtm.gif")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 다메다네 준서":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='다메다네 카테고리 : `준서`', color=0xFFBB00)
            embed.set_image(url="https://i.esdrop.com/d/lIDpy3sDiP.gif")
            await message.channel.send(embed=embed)
            return None

        if message.content == "!정보봇 다메다네 태민":
            channel = message.channel
            embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='다메다네 카테고리 : `태민`', color=0xFFBB00)
            embed.set_image(url="https://i.esdrop.com/d/bQ1l96ctNH.gif")
            await message.channel.send(embed=embed)
            return None
        
        if message.content == "!정보봇 무작위엽사":
            bot_response = random.randint(1, 46)
            if bot_response == 1:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/pSuyPA25G4.gif")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 2:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/j1v8KDdbV0.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 3:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/xjEAlxDYNU.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 4:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/DehiZjIv5k.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 5:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/UzLRR9mJsB.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 6:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/sgo51QhQ68.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 7:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/FbI92KWoC2.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 8:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/L5VBp2RlGN.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 9:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/eY4jdfM0hY.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 10:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/fDdSAdxcUF.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 11:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/22kxnLwZMa.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 12:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/AWOpfFqw4q.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 13:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/RAsDSs7Krx.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 14:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/ouBlLVbR6R.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 15:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/lTZT3EApCh.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 16:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/zIyyqyGmFJ.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 17:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/ar7qekk1ge.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 18:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/XQFEBoZdTu.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 19:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/uGSmFRUfM1.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 20:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/HowVgAO24V.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 21:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/ONa0T30Arl.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 21:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/7mhsMf4SeC.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 22:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/h8La4etqB9.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 23:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/51pnsMonn3.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 24:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/CjJW6GeLgO.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 25:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/TeW1CtDeTZ.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 26:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/qy4tGWJgLG.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 27:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/ngdcham33b.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 28:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/1blGUzhBqr.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 29:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/1blGUzhBqr.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 30:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/c5PYNlXTdy.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 31:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/ZYtL5pRrBS.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 32:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/wDButSMFni.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 33:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/J2Zd7AyMfK.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 34:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/9A8ZHgrh1v.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 35:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/yTSwWNbCqW.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 36:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/EIw6OHBUdm.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 37:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/GGMO8bfNZ4.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 38:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/Mop2a0U7SP.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 39:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/R1Csn14zv8.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 40:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/ojfbfnub92.png")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 41:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/peP8vheHmT.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 42:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/doeE2JfJl0.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 43:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/LF5r1PkvJt.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 44:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/fNmmpwVQYU.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 45:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/DTMDKC8k0Q.jpg")
                await message.channel.send(embed=embed)
                return None
            if bot_response == 46:
                channel = message.channel
                embed = discord.Embed(title="로우패밀리 정보봇  :robot:", description='무작위로 엽사를 전송하였습니다. :laughing:', color=0xFFBB00)
                embed.set_image(url="https://i.esdrop.com/d/X4z5kvhxww.jpg")
                await message.channel.send(embed=embed)
                return None

if __name__ == "__main__":
    client = chatbot()
    acess_token - os.environ["BOT_TOKEN"]
    client.run("acess_token")
