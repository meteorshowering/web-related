from tkinter import filedialog
from typing import Protocol

#fname = filedialog.askopenfilename()        #选择包文件，返回值是所选择文件的路径
fname = "/Users/liuguohao/Desktop/network/ok.pcap"
capfile = open(fname, 'rb')         # 打开包文件
ftxtOut = open(fname + 'Out.txt', 'w')      #在包文件路径下生成一个对应包文件名的记事本文件
ftxtIn = open(fname + 'In.txt', 'w')
LocalMAC = "147dda79c542"

try:
    # pcap文件的文件头处理
    GlobalHeader = capfile.read(24).hex()
    # 对于每一个pcap packet做处理
    while 1:
        # 从pcap packet包头中解析出packet的长度
        PacketHeader = capfile.read(16).hex()
        CapturedPacketLength = int(PacketHeader[16:18],16) + \
                        int(PacketHeader[18:20],16) * 256 + \
                        int(PacketHeader[20:22],16) * (256 ^ 2)+ \
                        int(PacketHeader[22:24],16) * (256 ^ 3)
        # 处理帧头
        FrameHeader = capfile.read(14).hex()
        # 如果是载荷为IPv4协议的帧，则提取数据
        if FrameHeader[24:28] == "0800":
            if FrameHeader[0:12] == LocalMAC:
                ftxt = ftxtIn
            elif FrameHeader[12:24] == LocalMAC:
                ftxt = ftxtOut
            # ftxt.write(FrameHeader[0:12] + " " + FrameHeader[12:24] + " ")
            HeaderLength = int(capfile.read(1).hex()[1],16) * 4
            Header = capfile.read(HeaderLength - 1).hex()
            TotalLength = int(Header[2:6],16)
            Identification = int(Header[6:10],16)
            Flags = bin(int(Header[10],16))[2:].zfill(4)
            DFFlag = Flags[1]
            MFFlag = Flags[2]
            protocol = Header[16:18]
            # SourceAddress = Header[22:30]
            SourceAddress = str(int(Header[22:24],16)) + "." + str(int(Header[24:26],16)) + "." + str(int(Header[26:28],16)) + "." + str(int(Header[28:30],16))
            # DestinationAddress = Header[30:38]
            DestinationAddress = str(int(Header[30:32],16)) + "." + str(int(Header[32:34],16)) + "." + str(int(Header[34:36],16)) + "." + str(int(Header[36:38],16))
            print(DestinationAddress)
            ftxt.write(str(TotalLength) + " " + str(Identification) + " " + DFFlag + " " + MFFlag + " " + protocol + " " + SourceAddress + " " + DestinationAddress + " ")
            if protocol == "06":
                #TODO:TCP协议报文段段头处理
                SourcePort = str(int(capfile.read(2).hex(),16))
                DestinationPort = str(int(capfile.read(2).hex(),16))
                RemainPacket = capfile.read(8).hex()
                Flags = bin(int(capfile.read(2).hex(),16))[2:].zfill(16)
                URGFlag = Flags[10]
                ACKFlag = Flags[11]
                PSHFlag = Flags[12]
                FlagRST = Flags[13]
                FlagSYN = Flags[14]
                FlagFIN = Flags[15]
                RemainPacket = capfile.read(CapturedPacketLength - 28 - HeaderLength).hex()
                ftxt.write(SourcePort + " " + DestinationPort + " " + URGFlag + " " + ACKFlag + " " + PSHFlag  + " " + FlagRST + " " + FlagSYN + " " + FlagFIN + "\n")
            elif protocol == "11":
                #TODO:UDP协议报文段段头处理
                SourcePort = str(int(capfile.read(2).hex(),16))
                DestinationPort = str(int(capfile.read(2).hex(),16))
                RemainPacket = capfile.read(CapturedPacketLength - 18 - HeaderLength).hex()
                ftxt.write(SourcePort + " " + DestinationPort + "\n")
            elif protocol == "01":
                #TODO:ICMP协议报文段段头处理
                RemainPacket = capfile.read(CapturedPacketLength - 14 - HeaderLength).hex()
                ftxt.write("\n")
            else:
                #TODO:其他
                RemainPacket = capfile.read(CapturedPacketLength - 14 - HeaderLength).hex()
                ftxt.write("\n")
        # 如果是载荷为IPv6的帧，则直接跳过
        else:
            PacketData = capfile.read(CapturedPacketLength - 14).hex()
except:
    capfile.close()     #关闭包文件
    ftxtIn.close()        #关闭记事本文件
    ftxtOut.close()        #关闭记事本文件
