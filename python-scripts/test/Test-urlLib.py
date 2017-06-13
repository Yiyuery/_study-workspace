#coding='utf-8'
#author Yiyuery
#todo 下载网页的三种方法

import urllib.request
import http.cookiejar

# 网页下载器
url = "http://www.baidu.com"

def print_resp(title):
    print(title)
    resp = urllib.request.urlopen(url)
    print(resp.getcode)
    print(len(resp.read()))

def print_resp_2(title):
    print(title)
    req = urllib.request.Request(url)
    req.add_header("user-agent", "Mozilla/5.0")
    resp = urllib.request.urlopen(req)
    print(resp.getcode)
    print(len(resp.read()))

def print_resp_3(title):
    print(title)
    cookie = http.cookiejar.CookieJar()
    # handler : urllib.request.HTTPCookieProcessor(cookie)
    # 添加特殊情境的处理器 扩充url.request的处理cookie能力
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    urllib.request.install_opener(opener)
    resp = urllib.request.urlopen(url)
    print(resp.getcode())
    print(cookie)
    print(resp.read())

# -----------------------------------------------
print_resp("基本的网络请求示例：")
# -----------------------------------------------
print_resp_2("伪装浏览器发起网络请求示例：")
# -----------------------------------------------
print_resp_3("含有cookie的网络请求")

# http://www.cnblogs.com/cocoajin/p/3679821.html
# urllib 发起网络请求的常见方法


# 网页解析器 正则表达式、html.parser、Beautiful Soup 、lxml 结构化解析


