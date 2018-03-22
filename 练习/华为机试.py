def count():
    a = input()
    b = ''
    count = 0
    for i in range(len(a) - 1, -1, -1):
        b += a[i]
    for j in range(0, len(a)):
        if b[j] == ' ':
            print(count)
            exit(0)
        else:
            count += 1


# 明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤1000），对于其中重复的数字，只保留一个，把其余相同的数去掉，
# 不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作。
#
#
def sortd():
    while True:
        try:
            n = int(input())
            b = []
            for i in range(0, n):
                x = int(input())
                if not x in b:
                    b.append(x)
                else:
                    continue
            b.sort()
            for j in range(0, len(b)):
                print(b[j])
        except:
            break


def function():
    # coding=utf-8
    import sys
    for line in sys.stdin:
        a = line.split()
        print(int(a[0]) + int(a[1]))


def niuke():
    import sys
    q = input().split()
    a, b = int(q[0]), int(q[1])
    i = 2
    count = 0
    ansd = []
    while (i < b):
        if b % (a * i) == 0:
            count += 1
            ansd.append(i * a)
            i += 1
        else:
            i += 1
            pass
        if count == 2:
            print(ansd[0] + ansd[1])
            exit()
    print(-1)


def niuke1():
    a = input().split()
    b = []
    for i in a:
        b.append(int(i))
    while (len(b)):
        x = min(b)
        c = []
        for i in range(0, len(b)):
            if b[i] - x > 0:
                c.append(b[i] - x)
        if len(b) > 0:
            print(len(b))
        b = c


# 字符串分割
def char_fenge():
    a = input()
    b = input()

    def processd(x):
        leftd = len(x) % 8
        if leftd != 0:
            x += '0' * (8 - leftd)
        for i in range(0, int(len(x) / 8)):
            print(x[i * 8:(i + 1) * 8])

    processd(a)
    processd(b)


# 进制转换
def dec2hexd():
    while (True):
        try:
            print(int(input(), 16))
        except:
            exit()


# 质数因子
def zhishu():
    a = int(input())
    ansd = []
    i = 2
    b = a
    while (i < b + 1):
        while a % i == 0:
            a = a / i
            ansd.append(i)
        i += 1
    for x in ansd:
        print(x, end=' ')


# 取近似值
def similrity():
    a = float(input())
    print(round(a))


# 合并表记录
def indexd():
    a = int(input())
    b = [i for i in range(a)]
    for i in range(0, a):
        b[i] = [int(x) for x in input().split()]
    c = a
    for i in range(0, a):
        try:
            for j in range(i+1,a):
                if b[i][0] == b[j][0]:
                    b[i][1] += b[j][1]
                    b.pop(j)
                    a = len(b)
        except:
            pass
#    print(b)
    b.sort()
    for i in range(0,len(b)):
        print(b[i][0],end=" ")
        print(b[i][1])

if __name__ == "__main__":
    #    sortd()
    #    niuke()
    #    niuke1()
    #    char_fenge()
    #    dec2hexd()
    #     zhishu()
    #    similrity()
    indexd()



















#coding=utf-8
import sys
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))


#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)