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
    beishu()
