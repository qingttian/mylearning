# 例一
# coding = utf-8
def example_1():
    import sys
    for line in sys.stdin:
        a = line.split()
        print(int(a[0]) + int(a[1]))


# 例二：
def example_2():
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


# 题目一:最大子列和
def maxsquence():
    import sys
    num = []
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip().split(' ')
    for i in s:
        num.append(int(i))
    maxsum = 0
    for m in range(0, n):
        thissum = 0
        for j in range(0, n):
            thissum += num[j]
            if thissum > maxsum:
                maxsum = thissum
    print(maxsum)


def bubble_sort():
    import sys
    num = []
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip().split(' ')
    for m in range(0,len(s)):
        num.append(int(s[m]))
    for i in range(0, n):
        for j in range(i+1, n):
            if num[i] > num[j]:
                num[j], num[i] = num[i], num[j]
    print(" ".join(str(k) for k in num))

if __name__ == "__main__":
    #    maxsquence()
    bubble_sort()
