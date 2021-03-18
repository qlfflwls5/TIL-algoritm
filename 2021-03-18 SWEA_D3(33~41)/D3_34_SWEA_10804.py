# 문자열의 거울상
# ‘b’, ‘d’, ‘p’, ‘q’로 이루어진 문자열이 주어진다. 이 문자열을 거울에 비추면 어떤 문자열이 되는지 구하는 프로그램을 작성하라.
# 예를 들어, “bdppq”를 거울에 비추면 “pqqbd”처럼 나타날 것이다.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 ‘b’, ‘d’, ‘p’, ‘q’만으로 이루어진 하나의 문자열이 주어진다. 문자열의 길이는 1이상 1000이하이다.


# [출력]
# 각 테스트 케이스마다 주어진 문자열을 거울에 비춘 문자열로 출력한다.


for t in range(1, int(input())+1):
    mirror = ''
    word = input()
    for c in word[::-1]:
        if c == 'b':
            mirror += 'd'
        elif c == 'd':
            mirror += 'b'
        elif c == 'q':
            mirror += 'p'
        elif c == 'p':
            mirror += 'q'

    print('#%d %s' % (t, mirror))

# mirror 리스트로 해도 되고 str로 해도 될 듯 -> 왜 리스트가 빠르지?