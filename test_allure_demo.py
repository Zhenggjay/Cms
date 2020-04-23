# -*- coding: utf-8 -*
#@Time:2020/4/14 19:31
#@Auther:GJ
import allure
import requests,json
import pytest
from Entry_PartTime import token

@allure.step("步骤1:点xxx")
def step_1():
    print("111")

@allure.step("步骤2:点xxx")
def step_2():
    print("222")

@allure.feature("编辑页面")
class TestEditPage():
    '''编辑页面'''

    def setup(self):
        self.result = None
        self.verify_info = None
        self.verify_result = None
        self.request_param = None

    def teardown(self):
        desc = "<font color='red'>请求参数:</br> </font>{}</br>" \
               "<font color='red'>实际结果:</br> </font>{}</br>" \
               "<font color='red'>验证结果:</br> </font>{}</br>" \
               "<font color='red'>验证信息:</br> </font>{}".format(self.request_param, self.result, self.verify_result,
                                                               self.verify_info)
        allure.dynamic.description(desc)
    @allure.story("这是一个xxx的用例")
    def test_1(self, login):
        '''用例描述：先登录，再去执行xxx'''
        step_1()
        step_2()
        print("xxx")


    @allure.story("打开a页面")
    def test_2(self):
        '''用例描述：先登录，再去执行yyy'''
        headers_one = {'Content-Type': 'application/json;charset=UTF-8', 'Authorization': token("ua0000003764")}
        employeeId = 1851  #
        body = {"employeeId": employeeId, "leaveCompanyIds": ["1", "2"],
                "leaveOfficeType": "INITIATIVE_LEAVE_JOB", "fileList":
                    [{"fileName": "图片1",
                      "fileUrl": "https://default.test.file.dachentech.com.cn/image/app/202001071555037330.jpg"}],
                "leaveTime": "2020-01-07 14:08:00", "hasKnow": True, "hasNeedLeaveProve": False,
                "leaveReason": "1234567", "submitWorkflow": True}
        url = 'https://test-ms.xgjk.info/cms-hr-service/org/areaLeave/save'
        get_post = requests.post(url=url, data=json.dumps(body), headers=headers_one).json()
        self.request_param = body
        self.result = get_post
        self.verify_info = get_post['code']
        self.verify_result = get_post['message']
        assert get_post['code'] == '9999'
@allure.feature("新增页面")
class TestAddPage():
    '''编辑页面'''

    @allure.tag("这是一个xxx的用例标签")
    def test_1(self, login):
        '''用例描述：新增内容'''
        step_1()
        step_2()
        print("xxx")

    @allure.dynamic.story
    @allure.story("新增内容提交")
    def test_2(self, login):
        '''用例描述：新增提交'''
        print("新增内容提交")

    @allure.epic("史诗")
    @allure.description_html("""
    <h1>Test something</h1>
    <table style='width:100%'>
    <tr>
    <th>Firstname</th>
    <th>lastname</th>
    <th>Agename</th>
    </tr>
    <tr align="center">
    <td>Wiilon</td>
    <td>cost</td>
    <td>28</td>
    </tr>
    <tr align="center">
    <td>pytest</td>
    <td>niuGG</td>
    <td>60</td>
    </tr>
    """)
    def test_3(self, login):
        '''用例描述：新增提交'''
        print("史诗")





