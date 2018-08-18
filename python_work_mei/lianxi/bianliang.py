# coding:utf-8
a=1
b=1
class bian():
    global a,b
    a=3
    b=5
    def bianliang(self):
        a=2
        b=4
        print("a的值是：%d"%a)
        print("b的值是：%d"%b)
sd=bian()
sd.bianliang()
print("外面a的值是：%d"%a)
print("外面b的值是：%d"%b)



hehe=6
def f():
    print(hehe)
f()
# print(hehe)