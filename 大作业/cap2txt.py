from tkinter import filedialog
#fname = filedialog.askopenfilename()        #选择包文件，返回值是所选择文件的路径
fname = "/Users/liuguohao/Desktop/network/test.cap"
capfile = open(fname, 'rb')     #打开包文件
ftxt = open(fname+'.txt', 'w')      #在包文件路径下生成一个对应包文件名的记事本文件
ftxt.write(str(capfile.read()))     #将读取到的流数据转成字符串并写入记事本文件中
ftxt.close()        #关闭记事本文件
capfile.close()     #关闭包文件