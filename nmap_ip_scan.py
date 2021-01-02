import nmap
import threading
import time

lock = threading.Lock()
opennum = 0
threads = []
time_start = time.time()

def portscaner():
    global opennum
    lock.acquire()

    try:
        n = nmap.PortScanner()
        n.scan(hosts="www.jju.edu.cn", arguments="-n -Pn -v -p 1-65535")        #配置nmap参数
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

    lock.release()

# def main():
#     setdefaulttimeout(0.1)
#     time_start = time.time()
#     for p in Port:
#         t = threading.Thread(target=portscaner)
#         threads.append(t)
#         t.start()
#     time_end = time.time()
#     time_length = time_end - time_start
#     for t in threads:
#         t.join()

if __name__ == '__main__':
    t1 = threading.Thread(target=portscaner())
    t1.start()
    for t1 in threads:
        t1.join()

time_end = time.time()
time_length = time_end - time_start
print('运行时间：'+str(time_length))