#         print(t)
# #         break


# class qiche():
#     color="red"
#     lunzi="4个"
#     renshu="5个"
#     def run(self):
#         print("跑的可快")
# baoma=qiche()
# print(qiche.color)
# print(qiche.lunzi)
# print(qiche.renshu)
# baoma.run()
#
# class haha:
#     def run(self,m,n):
#         for i in range(m,n):
#             if i%4==0 and i%100!=0 or i%400== 0:
#                 print("今年是%d"%i)
# aaa=haha()
# aaa.run(1000,2000)



#
for i in range(1,5):
    for j in  range(1,5):
        print("%s%2s"%(i,j))
    print("")

# print("%s is %s,%d years old"%(zhangsan,boy,20))
# .输入三个整数a,b,c，请把这三个数按从小到大排序
# 7.求三位数，该三位数的各位数字的立方，求和后等于数字本身，
#  例如：153=1*1*1+5*5*5+3*3*3
# for i in range(100,1000):
#     a=i/100
#     b=i%100/10
#     c=i%10
#     if a*a*a+b*b*b+c*c*c==i:
#         print(i)
# 8.python中怎么声明一个空列表，空字符串
# print sorted ([input(“a:”),input(“b:”),input(“c:”)])
# l=[]
# print (l)
list=[3,9,90,1]
t=list.sort(reverse=True)
print(t)