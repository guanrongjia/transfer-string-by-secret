#coding=utf8
from Cryptodome.Cipher import AES
from Cryptodome import Random
from tools import smart_decode, get_path

def aes_encode(data, key):
    '''
    aes加密
    :param data: 明文
    :param key: 用来加密的key，和解密的key是同一个，所以是对称加密
    :return:
    '''
    if len(key) not in [16, 24, 32]:
        print u'秘钥必须为16, 24, 32位'
        raise Exception
    data = smart_decode(data)
    key = smart_decode(key).encode('utf8')
    # 生成长度等于AES块大小的不可重复的密钥向量
    iv = Random.new().read(AES.block_size)
    # 使用key和iv初始化AES对象, 使用MODE_CFB模式
    mycipher = AES.new(key, AES.MODE_CFB, iv)
    # 加密的明文长度必须为16的倍数，如果长度不为16的倍数，则需要补足为16的倍数
    # 将iv（密钥向量）加到加密的密文开头，一起传输
    ciphertext = iv + mycipher.encrypt(data.encode('utf8'))
    return ciphertext


def aes_decode(data):
    '''
    aes解密
    :param ciphertext: 密文
    :param key: 用来解密的key，和加密的key是同一个，所以是对称加密
    :return:
    '''
    file_path = get_path(u'key.bcp')
    with open(file_path) as file:
        key = file.read()
    data = smart_decode(data)
    key = smart_decode(key).encode('utf8')
    # 解密的话要用key和iv生成新的AES对象
    mydecrypt = AES.new(key, AES.MODE_CFB, data[:16])
    # 使用新生成的AES对象，将加密的密文解密
    decrypttext = mydecrypt.decrypt(data[16:])
    return decrypttext.decode('utf8')


if __name__ == '__main__':
    pass