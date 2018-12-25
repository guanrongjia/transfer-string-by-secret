#coding=utf8
import os
import sys
import types

def get_user_input(remind=None, input_range=None, validate_fun=None, args=None):
    '''
    捕获用户输入的功能函数，不允许为空
    :param remind:  指的是提示文字
    :param end_flag:  指的是输入结束符，
    :param validate_fun:  指的是输入验证函数，
    :return:
    '''
    user_input = ''
    remind = remind or u'请输入需要编码的内容，按enter结束！'
    input_range = [str(item) for item in input_range] if input_range else None
    print remind
    while not user_input:
        user_input = raw_input()
        user_input = str(user_input)
        user_input = user_input.strip()
        if user_input:
            if input_range and user_input not in input_range:
                print u'输入字符非法，可选输入为： %s' %  ' , '.join(input_range)
                user_input = ''
                continue
            if validate_fun and not validate_fun(user_input, args):
                user_input = ''
                continue
            return smart_decode(user_input)
        else:
            print u'请输入非空字符！'


def file_validate(path, args):
    '''
    功能函数，输入一个路径，判断其位置上的文件是否存在
    :param path: 文件绝对路径
    :return:
    '''
    dirname, filename = os.path.split(path)
    if not os.path.exists(path):
        print u'文件 %s 不存在' % filename
        return False
    return True


def key_validate(user_input, args):
    '''
    功能函数，验证输入字段的长度
    :param path: 文件绝对路径
    :return:
    '''
    if len(user_input) != args.get('length'):
        print u'输入长度不对错误，规定长度为：%s' % args.get('length')
        return False
    if not is_ascii(user_input):
        print u'输入数据必须全部为ASCII码，输入非法'
        return False

    return True


def save_key(key, name):
    file_path = get_path(name)
    with open(file_path, 'w') as file:
        file.write(key)


def read_key(name):
    file_path = get_path(name)
    with open(file_path, 'r') as file:
        key = file.read()
    return key


def get_path(name):
    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
    return os.path.join(dirname, name)


def smart_decode(text):
    """智能转码"""

    if type(text) == types.UnicodeType:
        return text
    elif not isinstance(text , types.StringTypes):
        text = str(text)

    try:
        return text.decode('utf8')
    except UnicodeDecodeError:
        try:
            return text.decode('gb2312')
        except UnicodeDecodeError:
            pass

    return text


def is_ascii(content):
    '''
    功能函数，判断是不是ASCII
    :param s:
    :return:
    '''
    return all(ord(char) < 128 for char in content)


if __name__ == '__main__':
    pass
    # get_user_input(input_range=[1, 2])


