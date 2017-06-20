# person_bean.py
import json

# 自定义类
class Person:
    # 基本信息
    basic_info = {
        'name': '',
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
        'major': ''
    }
    # 就业意向
    employment_intention = ""
    # 工作特长
    work_specialty = ""
    # 教育经历
    educational_experience = ""
    # 工作经历
    work_experience = ""
    # 特长
    special_skill = ""
    # 职业目标
    career_goals = ""
    # 自我介绍
    self_introduction = ""

    # 初始化
    def __init__(self, basic_info):
        self.basic_info = basic_info
