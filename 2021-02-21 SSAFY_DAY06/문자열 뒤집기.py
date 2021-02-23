# 문자열 뒤집기


# 입력
# 5
# abcdefg
# ABCdef1234
# a
# abc
# aabb


# 출력
# #1 gfedcba
# #2 4321fedCBA
# #3 a
# #4 cba
# #5 bbaa


# 1
T = int(input())
for t in range(1, T+1):
    word = input()
    result = ''
    for i in range(len(word)):
        result = word[i] + result

    print('#%d %s' %(t, result))


# 2
T = int(input())
for t in range(1, T+1):
    word = list(input())
    for i in range(len(word)//2):
        word[i], word[-1-i] = word[-1-i], word[i]

    print('#%d %s' %(t, ''.join(word)))