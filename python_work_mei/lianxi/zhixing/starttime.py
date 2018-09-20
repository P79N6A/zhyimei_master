# coding:utf-8
import os,time
# start_time=raw_input(u"请输入脚本执行开始时间(例如：12:00)：")
print(u"请输入脚本执行开始时间(例如：12:00")
start_time =raw_input()
while True:
    now_time=time.strftime("%H:%M")
    if now_time ==start_time:
        print(u"开始运行脚本")
        os.chdir("D:\\python_work\\lianxi\\")
        os.system("python excute.py")
        print(u"执行完成后退出")
        break
    else:
        time.sleep(6)
        print(now_time)


# #coding:utf-8
# import os,time
# print("请输入脚本开始执行的时间，例如09:00")
# start_time = raw_input()
# while True:
#     now_time = time.strftime("%H:%M") #获取时间转换为小时分钟
#     if now_time ==start_time:
#         print("开始运行脚本")
#         os.chdir("D:\\python_work\\test\\")
#         os.system("python add_leads.py")
#
#
#         #开始执行脚本
#         print("执行完成后退出")
#         break
#     else:
#         time.sleep(10)
#         print(now_time)
#
