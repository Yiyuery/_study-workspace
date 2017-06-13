# net_utils.py

import urllib.request
import http.cookiejar
import bs4
from bs4 import BeautifulSoup, Comment

def hello():
    print("hello, Master! I'm net_utils!")
    return

# 网页解析
def resp_soup(resp):
    return BeautifulSoup(resp, "lxml")

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