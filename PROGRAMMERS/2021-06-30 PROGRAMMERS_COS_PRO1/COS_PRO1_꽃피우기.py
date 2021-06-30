# 꽃피우기
# 정사각형 크기 격자 모양 정원에 칸마다 핀 꽃 또는 피지 않은 꽃을 심었습니다.
# 이 정원의 꽃이 모두 피는 데 며칠이 걸리는지 알고 싶습니다. 핀 꽃은 하루가 지나면 앞, 뒤, 양옆 네 방향에 있는 꽃을 피웁니다.
# 현재 정원의 상태를 담은 2차원 리스트 garden이 주어졌을 때, 모든 꽃이 피는데 며칠이 걸리는지 return 하도록 solution 함수를 작성해주세요.


# 매개변수 설명
# 현재 정원 상태를 담은 2차원 리스트 garden이 solution 함수의 매개변수로 주어집니다.


# 정원의 한 변의 길이는 2 이상 100 이하입니다.
# 정원 상태를 담은 2차원 리스트 garden의 원소는 0 또는 1 입니다.
# 이미 핀 꽃은 1로 아직 피지 않은 꽃은 0으로 표현합니다.
# 정원에 최소 꽃 한 개는 피어 있습니다.
# return 값 설명
# 꽃이 모두 피는데 며칠이 걸리는지 return 합니다.


# 예제
# garden	return
# [[0, 0, 0], [0, 1, 0], [0, 0, 0]]	2
# [[1, 1], [1, 1]]	0


drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def solution(garden):
    # 여기에 코드를 작성해주세요.
    N = len(garden)
    queue = []
    rear = 0
    for i in range(N):
        for j in range(N):
            if garden[i][j]:
                queue.append((i, j))

    while rear < len(queue):
        r, c = queue[rear]
        rear += 1
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not garden[nr][nc]:
                garden[nr][nc] = garden[r][c] + 1
                queue.append((nr, nc))

    answer = 0
    for i in range(N):
        for j in range(N):
            answer = max(answer, garden[i][j])

    return answer - 1


print(solution([[1, 0, 0], [0, 0, 0], [0, 0, 1]]))