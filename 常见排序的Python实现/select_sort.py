a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for i in range(1, len(a)):
    print(a[i])


# 选择排序要注重range范围

def insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists


b = insert_sort(a)
print(b)
