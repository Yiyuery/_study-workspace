# coding='utf-8'
# author:Yiyuery
# Todo:模拟登陆LinkedIn
# From :
#   > linkedIn登录
#   http://blog.csdn.net/xiaoxinwenziyao/article/details/50387184
#   http://blog.csdn.net/shomy_liu/article/details/37658701
#   > Beautiful Soup 网页解析器
#   http://kevinkelly.blog.163.com/blog/static/21390809320133185748442/
#   http://cuiqingcai.com/1319.html
#   > post 请求
#   https://www.v2ex.com/t/342795

import re
import json
import urllib.request
import http.cookiejar
import bs4
from bs4 import BeautifulSoup, Comment


def login(resp):
     # html处理
    soup = BeautifulSoup(resp, "lxml")
    # 查找表单
    soup = soup.find(id="login")

    # 提取表单信息
    loginCsrfParam = soup.find('input', id='loginCsrfParam-login')['value']
    csrfToken = soup.find('input', id='csrfToken-login')['value']
    sourceAlias = soup.find('input', id='sourceAlias-login')['value']
    isJsEnabled = soup.find('input', attrs={"name": 'isJsEnabled'})['value']
    source_app = soup.find('input', attrs={"name": 'source_app'})['value']
    tryCount = soup.find('input', id='tryCount')['value']
    clickedSuggestion = soup.find('input', id='clickedSuggestion')['value']
    signin = soup.find('input', attrs={"name": 'signin'})['value']
    session_redirect = 'https://www.linkedin.com/voyager/loginRedirect.html'
    #soup.find('input', attrs={"name": 'session_redirect'})['value']

    trk = soup.find('input', attrs={"name": 'trk'})['value']
    fromEmail = soup.find('input', attrs={"name": 'fromEmail'})['value']

    # 填充表单
    payload = {
        'isJsEnabled': isJsEnabled,
        'source_app': source_app,
        'tryCount': tryCount,
        'clickedSuggestion': clickedSuggestion,
        'session_key': 'xiazhaoyang@live.com',
        'session_password': 'Capsule-v-1.0',
        'signin': signin,
        'session_redirect': session_redirect,
        'trk': trk,
        'loginCsrfParam': loginCsrfParam,
        'fromEmail': fromEmail,
        'csrfToken': csrfToken,
        'sourceAlias': sourceAlias
    }
    print("登陆提交参数：-> json")
    print(payload)
    postdata = bytes(urllib.parse.urlencode(payload), encoding='utf-8')
    print("登陆提交参数：-> 追加网页请求参数")
    print(postdata)
    # 提交表单
    response= urllib.request.urlopen('https://www.linkedin.com/uas/login-submit', data=postdata)
    return


def post_url(_url):
    cookie = http.cookiejar.CookieJar()
    # handler : urllib.request.HTTPCookieProcessor(cookie)
    # 添加特殊情境的处理器 扩充url.request的处理cookie能力
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    urllib.request.install_opener(opener)
    resp = urllib.request.urlopen(_url)
    return resp.read()


if __name__ == '__main__':

    # 获取js参数
    _url = 'https://www.linkedin.com/uas/login'
    resp = post_url(_url)
    print("登陆界面获取动态参数："+_url)
    print(resp)

    login(resp)

    _url2 = "https://www.linkedin.com/school/1503/alumni?keywords=%E9%BA%BB%E7%9C%81%E7%90%86%E5%B7%A5"
    resp2 = urllib.request.urlopen(_url2)
    print("获取麻省理工校友: ")
    print(resp2.read().decode("utf-8"))

