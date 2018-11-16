#-*- coding=UTF-8 -*-
import public.test_base
import time
import uiautomator2 as u2
import uiautomator

d = u2.connect_usb(u"dbfc611")
# SJE5T17223002057
# dbfc611
# MKJNW18421020291
print d.device_info
# d.press("back")
time.sleep(2)
# d(className="android.view.View", instance=6).swipe("left", steps=10)
# d.swipe( 200, 800, 1000, 800, duration=0.5)
# print "1"
# time.sleep(2)
# d.swipe( 1000, 800,200, 800, duration=0.5)
# for i in range(1,6):
#     d.swipe(540, 500, 540, 1600, duration=0.5)
#     i=i+1
# d.swipe( 540, 500,540, 1600, duration=0.5)
d(resourceId="online.skyplan.echo:id/avator").click()



