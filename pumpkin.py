#-*- coding:utf-8 -*-
import math
import thinkstats as ts

def Pumpkin():
    pumpkins = [0.5, 0.5, 1.5, 1.5, 96.0]

    mean, var = ts.MeanVar(pumpkins)

    print u'平均:', mean
    print u'分散:', var
    print u'標準偏差:', math.sqrt(var)

def main():
    Pumpkin()

if __name__ == '__main__':
    main()
