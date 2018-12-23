#coding=utf8
import SocketServer
from tools_rsa import rsa_decode
from tools_aes import aes_decode
from tools import smart_decode
addr = ('127.0.0.1', 15324)
class MyTCPHandler (SocketServer.StreamRequestHandler):
    def handle (self):
        source_data = self.rfile.readline().strip()
        encode_type = source_data[:7]
        secret_data = source_data[7:]
        secret_data = smart_decode(secret_data)
        if encode_type.upper().startswith('AES'):
            print aes_decode(secret_data)
        elif encode_type.upper().startswith('RSA'):
            print rsa_decode(secret_data)
        else:
            print u'客户端传入数据不合法，请检查代码'


server = SocketServer.TCPServer(addr, MyTCPHandler)
server.serve_forever()
