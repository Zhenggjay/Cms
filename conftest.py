# -*- coding: utf-8 -*
#@Time:2020/4/14 19:31
#@Auther:GJ
import pytest


@pytest.fixture(scope="session")
def login():
    print("用例先登录")