import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
def load(filename):
    TCPSrc = []
    TCPDst = []
    UDPSrc = []
    UDPDst = []
    file = open(filename, 'r')
    for line in file.readlines():
        line = line.strip('\n')         # 除去换行
        line = line.split(' ')          # 文件以“ ”分隔
        if "" in line:                  # 解决每行结尾有空格的问题
            line.remove("")
        if line[3] == "06":
            TCPSrc.append(int(line[6]))
            TCPDst.append(int(line[7]))
        elif line[3] == "11":
            UDPSrc.append(int(line[6]))
            UDPDst.append(int(line[7]))
    file.close()
    TCPSrc.sort()
    TCPDst.sort()
    UDPSrc.sort()
    UDPDst.sort()
    return TCPSrc,TCPDst,UDPSrc,UDPDst

def load_Totallength(filename,Protocol,PortClass,PortNum):
    LengthList = []
    file = open(filename, 'r')
    if PortClass == "Dst":
        i = 7
    elif PortClass == "Src":
        i = 6
    for line in file.readlines():
        line = line.strip('\n')         # 除去换行
        line = line.split(' ')          # 文件以“ ”分隔
        if "" in line:                  # 解决每行结尾有空格的问题
            line.remove("")
        if line[3] != Protocol:
            continue
        if int(line[i]) == PortNum:
            LengthList.append(int(line[0]))
    file.close()
    LengthList.sort()
    return LengthList

TCPSrc,TCPDst,UDPSrc,UDPDst = load("/Users/liuguohao/Desktop/network/tryagain.pcapOut.txt")
number = Counter(TCPSrc) #传入列表
result = number.most_common() #使用most_common()函数
print('出现最多前十名端口为：{},{},{},{},{},{},{},{},{},{}'.format(result[0][0],result[1][0],result[2][0],result[3][0],result[4][0],result[5][0],result[6][0],result[7][0],result[8][0],result[9][0]))
i = 0
while i < 10:
    plotDataset = [[],[]]
    LengthListTCPInSrc = load_Totallength("/Users/liuguohao/Desktop/network/tryagain.pcapOut.txt","06","Src",result[i][0])
    count = len(LengthListTCPInSrc)
    for j in range(count):
        plotDataset[0].append(float(LengthListTCPInSrc[j]))
        plotDataset[1].append((j+1))
    print(plotDataset)
    plt.plot(plotDataset[0], plotDataset[1], '-', linewidth=2)
    plt.title("Cumulative distribution curve of IP packet length (Out;TCP;Source Port:{})".format(result[i][0]))
    plt.show()
    i = i + 1


TCPSrc,TCPDst,UDPSrc,UDPDst = load("/Users/liuguohao/Desktop/network/tryagain.pcapIn.txt")
number = Counter(TCPSrc) #传入列表
result = number.most_common() #使用most_common()函数
print('出现最多前十名端口为：{},{},{},{},{},{},{},{},{},{}'.format(result[0][0],result[1][0],result[2][0],result[3][0],result[4][0],result[5][0],result[6][0],result[7][0],result[8][0],result[9][0]))
i = 0
while i < 10:
    plotDataset = [[],[]]
    LengthListTCPInSrc = load_Totallength("/Users/liuguohao/Desktop/network/tryagain.pcapIn.txt","06","Src",result[i][0])
    count = len(LengthListTCPInSrc)
    for j in range(count):
        plotDataset[0].append(float(LengthListTCPInSrc[j]))
        plotDataset[1].append((j+1))
    print(plotDataset)
    plt.plot(plotDataset[0], plotDataset[1], '-', linewidth=2)
    plt.title("Cumulative distribution curve of IP packet length (Out;TCP;Source Port:{})".format(result[i][0]))
    plt.show()
    i = i + 1
"""
plt.figure(figsize=(136,4))
plt.hist(TCPSrc,50,(54100,54300))
plt.title('histogram for the source port distribution of TCP traffic (Oriention:Out)')
plt.show()
print(UDPSrc)
plt.figure(figsize=(136,4))
plt.hist(UDPSrc,bins=500)
plt.title('histogram for the source port distribution of UDP traffic (Oriention:Out)')
plt.show()
plt.figure(figsize=(136,4))
plt.hist(TCPDst,bins=50)
plt.title('histogram for the destination port distribution of TCP traffic (Oriention:Out)')
plt.show()
plt.figure(figsize=(136,4))
plt.hist(UDPDst,bins=50)
plt.title('histogram for the destination port distribution of UDP traffic (Oriention:Out)')
plt.show()
"""