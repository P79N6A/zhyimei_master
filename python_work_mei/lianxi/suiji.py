# coding:utf-8
# from random import Random
# ran =Random()
# a =ran.randint(1,10000)
# print(a)

from  random import Random
ran =Random()
for i in range(1,10000):
    # print("%d%d"%(138,ran.randint(10000000,100000000)))
    # if ran.randint(100000000,1000000000)==348929394:
    #     print("我的")
    #     break
    print("%d%s"%(ran.randint(100000000,1000000000),"@qq.com"))