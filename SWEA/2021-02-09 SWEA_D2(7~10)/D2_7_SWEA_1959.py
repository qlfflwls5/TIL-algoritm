# 두 개의 숫자열
# N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.

# Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
# 단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.

# 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.
# 위 예제의 정답은 아래와 같이 30 이 된다.


# [제약 사항]
# N 과 M은 3 이상 20 이하이다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
# 두 번째 줄에는 Ai,
# 세 번째 줄에는 Bj 가 주어진다.


# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


import sys

sys.stdin = open("1959_input.txt")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    # 긴 것을 L에, 짧은 것을 S에 넣고 시작할 것이다.
    if len(Ai) >= len(Bj):
        L, S = Ai, Bj
    else:
        L, S = Bj, Ai

    # 긴 것의 길이에서 짧은 것의 길이를 뺀 것에 1을 더한 만큼 하는 이유: 슬라이딩 윈도우
    # 매 순회마다 각 슬라이딩 윈도우에서의 temp_sum을 구하고 그들 중 max_sum인 것을 찾을 것이다.
    for i in range(len(L)-len(S)+1):
        temp_sum = 0
        # temp_sum은 긴 것 입장에서는 j(i)번째에서 시작, 짧은 것 입장에서는 0번째, 즉 j-i번째부터 시작한다.
        for j in range(i, i+len(S)):
            temp_sum += L[j] * S[j-i]
        # 초기 max_sum은 i가 0번째인 것으로 설정한다.
        if i == 0:
            max_sum = temp_sum
        if temp_sum > max_sum:
            max_sum =temp_sum

    print('#%d %d' %(t, max_sum))

# float('inf')
