# coding:utf-8
# from test1 import qiche
# benchi=qiche()
# benchi.run()

# from test1 import haha
# hehe=haha()
# hehe.run()


# def runnian(n,m):
#     for i in range(n,m):
#         if  i%4==0  and i%100!=0 or i/400==0:
#             print("闰年%d"%i)
#     return (i)
# t=runnian(1000,2000)
# print t
# def runnian(m,n):
#     for i in range(m,n):
#         if  i%4==0  and i%100!=0  or  i/400==0:
#             print("闰年：%d"%i)
#     return ("结束了i")
# asd=runnian(1000,2000)
# print(asd)
# 1.代码模拟用户登录，当用户名是admin,密码是123456时显示登录成功，
# 否则失败，失败允许重复输入三次，提示：使用while循环更加简洁
#
# a=0
# while True:
#     a=a+1
#     n=raw_input("用户名：")
#     m=raw_input("密码：")
#     if n=="admin" and m=="123456":
#         print("登陆成功")
#         break
#     else:
#         print("账号或密码错误，请重新输入：")
#         if a>=3:
#             print("错误次数过多，禁止登陆！")
#             break

# 3.定义一个方法，输出n*m乘法
# def mn(n,m):
#     for i in range(n,m):
#         for j in range(n,i+1):
#             print("%d*%d=%d"%(j,i,i*j)),
#         print("")
# mn(1,10)
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(j,i,i*j)),
    print("")
# 4.0-9之间可以输出多少不重复的三位数,提示：使用循环

# for a in range(0,10):
#     for b in range(0,10):
#         for c in range(0,10):
#             if a!=b and b!=c and a!=c:
#                 print(a*100+b*10+c)

# class jisuan():
#     def caculate(self,a,b,c):
#         return (a+b)*c
# jisuan= jisuan()
# d=jisuan.caculate(10,9,8)
# print(d)

# 6.求1-2+3-4+5...99表达式执行的结果（用python 语句）
# sum1=0
# sum2=0
# for a in range(1,100):
#     if  a%2==1:
#         sum1=sum1+a
#     else:
#         sum2=sum2-a
# print(sum1+sum2)
