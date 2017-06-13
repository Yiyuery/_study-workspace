# coding='utf-8'
# author:Yiyuery
# Todo:模拟登陆LinkedIn v1.0.0.1
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


# 登陆请求表单 提交
def do_login(resp, dev_mode):
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
    # soup.find('input', attrs={"name": 'session_redirect'})['value']

    trk = soup.find('input', attrs={"name": 'trk'})['value']
    fromEmail = soup.find('input', attrs={"name": 'fromEmail'})['value']

    if dev_mode == 'true':
        session_key = 'xiazhaoyang@live.com'
        session_password = 'Capsule-v-1.0'
    else:
        session_key = input("请输入账号：（邮箱）")
        session_password = input("请输入密码：")

    # 填充表单
    payload = {
        'isJsEnabled': isJsEnabled,
        'source_app': source_app,
        'tryCount': tryCount,
        'clickedSuggestion': clickedSuggestion,
        'session_key': session_key,
        'session_password': session_password,
        'signin': signin,
        'session_redirect': session_redirect,
        'trk': trk,
        'loginCsrfParam': loginCsrfParam,
        'fromEmail': fromEmail,
        'csrfToken': csrfToken,
        'sourceAlias': sourceAlias
    }
    # print("登陆提交参数：-> json")
    # print(payload)
    # postdata = bytes(urllib.parse.urlencode(payload), encoding='utf-8')
    # print("登陆提交参数：-> 追加网页请求参数")
    # print(postdata)
    # 提交表单 模拟浏览器
    # urllib.request.urlopen('https://www.linkedin.com/uas/login-submit', data=postdata)
    form_resp = browser_post('https://www.linkedin.com/uas/login-submit', payload)
    return form_resp


# post 请求
def do_post(_url, fmt):
    add_cookie()
    resp = urllib.request.urlopen(_url)
    rel = resp.read()
    if fmt == 'true':
        rel = rel.decode("utf-8")
    return rel


# 添加cookie
def add_cookie():
    cookie = http.cookiejar.CookieJar()
    # handler : urllib.request.HTTPCookieProcessor(cookie)
    # 添加特殊情境的处理器 扩充url.request的处理cookie能力
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    urllib.request.install_opener(opener)
    return


# 模拟浏览器
def browser_post(url, para):
    print(para)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    headers = {'user-agent': user_agent}
    data = bytes(urllib.parse.urlencode(para), encoding='utf-8')
    req = urllib.request.Request(url, data, headers)
    resp = urllib.request.urlopen(req)
    #print("模拟浏览器返回结果：" + resp.read().decode("utf-8"))
    return resp


# 获取login界面动态参数
def init_login(dev_mode):
    _url = 'https://www.linkedin.com/uas/login'
    resp = do_post(_url, 'true')
    # 解析页面表单信息
    print("开始模拟登陆：" + _url)
    # print(resp.decode('utf-8'))
    form_resp = do_login(resp, dev_mode)
    # 解析验证页面的表单
    validate_form(form_resp)
    return


# 模拟验证信息
def validate_form(form_resp):
    verification_code = input('请输入LinkedIn验证码：')
    url = 'https://www.linkedin.com/uas/ato-pin-challenge-submit'
    # html处理
    soup = BeautifulSoup(form_resp, "lxml")
    # 查找表单
    soup = soup.find('form', attrs={"name": "ATOPinChallengeForm"})
    print(soup)
    # 提取表单信息
   # dts = soup.find('input', id='dts-ATOPinChallengeForm')['value']
   # security_challenge_id = soup.find('input', id='security-challenge-id-ATOPinChallengeForm')['value']
   # sourceAlias = soup.find('input', id='sourceAlias-ATOPinChallengeForm')['value']
   # csrfToken = soup.find('input', id='csrfToken-ATOPinChallengeForm')['value']
   # origSourceAlias = soup.find('input', id='origSourceAlias-ATOPinChallengeForm')['value']

  #  validate_para = {
   #     'verification-code': verification_code,
  #     'dts': dts,
   #     'security-challenge-id': security_challenge_id,
   #     'sourceAlias': sourceAlias,
   #     'csrfToken': csrfToken,
   #     'origSourceAlias': origSourceAlias
  #  }
  #  print(validate_para)
    return


# 检查开发模式
def check_mode():
    mode = input('请输入开发模式：true/false :')
    if len(mode) < 4 or len(mode) > 5:
        mode = 'true'
    return mode


# 学校搜索
def init_search():
    _url2 = "https://www.linkedin.com/school/1503/alumni?keywords=%E9%BA%BB%E7%9C%81%E7%90%86%E5%B7%A5"
    resp2 = urllib.request.urlopen(_url2)
    print("获取麻省理工校友: ")
    print(resp2.read().decode("utf-8"))
    return


# 初始化函数
def init():
    # 获取动态参数并模拟登陆
    #init_login(check_mode())
    init_login('true')
    # 登陆成功后发起学校搜索的请求
    init_search()
    return


# 主函数
if __name__ == '__main__':
    init()
    # _url2 = "https://www.linkedin.com/school/1503/alumni?keywords=%E9%BA%BB%E7%9C%81%E7%90%86%E5%B7%A5"
    # resp2 = urllib.request.urlopen(_url2)
    # print("获取麻省理工校友: ")
    # print(resp2.read().decode("utf-8"))
