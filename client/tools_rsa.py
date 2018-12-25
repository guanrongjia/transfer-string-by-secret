# -*- coding: UTF-8 -*-
'''
# 一种非对称加密算法，公钥加密算法
'''
import rsa
from tools import smart_decode, save_key, read_key


def getKeys():
    '''
    随机生成公钥，私钥
    :return:
    '''
    (pubkey, privkey) = rsa.newkeys(1024)
    pub = pubkey.save_pkcs1()
    save_key(pub, 'public.pem')

    pri = privkey.save_pkcs1()
    save_key(pri, 'private.pem')


def rsa_encode(text):
    '''
    加密函数,使用公钥加密
    :param text: 明文
    :return:
    '''
    public_key = read_key('public.pem')
    public_key = rsa.PublicKey.load_pkcs1(public_key)
    text = smart_decode(text).encode('utf8')
    crypto = rsa.encrypt(text, public_key)
    return crypto


if __name__ == '__main__':
    getKeys()