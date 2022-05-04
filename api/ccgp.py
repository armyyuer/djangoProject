import re, requests
import json
import time
import dingtalk.api


# 获得access_token
def access_token():
    request = dingtalk.api.OapiGettokenRequest("https://oapi.dingtalk.com/gettoken")
    request.appkey = "dingew1bs4souannu3md"
    request.appsecret = "t7TtbMeg-APC_37FKHRx2-2GSkwUeSWUoUSr687i9rOa6jUBF4OZcA7WHefPIGCJ"
    f = request.getResponse()
    print(f['access_token'],"access_token")  # 获取access_token
    return f


# 获得部门列表
def get_department_list(dept_id=1):
    """
        查询部门列表
        :param dept_id: 部门id，默认为1（根部门），可输入任意部门id
        """
    post_url = "https://oapi.dingtalk.com/topapi/v2/department/listsub?access_token=%s" % (access_token())
    data = {
        "dept_id": dept_id,
    }
    response = requests.post(post_url, data)
    str_res = response.text
    result = (json.loads(str_res)).get('result')
    print(result,"get_department_list")
    return result


# 获得在职员工列表
def get_user_list():
    post_url = "https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/queryonjob?access_token=%s" % (access_token())
    # 初始化offset
    offset = 0
    while True:
        # 请求参数
        data = {
            "status_list": "2,3,5,-1",
            "offset": offset,
            "size": 50
        }
        # 发送post请求
        response = requests.post(post_url, data)
        str_res = response.text
        # json解析
        result = (json.loads(str_res)).get('result')

        # 返回当前页列表
        yield result["data_list"]
        print(result["data_list"],"get_user_list")
        try:
            # 下一页（下50条）
            offset = result["next_cursor"]
            continue
        # 退出条件
        except KeyError:
            break


if __name__ == '__main__':
    access_token()
    get_department_list(dept_id=1)
    get_user_list()
    today = time.strftime('%Y-%m-%d', time.localtime())
    print(today)
    host = "www.ccgp-guangxi.gov.cn"
    url = 'http://www.ccgp-guangxi.gov.cn/front/search/category'
    # url = 'http://www.ccgp-guangxi.gov.cn/reformColumn/index.html'
    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        #               'Chrome/100.0.4896.60 Safari/537.36 ',
        # 'cookie': 'acw_tc=2f624a5216515120695576519e78fd6cf0d08d9ff5f73384ee1a8dd3bd0271;path=/;HttpOnly;Max-Age=1800',
        # 'Referer': 'http://www.ccgp-guangxi.gov.cn/reformColumn/index.html'

        'Host': 'www.ccgp-guangxi.gov.cn',
        'Content-Type': 'application/json',
    }
    data = {
        'categoryCode': 'ZcyAnnouncement10016',
        'pageSize': '15',
        'pageNo': 1,
        'districtCode': ["450500"]
    }
    title = ""  # 标题
    pathName = ""  # 类型
    districtName = ""  # 区域
    url_n = ""  # 链接
    publishDate = ""  # 发布时间
    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    b_list = response.json()
    n_list = b_list["hits"]["hits"]
    # print(n_list)
    # 遍历response
    for i in n_list:
        title = i["_source"]["title"]
        pathName = i["_source"]["pathName"]
        districtName = i["_source"]["districtName"]
        url_n = i["_source"]["url"]
        publishDate = i["_source"]["publishDate"]
        timeArray = time.localtime(int(publishDate / 1000))
        otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
        print(title)
        print(publishDate)
        print(pathName)
        print(districtName)
        print("日期", otherStyleTime)
        print(url_n)
        print("-----------------------------------------------------")


