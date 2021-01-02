#-*- encoding=utf-8 -*-

from IPy import IP

test_ip = input('输入需要扫描的IP段：')

ip = IP(test_ip)
for x in ip:                       #循环输出IP
    ip1 = str(x)
    ip_pool = open('ip_pool.txt','a')
    ip_pool.write(ip1)
    ip_pool.write('\n')
    ip_pool.close()                #将遍历的ip写入ip_pool.txt文件
