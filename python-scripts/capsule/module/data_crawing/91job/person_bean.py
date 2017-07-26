# person_bean.py
import json


# 自定义人员类
class Person(object):
    # 基本信息
    _person_basic = {
        'name': '',
        'sex': '',
        'nation': '',
        'age': '',
        'marriage': '',
        'education': '',
        'household': '',
        'address': '',
        'height': '',
        'weight': '',
        'memType': '',
        'post_intention': '',
        'salary_require': '',
        'work_address': '',
        'major': ''
    }
    # 高级信息
    _person_advanced = {
        # 就业意向
        'employment_intention': '',
        # 工作特长
        'work_specialty': '',
        # 教育经历
        'educational_experience': '',
        # 工作经历
        'work_experience': '',
        # 特长
        'special_skill': '',
        # 职业目标
        'career_goals': '',
        # 自我介绍
        'self_introduction': ''
    }

    # 链式操作写入数据
    def _set_basic(self, basic):
        self._person_basic = basic
        return self

    def _set_advanced(self, advanced):
        self._person_advanced = advanced
        return self


# 信息解析 女，汉族，27岁，未婚，博士及以上学历，浙江省户籍，现住国外，身高168cm，体重48kg
def parser_person_basic(person_basic, arr):
    if len(arr) == 0:
        return person_basic
    arr[6] = arr[6].replace('现住', '')
    arr[7] = arr[7].replace('身高', '')
    arr[8] = arr[8].replace('体重', '')
    types = ['sex', 'nation', 'age', 'marriage', 'education', 'household', 'address', 'height', 'weight']
    index = 0
    for key in types:
        person_basic[key] = arr[index]
        index += 1
    return person_basic


# 解析 [ 人才类型：应届毕业生 , 意向岗位：科技管理 , 月薪要求：面议 , 希望工作地：,所学专业：有机催化　]
# 双层解析 取第二个
def parser_person_base_info(person_basic, arr):
    if len(arr) == 0:
        return person_basic
    types = ['memType', 'post_intention', 'salary_require', 'work_address', 'major']
    index = 0
    for key in arr:
        items = key.split('：')
        person_basic[types[index]] = items[1].replace('\u3000', '')  # 删除中文全角空格
        index += 1
    return person_basic


# Test
if __name__ == '__main__':
    #  新建对象 Person
    person = Person()
    basic = {
        'name': '1',
        'nation': '2',
        'age': '3',
        'marriage': '4',
        'education': '5',
        'household': '6',
        'address': '7',
        'height': '8',
        'weight': '9',
        'memType': '10',
        'post_intention': '11',
        'salary_require': '12',
        'major': '13'
    }
    advanced = {
        # 就业意向
        'employment_intention': '14',
        # 工作特长
        'work_specialty': '15',
        # 教育经历
        'educational_experience': '16',
        # 工作经历
        'work_experience': '17',
        # 特长
        'special_skill': '18',
        # 职业目标
        'career_goals': '19',
        # 自我介绍
        'self_introduction': '20'
    }
    person._set_basic(basic)._set_advanced(advanced)
    # 打印对象内部元素
    print(person._person_basic)
    print(person._person_advanced)
    # 类型帮助信息
    print('类型帮助信息: ', Person.__doc__)
    # 类型名称
    print('类型名称:', Person.__name__)
    # 类型所继承的基类
    print('类型所继承的基类:', Person.__bases__)
    # 类型字典
    print('类型字典:', Person.__dict__)
    # 类型所在模块
    print('类型所在模块:', Person.__module__)
    # 实例类型
    print('实例类型:', Person().__class__)
