#-*- encoding=utf-8 -*-
import nmap
import time

list = []

def main():
    file_test = open('ip.txt')
    with file_test as f:
        text = f.read()
    length = len(text.splitlines())  # 读取文件计算文件的行数长度
    file_test.close()
    file_test = open('ip.txt')
    for i in range(0, length):  # 跟据文件的行数进行循环
        file_line = file_test.readline()
        remove_n = file_line.strip()  # 输出文件每行的内容
        list.append(remove_n)  # 将文件每行的内容加入list列表
        time.sleep(0.3)
    file_test.close()
main()

def portscaner():
    for host1 in list:
        try:
            n = nmap.PortScanner()
            n.scan(hosts=host1, arguments="-n -Pn -v -p 80,443,445")        #配置nmap参数,-p参数后面添加端口
            for x in n.all_hosts():
                host = x
                for y in n[x].all_protocols():
                    for z in n[x][y].keys():
                        port1 =  (host+':'+str(z))
                        print(port1)
                        ip_alive_port = open('ip_alive_port.txt', 'a')     #输出ip+端口至ip_alive_port.txt
                        ip_alive_port.write(port1)
                        ip_alive_port.write('\n')
                        ip_alive_port.close()
        except:pass

if __name__ == '__main__':
    portscaner()
