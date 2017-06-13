# dict_utils.py
# From http://www.jb51.net/article/80791.htm
# 把Object对象转换成Dict对象
def convert_to_dict(obj):
    dict = {}
    dict.update(obj.__dict__)
    return dict


# 把对象列表转换为字典列表
def convert_to_dicts(objs):
    obj_arr = []
    for o in objs:
        # 把Object对象转换成Dict对象
        dict = {}
        dict.update(o.__dict__)
        obj_arr.append(dict)
    return obj_arr


# 把对象(支持单个对象、list、set)转换成字典
def class_to_dict(obj):
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__
    if is_list or is_set:
        obj_arr = []
        for o in obj:
            # 把Object对象转换成Dict对象
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict