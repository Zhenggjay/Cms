# -*- coding: utf-8 -*
#@Time:2020/4/14 19:31
#@Auther:GJ
import allure
import pytest

@allure.step("步骤1:点xxx")
def step_1():
    print("111")

@allure.step("步骤2:点xxx")
def step_2():
    print("222")

@allure.feature("编辑页面")
class TestEditPage():
    '''编辑页面'''

    @allure.story("这是一个xxx的用例")
    def test_1(self, login):
        '''用例描述：先登录，再去执行xxx'''
        step_1()
        step_2()
        print("xxx")


    @allure.story("打开a页面")
    def test_2(self, login):
        '''用例描述：先登录，再去执行yyy'''
        print("yyy")
@allure.feature("新增页面")
class TestAddPage():
    '''编辑页面'''

    @allure.tag("这是一个xxx的用例标签")
    def test_1(self, login):
        '''用例描述：新增内容'''
        step_1()
        step_2()
        print("xxx")


    @allure.story("新增内容提交")
    def test_2(self, login):
        '''用例描述：新增提交'''
        print("新增内容提交")

    @allure.epic("史诗")
    def test_3(self, login):
        '''用例描述：新增提交'''
        print("史诗")

   
