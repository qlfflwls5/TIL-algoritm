# 대각선 출력하기
# 주어진 텍스트를 그대로 출력하세요.

#   #++++
#   +#+++
#   ++#++
#   +++#+
#   ++++#


# '+' 0개 + '#' 1개 + '+' 4개,
# '+' 1개 + '#' 1개 + '+' 3개 ...의 규칙이다.
for i in range(5):
    print('+' * i + '#' + '+' * (4 - i))


#2 .insert()를 사용
for i in range(5):
    n = ['+', '+', '+', '+']
    n.insert(i, '#')
    print(''.join(n))


#3 index를 활용
for i in range(5):
    for j in range(5):
        if i == j:
            print('#', end='')
        else:
            print('+', end='')
    print()