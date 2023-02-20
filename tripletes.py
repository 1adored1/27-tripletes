f = open('file.txt')
N = int(f.readline())
first = []
second = []
third = []
for i in range(N):
    x, y, z = map(int, f.readline().split())
    first.append(x)
    second.append(y)
    third.append(z)
res = 0
diff_first = []
diff_second = []
for i in range(N):
    res += max(first[i], second[i], third[i])
    h = [first[i], second[i], third[i]]
    h = sorted(h)
    diff_first.append(h[2] - h[0])
    diff_second.append(h[2] - h[1])
diff = [] + diff_first + diff_second
diff = sorted(diff)
while res % 91 == 0:
    for i in range(len(diff)):
        res -= diff[i]
        if res % 91 != 0:
            break
        else:
            res += diff[i]
print(res)
