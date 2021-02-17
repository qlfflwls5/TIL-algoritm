# 입력으로 1개의 정수 N 이 주어진다.
# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.
 

# [제약사항]
# N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)
 

# [입력]
# 입력으로 정수 N 이 주어진다.


# [출력]
# 정수 N 의 모든 약수를 오름차순으로 출력한다.


# N을 i로 나누었을 때 나머지가 0이면 i를 N의 '약수'라고 한다.
n = int(input())
divisor_list = []
for i in range(1, n + 1):
    if n % i == 0:
        # 이후에 사이에 공백을 넣기 위해 .join()을 사용하려면 모든 리스트의 요소가 str이어야 한다.
        divisor_list.append(str(i))
print(' '.join(divisor_list))