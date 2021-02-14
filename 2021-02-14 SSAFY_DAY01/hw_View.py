import sys

sys.stdin = open("hw_View_input.txt")

for t in range(1, 11):
    N = int(input())
    B = list(map(int, input().split()))
    result = 0
    i = 2
    while i < N - 2:
        max_building = B[i-2]
        if B[i-1] > max_building:
            max_building = B[i-1]
        if B[i+1] > max_building:
            max_building = B[i+1]
        if B[i+2] > max_building:
            max_building = B[i+2]
        if B[i] > max_building:
            result += B[i] - max_building
            i += 3
        else:
            i += 1
    print('#%d %d' %(t, result))