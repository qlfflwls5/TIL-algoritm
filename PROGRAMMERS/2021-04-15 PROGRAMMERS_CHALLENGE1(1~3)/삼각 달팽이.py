# 삼각 달팽이
# 정수 n이 매개변수로 주어집니다.
# 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후,
# 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

#     1
#   2   9
#  3  10  8
# 4  5  6  7


# 입출력 예
# n	result
# 4	[1,2,9,3,10,8,4,5,6,7]
# 5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
# 6	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]


# 방향은 아래, 오른쪽, 좌상의 반복이다.
# 그리고 숫자가 나아가는 횟수는 n일 때 방향마다 n, n-1, n-2, ..., 1로 줄어든다.
def solution(n):
    drc = [[1, 0], [0, 1], [-1, -1]]
    arr = [[0] * i for i in range(1, n + 1)]
    v, go, direction = 1, n, 0
    r, c = -1, 0
    while go:
        dr, dc = drc[direction % 3]
        for _ in range(go):
            r, c = r + dr, c + dc
            arr[r][c] = v
            v += 1
        go -= 1
        direction += 1

    answer = []
    for row in arr:
        answer.extend(row)
    return answer