# dna最长片段问题

def dnad(i):
    length = 0
    try:
        while s[i] in dna:
            length += 1
            i += 1
    except:
        pass
    return length


def dna():
    s = input('please input a string:')
    dna = 'ATCG'
    leng = []
    for i in range(0, len(s)):
        if s[i] in dna:
            leng.append(dnad(i))
    try:
        c = max(leng)
        print(c)
    except:
        print(0)


# !全部运行通过



# 判断偶串

def oushu():
    s = input()
    for x in range(len(s), -2, -2):
        i = int(x / 2)
        s1 = s[0:i]
        s2 = s[i:x]
        if s1 == s2:
            print(x)
            break;
        while i == 0:
            print(0)


# 魔法币
'''小易准备去魔法王国采购魔法神器,购买魔法神器需要使用魔法币,但是小易现在一枚魔法币都没有,但是小易有两台魔法机器可以通过投入x(x可以为0)个魔法币产生更多的魔法币。
魔法机器1:如果投入x个魔法币,魔法机器会将其变为2x+1个魔法币
魔法机器2:如果投入x个魔法币,魔法机器会将其变为2x+2个魔法币
小易采购魔法神器总共需要n个魔法币,所以小易只能通过两台魔法机器产生恰好n个魔法币,小易需要你帮他设计一个投入方案使他最后恰好拥有n个魔法币。 '''


def magic_con():
    magic = []
    magic1 = []
    n = int(input())
    while n != 0:
        if n % 2 == 0:
            magic.append('2')
            n = n / 2 - 1

        else:
            magic.append('1')
            n = (n - 1) / 2
    for i in range(len(magic) - 1, -1, -1):
        magic1.append(magic[i])
    print((''.join(magic1)))


if __name__ == '__main__':
    magic_con()
