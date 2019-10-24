import os
from time import sleep
from sys import argv

def get_user():
    if len(argv) > 4:
        uname = argv[4]
    else:
        uname = input("输入用户标记名：")
    if check_uname(uname):
        dd = check_dd(uname)
    else:
        os.makedirs("./user/{}".format(uname))
        dd = False
    return dd, uname

def get_userId(userId):
    if check_log(userId):
        dd = check_log(userId)
    else:
        os.makedirs("./user/{}".format(userId))
        dd = False
    return dd, userId

def get_log(dd,userId):
    if not dd :
        print('创建新的userId:{}'.format(userId))
    a_log = get_a_log(userId)
    v_log = get_v_log(userId)
    return a_log, v_log

def check_uname(uname):
    __check_status = False
    if os.path.exists("./user/{}".format(uname)):
        __check_status = True
    return __check_status

def check_log(userID):
    __check_status = False
    if os.path.exists("./user/{}".format(userID)):
        __check_status = True
    return __check_status

def check_dd(uname):
    __dd_status = False
    if os.path.exists("./user/{}/dingding".format(uname)):
        __dd_status = True
    return __dd_status


def get_a_log(uname):
    __a_log = 0
    if os.path.exists("./user/{}/a_log".format(uname)):
        with open("./user/{}/a_log".format(uname), "r", encoding="utf8") as fp:
            __a_log = int(fp.read())
    else:
        with open("./user/{}/a_log".format(uname), "w", encoding="utf8") as fp:
            fp.write(str(__a_log))
    return __a_log


def get_v_log(uname):
    __v_log = 0
    if os.path.exists("./user/{}/v_log".format(uname)):
        with open("./user/{}/v_log".format(uname), "r", encoding="utf8") as fp:
            __v_log = int(fp.read())
    else:
        with open("./user/{}/v_log".format(uname), "w", encoding="utf8") as fp:
            fp.write(str(__v_log))
    return __v_log


def shutdown(stime):
    if stime:
        stime = int(stime)
        os.system('sudo shutdown -s -t {}'.format(stime))
        for i in range(stime):
            print("\r{}秒后关机".format(stime-i), end="")
            sleep(1)
    else:
        print("无自动关机任务，已释放程序内存，10分钟后窗口将自动关闭")
        sleep(600)
