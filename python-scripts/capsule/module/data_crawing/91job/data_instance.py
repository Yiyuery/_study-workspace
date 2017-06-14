# data_instance.py

INSTANCE = {
    'form': {
        '__EVENTTARGET': 'GridView1',
        '__EVENTARGUMENT': 'Page$2',
        '__LASTFOCUS': '',
        '__VIEWSTATE': '',
        '__EVENTVALIDATION': ''
    },
    'page': {
        'current': 1
    }
}

# 设置INSTANCE实例数据
def setKeyVal(instance, key, val):
    INSTANCE[instance][key] = val
    return INSTANCE[instance]

# 获取实例参数
def get_instance(key):
    return INSTANCE[key]

