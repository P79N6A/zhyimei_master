 # coding:utf-8
from random import Random
import xlrd
# table = xlrd.open_workbook(r"D:\Python27\country.xlsx")
# sheet = table.sheets()[0]
# k =sheet.cell(1,1)
# l = sheet.row_values(2)
# m = sheet.col_values(0)
# print(k)
# print(l)
# print(m)
# print(m[1])
# 封装表格
# def fzbg(m,n):
#     import xlrd
#     table = xlrd.open_workbook("D:\Python27\student.xlsx")
#     sheet = table.sheets()[0]
#     k =sheet.cell(m,n)
#     return (k)
# print(fzbg(1,1))
# class enhen():
#     def haha(self,a,b):
#         import xlrd
#         table = xlrd.open_workbook("D:\Python27\student.xlsx")
#         sheet = table.sheets()[0]
#         l = sheet.row_values(a)[b]
#         return (l)
# t=enhen()
# print(t.haha(0,0))

class a():
    table = xlrd.open_workbook("D:\Python27\student.xlsx")
    global table
    def f(self,b):
        sheet = table.sheets()[0]
        l= sheet.row_values(b)
        return (l)
    def kehu(self,ee):
        sheet=table.sheets()[1]
        ww=sheet.row_values(ee)
        return (ww)
    def yh(self,dd):
        table = xlrd.open_workbook("D:\Python27\student.xlsx")
        sheet = table.sheets()[2]
        yhm= sheet.row_values(dd)
        return (yhm)
    def cp(self,ccp):
        sheet = table.sheets()[3]
        lll=sheet.row_values(ccp)
        return (lll)
if __name__ == '__main__':
    r=Random()
    h=r.randint(1,21)
    xx=a()
    s=xx.kehu(h)
    print(s)


    print(h)
    t=a()
    oo=t.yh(h)
    print(oo[0],oo[1])


if __name__ == '__main__':
    r= Random()
    h=r.randint(1,10)
    print(h)
    t=a()
    ss=t.f(h)
    print(ss[0],ss[1])
# class ge():
#     def biao(self,a):
#         import xlrd
#         table=xlrd.open_workbook("D:\Python27\student.xlsx")
#         sheet=table.sheets()[0]
#         l=sheet.row_values(a)
#         return (l)
if __name__ == '__main__':
    i=ge()
    c=i.biao(1)




