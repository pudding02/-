from ration import rooms,helps,fg,f_g,h_look

bag=[]
room="门厅"
item=rooms[room]["item"]
T=True

print(h_look(room))
while T:#游戏主循环
    make=input('操作:')
    if make=='help':#帮助反馈
        T=helps(room,bag)
        continue
    #判断游戏结束
    if make=='exit' or make=='quit':
        print("游戏结束！")
        break
    #行进/位置变换
    elif make[:2]=='go':
        fx=make.replace(' ','')[2:]
        if fx in ["north","south","east","west","down"]:
            if fx in rooms[room]["exits"]:
                #判断是否满足进入走廊条件
                if room=='门厅' and fx=='east':
                    if '烛台' in bag and '火柴' in bag:
                        x=input("是否使用火柴点燃烛台以便进入走廊？(yes/no)")
                        if x=='yes':
                            room='走廊'
                            h_look(room)
                        else:
                            print("走廊光线很暗，无法探索该区域！")
                    else:
                        print("走廊光线很暗，您需要拥有火柴点燃烛台才能更方便探索！")
                else:
                #判断是否满足通关条件
                    if room=='厨房' and fx=='down':
                        if '生锈的铁钥匙' in bag:
                            room='地下通道'
                            print("恭喜通关！！！")
                            break
                        else:
                            print("您需要拥有钥匙才能进入地下通道！")
                    else:#正常位置变换并输出房间说明
                        room=rooms[room]["exits"][fx]
                        h_look(room)
            else:
                print("那边没有路！")
        else:
            print("输入有误！")
            continue
    #拾取物品
    elif make[:4]=='take':
        wp=make.replace(' ','')[4:]
        if wp in rooms[room]["item"]:
            bag.append(wp)
            print(f"你拿起了 {wp}")
            del rooms[room]["item"][wp]
        else:
            print(f"{fg}这里没有 {wp}")
    #查询背包
    elif make=="inventory":
        if not bag:
            print("空空如也！")
        else:
            print("=======================\n你背包里有：")
            for i in bag:
                print(i)
    else:
        print(f"{fg}指令有误！！！")


