'''
获取随机参数

['参数1|类型|是否必传|默认值','参数1|类型|是否必传|默认值1,默认值2']

类型 : int, string, time
是否必传 : 1 : 是 , 0 : 否
'''


from faker import Faker
import random

f = Faker(locale='zh_CN')
PARAM_NAME = 0
PARMA_TYPE = 1
PARAM_MUST = 2
PARAM_DAFULT = 3

def _get_by_type(type, default_value):
    '''根据类型及默认值获取随机值'''

    if default_value:
        all_value = default_value.split(',')
        
        if len(all_value) > 1:
            default_value = all_value[random.randint(0, len(all_value) - 1)]
        if type == 'int':
            default_value = int(default_value) 
        return default_value
    else:
        if type == 'int':
            return random.randint(0,100)
        if type == 'string':
            return str(f.name())
        if type == 'time':
            # f.date(pattern="%Y-%m-%d  %H:%i:%S", end_datetime=None)
            return str(f.date_time_this_year())

def get_param(param_list):
    '''获取json格式的数据'''
    
    param_temp = {}

    for param in param_list:

        co = param.split('|')
        param_name = co[PARAM_NAME]
        param_default_value = co[PARAM_DAFULT]
        
        if co[PARAM_MUST] == '1':
            param_temp.update({param_name: _get_by_type(co[PARMA_TYPE], param_default_value)})
        else: 
            if random.randint(0,1):
                param_temp.update({param_name: _get_by_type(co[PARMA_TYPE], param_default_value)})

    return param_temp

if __name__ == "__main__":
    for i in range(0, 10):
        print(get_param(['name|string|1|', 'age|int|1|1', 'birthday|time|1|']))