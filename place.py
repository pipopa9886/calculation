import random
import time

#足し算
def addition(keta,kuchi,kankaku):
    s=0
    list=[]
    sum=0
    for a in range(0,kuchi):
        a=random.randrange(10**(keta-1),10**keta)
        list.append(a)
        sum+=a

    for i in list:
        print("\r{0:d}".format(i),end="")
        time.sleep(kankaku)
    time.sleep(1.2)
    print("\n答え:",sum)

def much():
    print("桁数と口数、必要であれば間隔も選んでください")
    print("桁数")
    global keta
    keta=int(input())
    print("口数")
    global kuchi
    kuchi=int(input())
    print("間隔（秒単位）")
    global kankaku
    kankaku=float(input())

def run():
    much()
    print("始めます。よろしいですか")
    print("よろしければ、ENTERを押してください")
    q=input()
    if q=="":
        addition(keta,kuchi,kankaku)
    else:
        pass

run()
