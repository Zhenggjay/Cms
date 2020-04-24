# -*- coding: utf-8 -*
#@Time:2020/4/21 17:46
#@Auther:GJ
import allure
import pytest
from pactverify.matchers import Matcher, EachLike, Like, PactVerify



@allure.feature("获取制定会话接口")
class TestGetConversation:

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

    # 获取制定会话接口
    @pytest.mark.case_p0
    @allure.title("根据conversationId获取制定会话接口")
    def test_conversations_by_conversationId(self):
        """根据imId获取会话列表"""
        conversationId = '5da9659ff53f07328308b355'
        # result = ApiTest().api_get_conversations_by_conversationId(conversationId)
        # print("返回的结果%s" % (result.json()))


        expect_format = Matcher({
            "statusCode": 200,
            "status": "success",
            "result": Like({
                "unreadCount": Like(2, key_missable=True),
                "messageReadTime": 34567890,
                "userType": "CUSTOMER",
                "_id": Matcher(conversationId),
                "imId": "erp-2253F6D0-B558-466F-87FA-86395B5A2830",
                "targetId": "erp-4B41582E-91D6-4337-846C-7D2B09D8F900",
                "type": "PERSON",
                "__v": 0,
                "createdAt": "2019-10-18T07:11:27.350Z",
                "displayName": "sdsa",
                "latestMessage": {
                    "description": "hahahaha最近消息dhkasldhasjkfhklasfhklas"
                },
                "portraitUri": "https://cdn.mytoken.org/Fvuapzak9DwkHSuBPp0hcfw1emhf",
                "tieId": "PERSON:erp-2253F6D0-B558-466F-87FA-86395B5A2830:erp-4B41582E-91D6-4337-846C-7D2B09D8F900",
                "updatedAt": "2019-10-18T07:25:06.161Z",
                "id": Matcher(conversationId)
            })
        })

        mPactVerify = PactVerify(expect_format, hard_mode=True)

        self.request_param = "conversationId" + str(conversationId)
        # self.result = result.json()
        mPactVerify.verify(self.result)

        self.verify_info = mPactVerify.verify_info
        self.verify_result = mPactVerify.verify_result
        assert mPactVerify.verify_result == True