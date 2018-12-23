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
    getKeys()
    public_key = read_key('public.pem')
    public_key = rsa.PublicKey.load_pkcs1(public_key)
    text = smart_decode(text).encode('utf8')
    crypto = rsa.encrypt(text, public_key)
    return crypto

def rsa_decode(text):
    '''
    解密函数，使用私钥解密
    :param text:密文
    :return:
    '''
    private_key = read_key('private.pem')
    private_key = rsa.PrivateKey.load_pkcs1(private_key)
    message = rsa.decrypt(text, private_key)
    return message

if __name__ == '__main__':
    pass