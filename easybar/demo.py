import time
from api import *



def main():
    barA = EasyBar(100, colour='green', display='=',boundary='||',mode='p')
    barB = EasyBar(100, colour='red', bg_colour="white")

    for _ in barA:
        time.sleep(0.01)

    for i in barB:
        with open('tmp.txt', 'at') as f:
            f.write(str(i))

if __name__ == "__main__":
    main()