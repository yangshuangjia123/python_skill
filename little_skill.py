#颠倒字符串
def string_inversion(s):
    s = s[::-1]
    return s

#math.floor(num) 下舍整数-12.2 会变成 -13
def drop_down_integer(num):
    import math
    num = math.floor(num)
    return num

#format拼接字符串和变量
def format_method():
    a = "{a} test {b}".format(a=1,b=2)
    print(a)
    b = "{} test {}".format(1,2)
    print(b)

#首个字符变成大写
def capitalize():
    info = "abc"
    print(info.capitalize())
    print(info.title())

#，字符串居中，右侧空白可能比左面多一个
def string_center():
    s = "center"
    s = s.center(20)
    print(s)

def list_operation():
    #列表去重(可能改变内部顺序)
    l0 = [3,2,1,3,2,1]
    l0 = list(set(l0))
    print(l0)
    #判断列表为空
    l1 = []
    if not l1:
        print("列表为空")
    #列表运算
    l2 = [4,3,2,1,6,7]
    l3 = [4,5,6]
    l4 = set(l2)&set(l3)
    l5 = set(l2)|set(l3)
    l6 = set(l2)-set(l3)
    print(l4)
    print(l5)
    print(l6)

def get_ip():
    import socket
    domain = "baidu.com"
    ip = socket.getaddrinfo(domain, 'http')[0][4][0]
    print(ip)

if __name__ == '__main__':
    get_ip()