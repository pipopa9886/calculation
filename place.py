import random
import time

#足し算
def addition(keta,kuchi):
    s=0
    for i in range(0,kuchi):
        x=random.randrange(10**(keta-1),10**keta)
        s += x
        print(x)
    time.sleep(1.2)
    print("答え:",s)



def much():
    print("桁数と口数を選んでください")
    print("桁数")
    global keta
    keta=int(input())
    print("口数")
    global kuchi
    kuchi=int(input())

def run():
    much()
    addition(keta,kuchi)
