#转正申请申请
import threading,requests,json,time,sys,re
from datetime import datetime,timedelta
from urllib import parse
headers = {'Content-Type': 'application/json;charset=UTF-8'}

def token(username,url='test'):
    # 拿到token
    url = 'http://%s-ms.xgjk.info/cms-auth/auth/app/login'%url#"http://pre-ms.xgjk.info/cms-auth/auth/app/login"#
    body = {"username":username , "password": "888888", "isBind": "NO"}  # 创建人
    try:
        token_data = requests.post(url=url, headers=headers, data=json.dumps(body)).json()
        if int(token_data.get('code')) == 0000:
            # 操作人和审核人后续写成变量动态生成，讲解先暂时写死
            if body.get('username') == "ua0000002158":
                print('操作人:艾丽斯  登录时间:%s  登录状态:登录成功' % time.strftime('%Y-%m-%d %H:%M:%S'))
                token = token_data.get('value').get('token')
                return token
            if body.get('username') == "ua0000003764":
                print('操作人:蒋庆富  登录时间:%s  登录状态:登录成功' % time.strftime('%Y-%m-%d %H:%M:%S'))
                token = token_data.get('value').get('token')
                return token
            elif body.get('username') == "ua0000002156":
                print('审核人:王丽娜  登录时间:%s  登录状态:登录成功' % time.strftime('%Y-%m-%d %H:%M:%S'))
                token = token_data.get('value').get('token')
                return token
            else:
                print("其他用户登录时间:%s  登录状态:登录成功：" % time.strftime('%Y-%m-%d %H:%M:%S'))
                token = token_data.get('value').get('token')
                return token
        else:
            print('%s  登录失败' % time.strftime('%Y-%m-%d %H:%M:%S'))
            sys.exit()
    except json.decoder.JSONDecodeError:
        print("正在构建环境....")
        sys.exit()
#获取审核通过的新员工入职去做转正操作
def get_employee():
    n=0
    headers_one = {'Content-Type': 'application/json;charset=UTF-8','Authorization':token("ua0000003764",'pre')}
    for i in range(0,6):
        #InApplicationurl='http://pre-ms.xgjk.info/cms-hr-service/org/employeeEntryApply/findByQuery?pageSize=10&pageNumber=%s&companyId=1&billState=AUDIT_PASS&showWaitAudit=NO'%i#替换页数
        InApplicationurl='http://pre-ms.xgjk.info/cms-hr-service/org/employeeEntryApply/findByQuery?pageSize=10&pageNumber=%s&companyId=1&billState=AUDIT_PASS&showWaitAudit=NO'%i#修改公司id
        info=requests.get(InApplicationurl,headers_one).json()['result']
        for i in info:
            n+=1
            value=i['id']#单据id
            employeeName=i['employeeName']#获取名称
            postId=i['postId']#职位id
            departmentId=i['departmentId']#获取部门id
            get_time='http://pre-ms.xgjk.info/cms-hr-service/org/employeeEntryApply/getFullTimeApply?id=%s'%value
            times = requests.get(get_time, headers_one).json()['employeeCompanyApply']['entryTime']
            name=parse.quote(employeeName)
            get_employeeidurl = 'http://pre-ms.xgjk.info/cms-basic-service/account/find?employeeName={}&pageNumber=1&pageSize=10'.format(name)
            employeeid=requests.get(get_employeeidurl, headers_one).json()['result'][0]['employeeId']
            #利用datetime.strptime(times, "%Y-%m-%d %H:%M:%S")1.把str格式转换成时间格式str 转datetime.datetime，2.再去切掉后面时分秒,.strftime("%Y-%m-%d")转成字符串形式
            trial_time=(datetime.strptime(times, "%Y-%m-%d %H:%M:%S")+ timedelta(days=90)).strftime("%Y-%m-%d")
            print(employeeName,trial_time,'employeeid:',employeeid)
            positiveurl='http://pre-ms.xgjk.info/cms-hr-service/org/employee/official/save'
            body={"employeeId":employeeid,"fileUrl":"","officialExplain":"","officialTime":trial_time,"submitWorkflow":False}
            get_positive=requests.post(positiveurl, headers=headers_one,data=json.dumps(body)).json()
            print(get_positive)
if __name__=='__main__':
    print('go')
    get_employee()