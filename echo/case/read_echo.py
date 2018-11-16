#-*- coding=UTF-8 -*-
import unittest
import public.test_base
import time
import uiautomator2 as u2


class echo_test(unittest.TestCase):
    def setUp(self):
        global zhyi,d
        d = u2.connect_usb(u"dbfc611")
        # SJE5T17223002057
        # dbfc611
        # MKJNW18421020291
        zhyi=public.test_base.echo_base()
        zhyi.connect()
        public.test_base.echo_base.echo_start(zhyi)
    def test_mine_echo(self):
        """
        查看我的瞬间
        :return:
        """
        public.test_base.echo_base.echo_login_weixin(zhyi)
        # d(resourceId="online.skyplan.echo:id/skip").click()
        # time.sleep(2)
        d(resourceId=u"online.skyplan.echo:id/avator").click()
        time.sleep(2)
        zhyi.swiperight()
        # time.sleep(3)
        # zhyi.swiperight()
        # time.sleep(3)
        # zhyi.swiperight()
        # time.sleep(3)
        # zhyi.swiperight()
        # time.sleep(3)
        # zhyi.swiperight()
        time.sleep(3)
        zhyi.swiperight()
        # self.assertEqual(True, False)
    def tearDown(self):
        public.test_base.echo_base.echo_logout(zhyi)
        public.test_base.echo_base.echo_stop(zhyi)

if __name__ == '__main__':
    unittest.main()
