# coding='utf-8'
# author:Yiyuery
# TODO: 爬取91job网站人员简历信息

import net_utils
import person_bean
import dict_utils

# 全局数据容器
dataHolder = {
    'request': {
        'url': 'http://job.91boshi.net/personnellist.aspx'
    },
    'resp': {
        'pageView_1': ''
    },
    'doc': {
        'doc_1': ''
    },
    'page': {
        'current': 1
    },
    'form': {
        '__EVENTTARGET': 'GridView1',
        '__EVENTARGUMENT': 'Page$2',
        '__LASTFOCUS': '',
        '__VIEWSTATE': '',
        '__EVENTVALIDATION': ''
    },
    'persons': []
}


# 初始化加載
def init_load():
    dataHolder['resp']['pageView_1'] = net_utils.do_post(dataHolder['request']['url'], 'true')
    return

# 绘制分割线
def print_part_line():
    print('--------------------------------------------------------------------')
    print('--------------------------------------------------------------------')
    return

# 数据解析
def table_parser(resp):
    soup = net_utils.resp_soup(resp)
    table = soup.find('table', id='GridView1')
    base_url = 'http://job.91boshi.net/'
    for tr in table.findAll(class_='person_info'):
        person_basic = {}
        person_advanced = {}
        base_info = []
        for doc in tr.findAll(class_='person_info_r_1'):
            # 默认第一个节点
            # print(doc.find('td').getText())
            person_basic['name'] = doc.find('td').getText()
            # 根据属性特征获取相邻节点信息
            # print(doc.find('td', attrs={'align': 'right'}).getText()) 简历发布时间
        for doc in tr.findAll(class_='person_info_r_2'):
            # print(doc.find('a').getText())
            person_basic = person_bean.parser_person_basic(person_basic, doc.find('a').getText().split('，'))
            # print(base_url + doc.find('a').get('href'))
            ## person_advanced = person_advanced_parser(base_url + doc.find('a').get('href'))
        for doc in tr.select('.person_info_r_3 td'):
            base_info.append(doc.getText())
        # 封装 人员基本信息
        person_basic = person_bean.parser_person_base_info(person_basic, base_info)
        print(person_basic)
    return

# 人员简介解析
def person_advanced_parser():
    _url = 'http://job.91boshi.net/person.aspx?id=26260'
    resp = net_utils.do_post(_url,'true')
    soup = net_utils.resp_soup(resp)
    container = soup.find(id='person_div')
    for doc in container.findAll(class_='person_div_c_1'):
            print(doc.find('td').getText())


    for doc in container.findAll(class_='person_div_c_2'):
        print(doc.find('td').getText())




def save_person(p):
    person = person_bean.Person(p)
    dataHolder['persons'].append(person)
    return

# 表单提交
def form_sbmit():
    if dataHolder['page']['current'] == 1:
        # 第1页直接解析
        table_parser(dataHolder['resp']['pageView_1'])
        return

    paras = {
        '__EVENTTARGET': 'GridView1',
        '__EVENTARGUMENT': fmt_page_current(),
        '__LASTFOCUS': '',
        '__VIEWSTATE': dataHolder['form']['__VIEWSTATE'],
        '__EVENTVALIDATION': dataHolder['form']['__EVENTVALIDATION']
    }
    form_resp = net_utils.browser_post('http://job.91boshi.net/personnellist.aspx', paras)
    # print(form_resp.read().decode("gbk"))
    dataHolder['resp']['pageView_1'] = form_resp.read().decode("utf-8")
    table_parser(dataHolder['resp']['pageView_1'])
    return


# 格式化页码参数
def fmt_page_current():
    return 'Page$' + str(dataHolder['page']['current'])


# 循环解析
def loop_controller(endPageNum):
    while dataHolder['page']['current'] <= endPageNum:
        print("开始解析第" + str(dataHolder['page']['current']) + "页的数据：")
        dataHolder['doc']['doc_1'] = net_utils.resp_soup(dataHolder['resp']['pageView_1'])
        form = dataHolder['doc']['doc_1'].find(id="form1")
        dataHolder['form']['__VIEWSTATE'] = form.find('input', id='__VIEWSTATE')['value']
        dataHolder['form']['__EVENTVALIDATION'] = form.find('input', id='__EVENTVALIDATION')['value']
        form_sbmit()
        print_part_line()
        dataHolder['page']['current'] = dataHolder['page']['current'] + 1
    return


# 主函数
if __name__ == '__main__':
    # init_load()
    # loop_controller(1)
    person_advanced_parser()
