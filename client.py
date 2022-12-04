import socket
import struct
import os
import stat
import re
import sys
import time
import random

import FDFTPsocket



server_ip="8.218.117.184"
CLIENT_PORT = 7777
server_addr=(server_ip,CLIENT_PORT)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

FILE_SIZE = 1024
packet_struct = struct.Struct('I1024s')                   #格式  无符号整型+1024字节
file_name = "host_iperf.py"
Task = FDFTPsocket.Task(file_name)

#建立连接
def build_con():
    data = (file_name).encode('utf-8')
    Task.sendto(s,data,server_addr)

def sendto(s,end_flag,data,server_addr):
    Task.sendto(s,packet_struct.pack(*(end_flag,data)),server_addr)

def recv_ack():
    a=1

if __name__ == "__main__":

    build_con()
    f = open(file_name,"rb")                     #二进制读  ，data格式为 ` b''  `
    while True:
        data = f.read(FILE_SIZE)
        if str(data)!="b''":
            end_flag = 0
        else:
            data = 'end'.encode('utf-8')
            end_flag = 1
        sendto(s,end_flag,data,server_addr)
        if end_flag!=0:
            break
    Task.finish()
    s.close()
