#-*- coding=UTF-8 -*-
import uiautomator2 as u2
import time


class echo_base():
    def connect(self):
        """
        连接测试机
        :return:
        """
        global d
        d = u2.connect_usb(u"dbfc611")
        # SJE5T17223002057
        # MKJNW18421020291
        # dbfc611
        print d.device_info
        return d
    def echo_start(self):
        """
        启动echo
        """
        start=d.app_start(u"online.skyplan.echo")
        time.sleep(5)
        return start
    def echo_login_weixin(self):
        """
        微信登录echo
        """
        login_weixin=d.click(0.432, 0.758)
        # login_weixin=d(resourceId="online.skyplan.echo:id/login_wechat_image").click()
        time.sleep(5)
        return login_weixin
    def echo_login_phone(self):
        """
        手机登录
        :return:
        """
        mobile_login=d(resourceId="online.skyplan.echo:id/mobile_login").click()
        time.sleep(3)
        return mobile_login
    def takescreen(self):
        """
        截图
        :return:
        """
        takescreen=d.screenshot(u"echo.jpg")
        return takescreen
    # a=d.screenshot("test.jpg")
    # image = d.screenshot()
    # image.save("home.jpg")
    # time.sleep(5)
    def swipeleft(self):
        """
        左滑屏幕
        :return:
        """
        swipeleft=d.swipe(1000, 800, 200, 800, duration=0.5)
        return swipeleft
    def swiperight(self):
        """
        右滑视频
        :return:
        """
        swiperight=d.swipe( 200, 800, 1000, 800, duration=0.5)
        return swiperight
    def swipeup(self):
        """
        上滑屏幕
        :return:
        """
        swipeup=d.swipe( 540, 1600,540, 100, duration=0.5)
        return swipeup
    def swipedown(self):
        """
        下滑屏幕
        :return:
        """
        swipdown=d.swipe(540, 500, 540, 1600, duration=0.5)
        return swipdown
    def echo_logout(self):
        """
        退出echo
        :return:
        """
        logout =d.click(0.135, 0.08)
        time.sleep(3)
        logout =d(resourceId="online.skyplan.echo:id/tv_nickname").click()
        time.sleep(3)
        logout =d(resourceId="online.skyplan.echo:id/tv_exit_account").click()
    def echo_stop(self):
        """
        关闭echo
        :return:
        """
        stop=d.app_stop(u"online.skyplan.echo")
        return stop