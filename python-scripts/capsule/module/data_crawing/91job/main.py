# coding='utf-8'
# author:Yiyuery

import net_utils
import person_bean
import dict_utils
# import js_utils

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
    }
}


# 初始化加載
def init_load():
    dataHolder['resp']['pageView_1'] = net_utils.do_post(dataHolder['request']['url'], 'true')
    return


# 数据解析器
def resp_parser():
    dataHolder['doc']['doc_1'] = net_utils.resp_soup(dataHolder['resp']['pageView_1'])
    table = dataHolder['doc']['doc_1'].find('table', id='GridView1')
    table_parser_test(table)
    # person = person_bean.Person("haha")
    # person.educational_experience = "西安邮电大学-->北京大学"
    # print(dict_utils.convert_to_dict(person))
    return

def table_parser(resp):
    soup = net_utils.resp_soup(resp)
    table = soup.find('table', id='GridView1')
    table_parser_test(table)
    return


def table_parser_test(table):
    base_url = 'http://job.91boshi.net/'
    for tr in table.findAll(class_='person_info'):
        for doc in tr.findAll(class_='person_info_r_1'):
            # 默认第一个节点
            print(doc.find('td').getText())
            # 根据属性特征获取相邻节点信息
            print(doc.find('td', attrs={'align': 'right'}).getText())
        for doc in tr.findAll(class_='person_info_r_2'):
            print(doc.find('a').getText())
            print(base_url + doc.find('a').get('href'))
        for doc in tr.select('.person_info_r_3 td'):
            print(doc.getText())
        print('\n')
    return

def page_form():
    dataHolder['doc']['doc_1'] = net_utils.resp_soup(dataHolder['resp']['pageView_1'])
    form = dataHolder['doc']['doc_1'].find(id="form1")
    paras = {
        '__EVENTTARGET': 'GridView1',
        '__EVENTARGUMENT': 'Page$3',
        '__LASTFOCUS': '',
        '__VIEWSTATE': form.find('input', id='__VIEWSTATE')['value'],
        '__EVENTVALIDATION': form.find('input', id='__EVENTVALIDATION')['value']
    }
    form_resp = net_utils.browser_post('http://job.91boshi.net/personnellist.aspx', paras)
    table_parser(form_resp.read().decode("utf-8"))
    return

# 主函数
if __name__ == '__main__':
    init_load()
    # resp_parser()
    page_form()
    # resp_parser()