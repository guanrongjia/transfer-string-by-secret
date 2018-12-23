#coding=utf8
from socket import *
from tools import get_user_input, file_validate, key_validate, save_key, smart_decode
from tools_aes import aes_encode
from tools_rsa import rsa_encode

target = ('127.0.0.1', 15324)
def get_header(name):
    leng = len(name)
    assert leng < 250
    return chr(leng) + name
 
def send_data(data):
    s = socket (AF_INET, SOCK_STREAM)
    s.connect(target)
    s.sendall (data)
    s.close()


if __name__ == '__main__':
    source_data = None
    secret_data = None
    encode_type = None
    while True:
        user_input = get_user_input(u'请选择模式传输内容的模式（输入序号）\n 1、手动输入字符\n 2、输入文件路径读取内容', [1, 2])
        if user_input == '1':
            source_data = get_user_input(u'请输入需要加密传输的内容')
        else:
            file_path = get_user_input(remind=u'请输入文件绝对路径，请注意输入可读文件！', validate_fun=file_validate)
            with open(file_path,  'r') as file:
                source_data = file.read()

        user_input = get_user_input(u'待发送的数据如下请确认（输入序号）\n %s \n 1、确认 \n 2、重新选择' % smart_decode(source_data), [1, 2])
        if user_input == '2':
            continue

        encode_type = get_user_input(u'请选择加密模式（输入序号）\n 1、AES-128 \n 2、AES-192 \n 3、AES-256\n 4、RSA-256', [1, 2, 3, 4])
        ascii_byte = str(int(encode_type) * 8 + 8)
        encode_type_map = {'1': 'AES-128', '2': 'AES-192', '3': 'AES-256', '4': 'RSA-256'}
        encode_type = encode_type_map.get(encode_type)
        if encode_type in ['AES-128',  'AES-192', 'AES-256']:
            key = get_user_input(remind=u'请输入自定义%s位ascii码作为key，将根据key生成堆成秘钥' % ascii_byte, validate_fun=key_validate, args={'length': int(ascii_byte)})
            save_key(key, u'key.bcp')
            secret_data = aes_encode(source_data, key)
        elif encode_type in ['RSA-256']:
            print u'选择使用RSA-256算法，即将随机生成公钥、私钥。。。'
            secret_data = rsa_encode(source_data)
        else:
            print u'选择错误，请重新执行。。。'
            continue
        print u'加密后数据为：'
        print secret_data
        print u'向服务器发送数据。。。'
        send_data(encode_type + secret_data)
        print u'发送数据成功，请查看服务器输出。。。'
        user_input = get_user_input(u'请问是否继续向服务器传输数据（输入序号） \n 1、继续 \n 2、退出',  [1, 2])
        if user_input == '1':
            continue
        else:
            break


    raw_input()