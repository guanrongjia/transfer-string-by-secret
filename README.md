## pwered by guanrongjia
@2018/12/19
all rights reserved

## 主要功能
程序主要模拟了网络中加密传输的过程，
包括加密和解密、传输的过程、
重点使用了rsa aes两个加密算法。

## 环境
电脑环境 window7 x64
需要python2.7
安装包rsa, Cryptodome
本实例在windows下运行

## 启动方法
启动工程，先启动server.py
然后启动client.py
根据提示，进行一系列操作
服务端监听本地端口号2409
客户端发送数据到2409
进行加密数据交互

## 支持的验证
### 版本1(第一次提交，可以从cimmit中拉下来)
可以支持中文、英文的加密
支持从文件中读取数据，也可以手写，
可以选择加密方式，
可以选择加密的key，
密码根据输入生成或者随机生成，保存在文件中，
注意： 1服务端和客户端因为这只是模拟，所以在同一个机器上，这个需要注意下
2：读取文件遗留一个问题，多行文本，没有转义，目前只能读取一行数据


### 版本2（客户端和服务端分离）
1、可以支持中文、英文的加密
2、支持从文件中读取数据，也可以手写，
3、可以选择加密方式
4、当选择AES加密方式的时候，密码以明文方式，存在key.bcp中，服务器和客户端都要存
密码只能是16，24,32位的ascii字符
5、当选择rsa的时候，密码是分别存储的，客户端的公钥为public.pem
 服务端的私钥为private.pem，密码是成对的，随机的，加密的。
 真实过程中，我们会服务器生成公钥和私钥之后，传递公钥给客户端，
 我们模拟的时候，为了简化，密码是生成好的分别存放于本地和服务端，
 当然在版本1中，我们也有生成密码的代码。
 
## 版本2 demo启动过程
0、启动快捷方式C:\Users\76527\Desktop\ShadowsocksR-dotnet4.0.exe
1、打开程序C:\Users\76527\Desktop\putty.exe
登录服务器
进来之后，依次输入：
cd /home/gitdata/transfer-string-by-secret/server/
python server.py
然后服务端就启动了，会持续监听消息，会把消息打印在控制台上

2、打开目录\transfer-string-by-secret\client
并在目录下启动power shell，在power shell中启动服务端程序： python client.py

3、在客户端按照提示输入数据，在服务端检查从客户端传入的数据

4、如果要更新aes的密钥，请分别在客户端和服务端的key.bcp中写入新的ascii字符串，
注意两个key.bcp的内容必须一致，且字符长度必须为16，24，36位。位数越高，加密等级越高
5、如果要更新rsa的密钥，请运行\transfer-string-by-secret\server\tools_rsa.py
然后把\transfer-string-by-secret\server\public.pem 移动到
\transfer-string-by-secret\client文件夹下，替换下面的public.pem文件


注意：1、为了简化模拟，没有做申请秘钥的过程，直接是把key存在文件中
2、因为客户端和服务端分离，所以填写ip的时候要注意监听服务端的ip

