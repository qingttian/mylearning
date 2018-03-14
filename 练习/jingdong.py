# coding = utf-8
def qqq():
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


def dongdong():
    import sys
    from math import sqrt
    cont = 0
    n = 1
    leng = []
    a = int(sys.stdin.readline().strip())
    n = sqrt(a)

    def summ(n):
        summd = 0
        for i in range(1, n + 1):
            summd += i
        return summd

    while a >= summ(n):
        n += 1
    else:
        print(n)

def dongdongdong():
    import sys
    cnt = 0
    cnt1 = 1
    s = sys.stdin.readline().strip()
    x = s.index(')')
    a = list(x)
    aa = []
    for i in range(0,len(s)):
        if i =='(':
            q = s[1:len(s)+1]
        for a in range(0,len(q)):
            if q(a) == ')':
                aa.append(a)
        for b in aa:
            qq = list(q)
             qqq = del(qq[a])

if __name__ == '__main__':
    dongdong()
