import random
import time

#足し算
def addition(keta,kuchi,kankaku):
    s=0
    for i in range(0,kuchi):
        x=random.randrange(10**(keta-1),10**keta)
        s += x
        print(x)
        time.sleep(kankaku)
    time.sleep(1.2)
    print("答え:",s)

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
    kankaku=int(input())

def run():
    much()
    addition(keta,kuchi,kankaku)
