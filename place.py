import json
import random
import time

#足し算
def save():
    print("もし必要なら結果を記録できます")
    print("名前とポイントを保存しますか")
    print("はい:0,いいえ:1")
    save=0
    save=int(input())
    if save==0:
        with open("date.json","r") as file:
            menu=json.load(file)
        print("名前を教えてください")
        name=input()
        c=name not in menu
        if c==True:
            you={"name":name,"point":point}
            menu.append(you)
            with open("date.json","w") as f:
                json.dump(menu,f)
        else:
            print("あるよ")
    else:
        print("中止")


def addition(keta,kuchi,kankaku):
    list=[]
    sum=0
    for a in range(0,kuchi):
        a=random.randrange(10**(keta-1),10**keta)
        list.append(a)
        sum+=a

    for i in list:
        print("\r{0:d}".format(i),end="")
        time.sleep(kankaku)

    print("\n答えを入力してください")
    answer=int(input())
    if answer==sum:
        print("正解!")
    else:
        print("不正解...")
    time.sleep(0.5)
    print("\n答え:",sum)

def much():
    print("桁数と口数、間隔を選んでください")
    print("桁数")
    global keta
    keta=int(input())
    if keta >10:
        keta=10
    else:
        pass
    print("口数")
    global kuchi
    kuchi=int(input())
    print("間隔 （小数可能）")
    global kankaku
    kankaku=float(input())
    global point
    point=(10*keta)*kuchi-(10*kankaku)


def run():
    much()
    print("始めます。よろしいですか")
    print("よろしければ、ENTERを押してください")
    q=input()
    if q=="":
        addition(keta,kuchi,kankaku)
        save()
    else:
        pass
