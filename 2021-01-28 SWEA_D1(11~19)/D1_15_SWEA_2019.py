# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
# 주어질 숫자는 30을 넘지 않는다.


# 입력
# 8


# 출력
# 1 2 4 8 16 32 64 128 256


n = int(input())
result_list = []
for i in range(n + 1):
    result_list.append(str(2 ** i))

print(' '.join(result_list))
