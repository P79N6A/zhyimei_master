# coding:utf-8
# import unittest
# # unittest.teseCase  #测试用例
# # unittest.TestCase  #测试套件
# # unittest.TextTestRunner   #用例执行器
# class first_test(unittest.TestCase):                     #继承Testcase类，使定义
#     def setUp(self):                    #初始化脚本环境，准备数据
#         print("开始")
#     def test_count2(self):               #主要测试内容，测试用例只反馈此方法执行的结果
#         a=2
#         b=3
#         if a+b==4:
#             print("a+b=4")
#         else:
#             print("a+b!=4")
#     def tearDown(self):                 #退出脚本执行环境
#         print("用例执行完毕")
#     def test_count1(self):
#         print("第二")
# if __name__ == '__main__':
#     unittest.main()