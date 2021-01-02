#-*- encoding:utf-8 -*-
from socket import *
import sys
import socket
import threading
import time

time_start = time.time()
lock = threading.Lock()
opennum = 0
threads = []

Port = [22,3306,1443,2021,6379,80,81,82,83,84,85,86,87,88,89,443,8080,8081,8082,8083,8084,8085,8086,8087,8088,8888,9080,9090,8089,9999,17000,7779,7777,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,8443,9443,8000,8001,8002,8003,8004,8005,8006,8007,8008,8009]

print('[*] Start scan')
# host = input('please input website:')
host = 'www.jju.edu.cn'
try:
    host_ip = socket.gethostbyname( host )
except :
    print('hostname could not resolved,exiting')
    sys.exit()
print('The website:'+ host + ' ip address is '+ host_ip)
print('[*] Show open port \n')

def portscaner(host_ip,port):
    global opennum
    lock.acquire()
    timeout = 6
    try:
        s = socket.socket()
        s.connect((host_ip,port))
        socket.timeout = timeout
        opennum+=1
        print('port: %d open'%port)
        s.close()
    except:pass
    lock.release()

def main():
    setdefaulttimeout(0.1)

    for p in Port:
        t = threading.Thread(target=portscaner,args=(host_ip,p))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('\n[*] The scan is complete!')
    print('[*] A total of %d open port ' % (opennum))


if __name__ == '__main__':
    main()

    time_end = time.time()
    time_length = time_end - time_start
    print('[*] The time is %.1fs'%time_length)
