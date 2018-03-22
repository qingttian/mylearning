
'''#coding=utf-8
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
'''

def stringd():
    a = input()
    b = ''
    c = ''
    d = 0
    for i in range(0,len(a)):
        if a[i].isdigit():
            b = b +a[i]
            for j in range(i+1,len(a)):
                if a[j].isdigit():
                    b = b+ a[j]
                else:
                    break
        if len(b) >= d:
            c = b
            d = len(b)
        else:pass
        b = ''
    print(c+','+str(len(c)))



def cheng():
    a = int(input())
    b = int(input())
    print(a*b)


# 字节流
def zijieliu():
    n = int(input())
    a = input().split()
    b = int(input())
    c = int(input())
    d = int(input())



if __name__ == "__main__":
    stringd()
#    cheng()