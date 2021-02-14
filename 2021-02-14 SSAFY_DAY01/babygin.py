import sys

sys.stdin = open('babygin_input2.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    num = []
    Gin = False
    for i in range(6):
        num += [N % 10]
        N //= 10
    for i1 in range(len(num)):
        for i2 in range(len(num)):
            if i1 != i2:
                for i3 in range(len(num)):
                    if i3 != i2 and i3 != i1:
                        for i4 in range(len(num)):
                            if i4 != i3 and i4 != i2 and i4 != i1:
                                for i5 in range(len(num)):
                                    if i5 != i4 and i5 != i3 and i5 != i2 and i5 != i1:
                                        for i6 in range(len(num)):
                                            if i6 != i5 and i6 != i4 and i6 != i3 and i6 != i2 and i6 != i1:
                                                if num[i1] == num[i2] == num[i3] and num[i4] == num[i5] == num[i6]:
                                                    Gin = True
                                                if num[i1] == num[i2] == num[i3] and num[i4] + 1 == num[i5] and num[i5] + 1 == num[i6]:
                                                    Gin = True
                                                if num[i1] + 1 == num[i2] and num[i2] + 1 == num[i3] and num[i4] == num[i5] == num[i6]:
                                                    Gin = True
                                                if num[i1] + 1 == num[i2] and num[i2] + 1 == num[i3] and num[i4] + 1 == num[i5] and num[i5] + 1 == num[i6]:
                                                    Gin = True

    result = 'Baby Gin' if Gin else 'Lose'
    print('#%d %s' %(t, result))
