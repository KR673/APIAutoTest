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

def _get_by_type(type, default_value, request_type):
    '''根据类型及默认值获取随机值'''
    string_value = ''
    if request_type == 'get':
        string_value = '{}'
    elif request_type == 'post':
        string_value = '"{}"'    

    if default_value:
        all_value = default_value.split(',')
        
        if len(all_value) > 1:
            default_value = all_value[random.randint(0, len(all_value) - 1)]

        if type == 'int':
            return default_value
        else:
            return string_value.format(default_value) 
    else:
        if type == 'int':
            return str(random.randint(0,100))
        if type == 'string':
            return string_value.format(str(f.name()))
        if type == 'time':
            # f.date(pattern="%Y-%m-%d  %H:%i:%S", end_datetime=None)
            return string_value.format(str(f.date_time_this_year()))

def _get_param(param_list, request_type):
    '''获取json格式的数据'''
    
    param_temp = []

    for param in param_list:

        co = param.split('|')
        param_name = co[PARAM_NAME]
        param_default_value = co[PARAM_DAFULT]
        
        param_format = ''
        if request_type == 'get':
            param_format = '{}={}'
        elif request_type == 'post':
            param_format = '"{}":{}'

        if co[PARAM_MUST] == '1':
            param_temp.append(param_format.format(param_name, _get_by_type(co[PARMA_TYPE], param_default_value, request_type)))
        else: 
            if random.randint(0,1):
                param_temp.append(param_format.format(param_name, _get_by_type(co[PARMA_TYPE], param_default_value, request_type)))

    return param_temp

def post_param(data_list):
    data = _get_param(data_list, 'post')
    return '{{{}}}'.format(';'.join(data))

def get_param(data_list):
    data = _get_param(data_list, 'get')
    return '&'.join(data)

if __name__ == "__main__":
    for i in range(0, 10):
        print(get_param(['name|string|1|', 'age|int|1|1', 'birthday|time|1|']))