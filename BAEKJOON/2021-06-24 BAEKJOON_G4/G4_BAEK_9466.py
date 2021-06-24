# 텀 프로젝트
# 이번 가을학기에 '문제 해결' 강의를 신청한 학생들은 텀 프로젝트를 수행해야 한다. 프로젝트 팀원 수에는 제한이 없다.
# 심지어 모든 학생들이 동일한 팀의 팀원인 경우와 같이 한 팀만 있을 수도 있다.
# 프로젝트 팀을 구성하기 위해, 모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택해야 한다.
# (단, 단 한 명만 선택할 수 있다.) 혼자 하고 싶어하는 학생은 자기 자신을 선택하는 것도 가능하다.

# 학생들이(s1, s2, ..., sr)이라 할 때, r=1이고 s1이 s1을 선택하는 경우나,
# s1이 s2를 선택하고, s2가 s3를 선택하고,..., sr-1이 sr을 선택하고, sr이 s1을 선택하는 경우에만 한 팀이 될 수 있다.

# 예를 들어, 한 반에 7명의 학생이 있다고 하자. 학생들을 1번부터 7번으로 표현할 때, 선택의 결과는 다음과 같다.
# 1 2 3 4 5 6 7
# 3 1 3 7 3 4 6

# 위의 결과를 통해 (3)과 (4, 7, 6)이 팀을 이룰 수 있다. 1, 2, 5는 어느 팀에도 속하지 않는다.
#
# 주어진 선택의 결과를 보고 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산하는 프로그램을 작성하라.


# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫 줄에는 학생의 수가 정수 n (2 ≤ n ≤ 100,000)으로 주어진다.
# 각 테스트 케이스의 둘째 줄에는 선택된 학생들의 번호가 주어진다. (모든 학생들은 1부터 n까지 번호가 부여된다.)


# 출력
# 각 테스트 케이스마다 한 줄에 출력하고, 각 줄에는 프로젝트 팀에 속하지 못한 학생들의 수를 나타내면 된다.


# python3 - 4.2초, pypy - 1.4초 -> 백준 31등
# dict.keys(), dict.values()는 set과 같은 순회 시간복잡도를 갖는다.
for _ in range(int(input())):
    N = int(input())
    data = [0] + list(map(int, input().split()))
    visited = [0] * (N + 1)
    result = 0
    for i in range(1, N + 1):
        # 이미 싸이클에 포함된 학생
        if visited[i]:
            continue
        
        # 내가 고른 학생이 이미 싸이클에 포함되었거나 팀에 속하지 못하게 된 학생
        if visited[data[i]]:
            visited[i] = 1
            result += 1
            continue

        idx = i
        cnt = 0
        cycle = dict()
        while True:
            visited[idx] = 1
            cycle[idx] = cnt
            if data[idx] in cycle.keys():
                result += cycle[data[idx]]
                break

            if visited[data[idx]]:
                result += len(cycle)
                break

            idx = data[idx]
            cnt += 1

    print(result)


# 2
# dict를 이용해서 인덱싱을 하고 set을 별도로 사용 -> pypy 1.6초, 메모리 많이 사용
# for _ in range(int(input())):
#     N = int(input())
#     data = [0] + list(map(int, input().split()))
#     visited = [0] * (N + 1)
#     result = 0
#     for i in range(1, N + 1):
#         # 이미 싸이클에 포함된 학생
#         if visited[i]:
#             continue
#
#         idx = i
#         cnt = 0
#         cycle_dict = {idx: cnt}
#         cycle = {idx}
#         while True:
#             visited[idx] = 1
#             cycle.add(idx)
#             cycle_dict[idx] = cnt
#             if data[idx] in cycle:
#                 result += cycle_dict[data[idx]]
#                 break
#
#             if visited[data[idx]]:
#                 result += len(cycle)
#                 break
#
#             idx = data[idx]
#             cnt += 1
#
#     print(result)


# 3
# 리스트 -> 시간초과
# for _ in range(int(input())):
#     N = int(input())
#     data = [0] + list(map(int, input().split()))
#     visited = [0] * (N + 1)
#     result = 0
#     for i in range(1, N + 1):
#         # 이미 싸이클에 포함된 학생
#         if visited[i]:
#             continue
#
#         idx = i
#         cycle = []
#
#         while True:
#             visited[idx] = 1
#             cycle.append(idx)
#             if data[idx] in cycle:
#                 result += cycle.index(data[idx])
#                 break
#
#             if visited[data[idx]]:
#                 result += len(cycle)
#                 break
#
#             idx = data[idx]
#
#     print(result)
