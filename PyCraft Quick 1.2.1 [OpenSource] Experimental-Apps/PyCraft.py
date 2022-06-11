# 
# !/usr/bin/py3
# Download more at https://www.gamefun.com/download-center
# PyCraft version 1.2.1 Quick experimental apps [MODER EDITION] zh-CN
# PyCraft is not for sale.
# If you purchased PyCraft, please report the seller.
# Version: v1.2.0 Quick Experimental apps [MODER EDITION]
# Author: Owen171400 (3381443064@qq.com)
# Updated: Fixed issues about mod installation. SSM will be distributed on version 1.3.
# News: PyCoins entered PyCraft. Get it for free!
# Mods: AreaShow 1.0.9 & Effect 1.0.3 avalible. Inslider mod Flask 1.0.6 also avalible.
# Known issues: Responces of commands are sometimes unrealiable.
# Fixed: Known 134 issues, such as ConnectionOutExceed(Ex0x0921).
# ****************************************************************************
# Peek:
# Version v1.2.0 beta: Developer added more fun sources!
# MODER: Version 1.0, api=1.1.6
# ****************************************************************************
# Update Notes: This version was fully open-source, share your ideas and editions on https://www.gamefun.com/pycraft/opensource-center/
# Example: BetterPyCraft v3.4.9 (source: https://www.gamefun.com/sources/pycraft/betterpycraft327/)
# Better PyCraft [open]Source project: www.opensource.com/betterpycraft/ops/
# Entering PyCraft server on pcft.com/server-100/pycraft-server/
# Thanks to Google LLC for translating.
#
import time
import datetime
import random
import sys
# Import your mod here :).
action = ['脚步声','方块:被破坏','方块:被放置','羊:咩~','奶牛:牟~','猪:叫声~','鸡:咯咯!','村民:自言自语','水:流动']
imported = ['Inslider-Flask','Status-Bar','PyCraft SSM system']
unable = []
name = None
place = 'default'
jy = 0
dig = 5
hunger = 10
toolcase = False
ABQuery = 'User'
Compass = False
foodpack = 0
md=True
account=None
SELECT=int(input("请选择游戏服务器:\n(1)main\n(2)subcontrol\n(3)EMUI\n"))
if SELECT==1 or SELECT==3:
    print("游戏正在启动...")
else:
    print("目前服务器被封禁，游戏正在关闭.")
    sys.exit() # Might Occur Errors (Normal)
print('正在加载你的模组...')
time.sleep(1)
try:
    import mod_areashow as mas
except:
    unable.append('areashow')
else:
    imported.append('areashow')
    mas._Exec().ShowExec()

try:
    import effect as efct
except:
    unable.append('effect')
else:
    imported.append('effect')
    efct._Exec().ShowExec()
print('以下模组可以导入:')
print(imported)
print('以下模组因错误无法导入:')
print(unable)
# Add mods via these codes:
'''
Add mods via:
try:
    import modname
except:
    unable.append('modname')
else:
    imported.append('modname')
    modname._Exec().ShowExec()
'''

def flatbuild(spec=False,flush=True):
    print("重新加载中!")
    print("重建模组...")
    time.sleep(2)
    print("加载地形...")
    time.sleep(1)
    if not flush:
        print("工具列表已禁用！") # Disable Tool List (Commands)
    if spec:
        print("测试模式已启用！") # Develop Mode
def hungercheck():
    if hunger <= 0:
        print('抱歉，您因为太饿而死亡。')
        quit()
def Compass1():
    global place
    if place == 1:
        p = '森林'
    elif place == 2:
        p = '平原'
    elif place == 3:
        p = '沙漠'
    elif place == 4:
        p = '小溪'
    x = str(random.randint(-300, 300))
    y = str(random.randint(-300, 300))
    z = str(random.randint(0, 20))
    print('搜索中...')
    print('您目前处在世界的 x={0}, y={1}, z={2}上.'.format(x, y, z))
    print('目前处在的地形: {}'.format(p))
def start():
    print('感谢您游玩本游戏！')
    print('PyCraft将持续更新，永久免费。')
    print('根据新发布的Internet Social Settings and Fungaments[因特网访问权限及条款]2020, PyCraft\n将对游戏启动做限制，需要启动码以开启PyCraft.')
    print("您的程序序列码为:WT98-OI08-YE73-UD8E")
    print("请在mirrors.gamefun.com/pycraft-exec-disclaim/下载pycraft execute disclaimer!")
    cmt=True
    while cmt:
        passw=int(input("请输入启动码:"))
        if passw==18028922:
            cmt=False
        else:
            print("代码错误.")
    global md
    print("是否启动作弊模式？(y/n)[默认选项y]")
    kl=input().lower()
    if kl == "n":
        print('=====[zh-Cn快照版]冒险模式=====')
        md=False
    else:
        print('=====[zh-Cn快照版]冒险模式[作弊Mode]=====')
        md=True
    efct._Exec().effect() # Mod Effect
    global name, account
    name = input('请输入您的游戏昵称: ')
    account = input("请输入游戏账号: ") # Get at gamefun.accounts.com/register/
def select_place():
    global place
    try:
        place = int(input('请选择出生地点：\n(1)森林\n(2)平原\n(3)沙漠\n(4)小溪\n'))
        print("生物群系已启动。")
    except:
        print('错误输入.')
        quit()
def animal():
    global hunger, foodpack
    animals = ['猪', '羊', '牛', '鸡', '兔子']
    print('搜索中...')
    time.sleep(3)
    if random.randint(1, 100) > 7:
        animal = random.choice(animals)
        print('有一只{}在附近！'.format(animal))
        print('尝试打击...')
        hunger -= 1
        hungercheck()
        time.sleep(1)
        if random.randint(1, 100) > 5:
            print('恭喜您！打中了！一剑就送它解脱了！')
            hunger += 2
            print('补充饥饿值2度')
        else:
            print('可惜啊！它跑了！')
    else:
        print('附近没有动物 :(')
def explore():
    global place, dig, hunger
    print('随便走走，看看有没有好东西！')
    hunger -= 3
    hungercheck()
    if place == 1 or place == 3:
        if random.randint(1, 100) > 80:
            print('唔！前面有个神庙！')
            time.sleep(5)
            print('看看箱子里有些什么好东西！')
            print('镐子、食物、指南针，美不胜收！')
            dig -= 2
            hunger += 5
        else:
            print('啥也没有！')
    else:
        print('捡到了几个鸡蛋。')
        egg = random.randint(1, 4)
        hunger += egg

            
def do():
    global jy, nd, dig, hunger, place, name, toolcase, ABQuery, Compass, foodpack, account
    while True:
        print('饥饿值: {}.'.format(str(hunger)))
        if hunger <= 0:
            print('抱歉，您因为太饿而死亡。')
            break
        mas._Exec().ShowAreaBlock()
        do = int(input('您要干什么？\n(1)采集木板\n(2)探索矿洞\n(3)种植\n(4)查看信息\n(5)经验商城\n(6)打猎\n(7)探索\n(8)使用指南针\n(9)吃饭\n(10)指令\n(11)退出\n(12)[测试]StatusBar\n'))
        if do == 1:
            print('正在采集...')
            time.sleep(random.randint(2, 5))
            mb = random.randint(10, 30)
            print('采集到了{0}块木板。'.format(str(mb)))
            hunger -= 2
            hungercheck()
            jy += mb
            if mb > 20:
                x = input('您可以建造房屋了，要建造吗？(y/n)')
                if x == 'y':
                    time.sleep(5)
                    print('建造成功！')
                    hunger -= 1
                    hungercheck()
                    built = True
                else:
                    print('工作台建造成功！')
                    hunger -= 1
                    hungercheck()
                    toolcase = True
            else:
                print('工作台建造成功！')
                hunger -= 1
                hungercheck()
                toolcase = True
        elif do == 2:
            if random.randint(1, 100) < 95:
                mine = ['金矿', '钻石矿', '铁矿', '煤矿', 'None']
                print('搜索中...')
                hunger -= 2
                hungercheck()
                if dig < 0:
                    dig = 0.5
                time.sleep(dig)
                found = random.choice(mine)
                if found == 'None':
                    print('什么也没有。')
                    continue
                print('发现{0}共{1}块。'.format(found, str(random.randint(1, 7))))
                if found != '煤矿':
                    if toolcase:
                        print('我们用找到的矿石为您做了一把镐子，挖掘更快!')
                        dig -= 0.5
                    else:
                        print('您还没有工作台，无法制造镐子。')
                else:
                    print('烤烤火，真暖！')
            else:
                print('没有矿洞。:(')
        elif do == 3:
            if place != 4:
                print('附近没有水源！')
                continue
            print('耕地建造完毕，小麦5秒成熟。')
            time.sleep(5)
            print('成熟小麦已采集。')
            print('制作面包中...')
            time.sleep(5)
            print('已食用面包，补充饥饿值1.')
            hunger += 1
        elif do == 4:
            print('昵称: {}'.format(name))
            print('饥饿值: {}'.format(hunger))
            print('经验: {}'.format(jy))
            print('挖掘速度: {}s'.format(dig))
            print('权限: {}'.format(ABQuery))
            print('背包中的食物: {}'.format(str(foodpack)))
            print("账号: {}".format(account))
        elif do == 5:
            print('(1)快速挖掘: 15(2)指南针: 20(3)食物补给包: 30')
            m = int(input('请选择：'))
            if m == 1:
                if jy >= 15:
                    jy -= 15
                    dig = 1.5
                else:
                    print('经验不足.')
                    continue
                print('购买成功！')
            elif m == 2:
                if jy >= 20:
                    jy -= 20
                    Compass = True
                else:
                    print('经验不足.')
                    continue
                print('购买成功！')
            elif m == 3:
                if jy >= 30:
                    jy -= 30
                    foodpack += 40
                else:
                    print('经验不足.')
                    continue
                print('购买成功！')
        elif do == 6:
            animal()
        elif do == 7:
            explore()
        elif do == 8:
            if Compass:
                Compass1()
            else:
                print('对不起，您没有指南针.')
        elif do == 9:
            if foodpack > 0:
                print('包里的食物足够补充{}饥饿值。'.format(str(foodpack)))
                eat = int(input('输入补充的饥饿值：'))
                if eat > foodpack:
                    print('不要贪心哦！食物不够补充那么多。')
                else:
                    print('成功！')
                    foodpack -= eat
                    hunger += eat
            else:
                print('包里没有吃的.')
        elif do == 10:
            if md:
                while True:
                    print('请输入指令[必须以/开头]:')
                    efct._Exec().efc()
                    print("以上为effect模组提供的内容。")
                    cmd = input()
                    if cmd == '/fill':
                        print('已将3饥饿值给予玩家。')
                        hunger += 3
                    elif cmd == '/kill @s':
                        print('您将自己杀死了！')
                        quit()
                    elif cmd == '/given jy':
                        print('已将10经验值给予玩家。')
                        jy += 10
                    elif cmd == '/rebuild':
                        print('Flask version 1.0.6.')
                        print('模式: 重建原理 9/9 [None]')
                        print('<None> Survival PyCraft')
                    elif cmd == '/impact':
                        print('Absurd commands')
                    elif cmd == '/$flatbuild':
                        print("PyCraft 正在重新加载...")
                        flatbuild(spec=True)
                        time.sleep(3)
                        print("游戏地图已重启!")
                    elif cmd == '/reload':
                        print("模组正在重新加载...")
                        time.sleep(10)
                        print("加载完毕！")
                    elif cmd == '/control':
                        break
                    else:
                        print('暂未开通此命令/命令错误。')
            else:
                print("作弊模式未开启!")
        elif do == 11:
            exit()
        elif do == 12:
            for i in range(10):
                print(random.choice(action))
def main():
    start()
    select_place()
    do()
if __name__ == '__main__':
    main()

# *****************************************************************************
# Thanks for playing! :)
# License: GameFunLicense-839123732-A
# (c)2022 GameFun Inc.
# Release Notes: Do not use upper information/license for your own pycraft edition certificate, otherwise, your account will automaticly freeze.
