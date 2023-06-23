import matplotlib.pyplot as plt

#分组数
TCPnum_in=0
UDPnum_in=0
TCPnum_out=0
UDPnum_out=0
ICMPnum=0

#总数据量
TCPLength=0
UDPLength=0
ICMPLength=0

#fragment
all_fragment_in=0
all_fragment_out=0
fragment_in=0
fragment_out=0
#datagram
datagram=[]
TCPdatagram_in=[]
UDPdatagram_in=[]
TCPdatagram_out=[]
UDPdatagram_out=[]
#dataprocess
file = open("D:\dasanshang\exp_packets.pcapIn.txt", 'r')
for line in file.readlines():
    all_fragment_in=all_fragment_in+1
    line = line.strip('\n')         # 除去换行
    line = line.split(' ')          # 文件以“ ”分隔
    #print(line)
    if "" in line:                  # 解决每行结尾有空格的问题
        line.remove("")
    if line[4] == "06":
        #TCP
        TCPnum_in=TCPnum_in+1
        #TCPLength=TCPLength+int(line[1])
        if int(line[1]) not in TCPdatagram_in:
            TCPdatagram_in.append(int(line[1]))
    elif line[4] == "11":
        #UDP
        UDPnum_in=UDPnum_in+1
        #UDPLength=UDPLength+int(line[1])
        if int(line[1]) not in UDPdatagram_in:
            UDPdatagram_in.append(int(line[1]))
    if line[3] == "1":
        fragment_in=fragment_in+1
file.close()

file = open("D:\dasanshang\exp_packets.pcapOut.txt", 'r')
for line in file.readlines():
    line = line.strip('\n')         # 除去换行
    line = line.split(' ')          # 文件以“ ”分隔
    all_fragment_out=all_fragment_out+1
    if "" in line:                  # 解决每行结尾有空格的问题
        line.remove("")
    if line[4] == "06":
        #TCP
        TCPnum_out=TCPnum_out+1
        #TCPLength=TCPLength+int(line[1])
        if int(line[1]) not in TCPdatagram_out:
            TCPdatagram_out.append(int(line[1]))
    elif line[4] == "11":
        #UDP
        UDPnum_out=UDPnum_out+1
        #UDPLength=UDPLength+int(line[1])
        if int(line[1]) not in UDPdatagram_out:
            UDPdatagram_out.append(int(line[1]))
    if line[3] == "1":
        fragment_out=fragment_out+1
    if int(line[1]) not in datagram:
        datagram.append(int(line[1]))
file.close()

#print("接收的总分组量："+str(all_fragment_in))
print("接收的被分片的分组数目："+str(fragment_in))
print("接收的TCP分组："+str(TCPnum_in))
print("接收的id不同的TCP分组数目："+str(len(TCPdatagram_in)))
print("接收的UDP分组数目："+str(UDPnum_in))
print("接收的id不同的UDP分组数目："+str(len(UDPdatagram_in)))
print("")
#print("发出的总分组数目："+str(all_fragment_out))
print("发出的被分片的分组数目："+str(fragment_out))
print("发出的TCP分组数目："+str(TCPnum_out))
print("发出的id不同的TCP分组数目："+str(len(TCPdatagram_out)))
print("发出的UDP分组数目："+str(UDPnum_out))
print("发出的id不同的UDP分组数目："+str(len(UDPdatagram_out)))

'''
#picture
plt.rcParams['font.family']= 'SimHei'
plt.rcParams['axes.unicode_minus']=False
fenzu=[TCPnum,UDPnum,ICMPnum]
total=[TCPLength,UDPLength,ICMPLength]
plt.subplot(121)
plt.title('分组数')
plt.pie(fenzu,explode=[0.1,0.1,0.1],labels=['TCP','UDP','ICMP'],autopct='%1.1f%%')

plt.subplot(122)
plt.title('总数据量')
plt.pie(total,explode=[0.1,0.1,0.1],labels=['TCP','UDP','ICMP'],autopct='%1.1f%%')
plt.show()
'''


