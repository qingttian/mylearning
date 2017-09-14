# 求相反数

def xiangfanshu():
    import sys
    s = sys.stdin.readline().strip()
    sd = ''
    for i in range(len(s), 0, -1):
        x = i - 1
        sd += s[x]
    if len(s) == 1:
        if s == '0':
            print(0)
        else:
            print(int(s) + int(s))
    elif sd[0] != '0':
        summ = int(s) + int(sd)
        print(summ)
    else:
        cnt = 1
        try:
            while s[cnt] == '0':
                cnt += 1
            else:
                sdd = sd[cnt:]
                print(int(s) + int(sdd))
        except:
            sdd = sd[cnt:]
            print(int(s) + int(sdd))


def fengge():
    import sys
    tables = []
    s = sys.stdin.readline().strip()
    i = 0
    cnt = 1
    summ = 0
    count = 0
    while i < len(s):
        try:
            while s[i] == s[i + 1]:
                cnt += 1
                i += 1
            else:
                tables.append(cnt)
                cnt = 1
                i += 1
        except:
            tables.append(cnt)
            cnt = 0
            i += 1
    for x in tables:
        summ += x
        count += 1
    print(summ / count)


def beishu():
    import sys
    s = int(sys.stdin.readline().strip())
    n = 2 * s
    list1 = []
    list2 = []
    list3 = []
    for i in range(0, n, 2):
        a = sys.stdin.readline().strip()
        list1.append(int(i))
    for x in range(1, n, 2):
        b = sys.stdin.readline().strip()
        for j in b:
            list2.append(int(j))
        list3.append(list2)
    for n in range(s):
        print('YSE')


if __name__ == "__main__":
    #    xiangfanshu()
    fengge()
    # beishu()
