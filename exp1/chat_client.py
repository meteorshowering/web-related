import socket
from threading import Thread
import time

#echo端口：10000
#聊天室：10001

BUFFER_SIZE = 1024


class Client():
    def __init__(self):
        #---------------------------------------------
        # TODO： 初始化客户端socket
        self.domain=socket.AF_INET#ipv4 
        self.type=socket.SOCK_STREAM#tcp stream sockets
        self.protocol=socket.IPPROTO_TCP
        self.client = socket.socket(self.domain,self.type,self.protocol)
        #创建socket
        #---------------------------------------------
        self.ip, self.port = self.set_ip_port()  # 通过命令行标准输入，设置服务器IP与端口


    def set_ip_port(self):
        print("请输入聊天服务器IP")
        ip = input()
        #ip = "127.0.0.1"##
        #ip="101.6.65.34"
        print("请输入聊天服务器端口")
        port = input()
        return ip,int(port)

    def start_connection(self):
        #---------------------------------------------
        # TODO： 通过socket连接至对应IP与端口
        # self.client.XXXXXX
        self.client.connect((self.ip,self.port))
        #---------------------------------------------
        print("与" + self.ip + "连接建立成功，可以开始聊天了！（输入q断开连接）")
        # 为接受消息和发送消息分别开启两个线程，实现双工聊天
        Thread(target=self.send_msg).start()
        Thread(target=self.recv_msg).start()
        #self.send_msg()




    def send_msg(self):
        #---------------------------------------------
        # TODO： 在本函数中实现Socket消息的接收，并实现输入q退出的功能
        # 提示：需要循环结构
        while True:
            data=input()
            self.client.send(bytes(data,'utf-8'))
            if data=='q':
                self.client.close()
                break
            #取消多线程的代码
          #  time.sleep(1)
           # self.recv_msg()

        #---------------------------------------------
        a = 1


    
    def recv_msg(self):
        #---------------------------------------------
        # TODO： 在本函数中实现Socket消息的接收
        # 提示：需要循环结构
        # 提示：send_msg子进程退出并关闭socket时会报错，因此需要用try except结构进行异常处
        #---------------------------------------------
        try:
            # 可能报错的语句
            while True:
                data=self.client.recv(BUFFER_SIZE)
                print(str(self.ip)+' : '+data.decode('utf-8'))
                #取消多线程之后的代码：
              #  time.sleep(1)
              #  self.send_msg()
            a = 1    
        except:
            # 如果报错了，则执行下面的内容（退出循环）
            print("聊天已结束")
            self.client.close()
            b = 1




if __name__ == '__main__':
    client = Client()
    client.start_connection()