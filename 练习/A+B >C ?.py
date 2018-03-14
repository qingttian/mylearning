d = []

def juage(x, y, z):
    if (x + y > z):
        d.append("true")
    else:
        d.append("flase")

x = int(input())
for i in range(0, x):
    a, b, c = (int(x) for x in input().split(" "))
    juage(a,b,c)
    print("Case #" + str(i) + ": " + d[i])