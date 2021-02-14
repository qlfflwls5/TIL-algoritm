T = int(input())

for t in range(1, T + 1):
    N = int(input())
    won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = ['0'] * 8
    for i in range(len(won)):
        if N // won[i] > 0:
            result[i] = str(N // won[i])
            N -= won[i] * (N // won[i])

    ans = ' '.join(result)
    print('#%d %s' %(t, ans))