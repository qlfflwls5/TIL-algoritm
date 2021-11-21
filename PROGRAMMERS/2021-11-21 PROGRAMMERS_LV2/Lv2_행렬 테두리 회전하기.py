# 행렬 테두리 회전하기
#
# rows x columns 크기인 행렬이 있습니다. 행렬에는 1부터 rows x columns까지의 숫자가 한 줄씩 순서대로 적혀있습니다.
# 이 행렬에서 직사각형 모양의 범위를 여러 번 선택해, 테두리 부분에 있는 숫자들을 시계방향으로 회전시키려 합니다.
# 각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현하며, 그 의미는 다음과 같습니다.
#
# x1 행 y1 열부터 x2 행 y2 열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전합니다.
#
# 행렬의 세로 길이(행 개수) rows, 가로 길이(열 개수) columns, 그리고 회전들의 목록 queries가 주어질 때, 각 회전들을 배열에 적용한 뒤,
# 그 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.


# 제한사항
# rows는 2 이상 100 이하인 자연수입니다.
# columns는 2 이상 100 이하인 자연수입니다.
# 처음에 행렬에는 가로 방향으로 숫자가 1부터 하나씩 증가하면서 적혀있습니다.
# 즉, 아무 회전도 하지 않았을 때, i 행 j 열에 있는 숫자는 ((i-1) x columns + j)입니다.
# queries의 행의 개수(회전의 개수)는 1 이상 10,000 이하입니다.
# queries의 각 행은 4개의 정수 [x1, y1, x2, y2]입니다.
# x1 행 y1 열부터 x2 행 y2 열까지 영역의 테두리를 시계방향으로 회전한다는 뜻입니다.
# 1 ≤ x1 < x2 ≤ rows, 1 ≤ y1 < y2 ≤ columns입니다.
# 모든 회전은 순서대로 이루어집니다.
# 예를 들어, 두 번째 회전에 대한 답은 첫 번째 회전을 실행한 다음, 그 상태에서 두 번째 회전을 실행했을 때 이동한 숫자 중 최솟값을 구하면 됩니다.


# 입출력 예시
# rows	columns	queries	result
# 6	6	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]	[8, 10, 25]
# 3	3	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	[1, 1, 5, 3]
# 100	97	[[1,1,100,97]]	[1]


def solution(rows, columns, queries):
    arr = [[i*columns + j + 1 for j in range(columns)] for i in range(rows)]
    answer = []
    for q in queries:
        min_v = 10001
        x1, y1, x2, y2 = q[0] - 1, q[1] - 1, q[2] - 1, q[3] - 1
        before = arr[x1][y1]
        for i in range(y1+1, y2+1):
            temp = arr[x1][i]
            min_v = min(min_v, temp)
            arr[x1][i] = before
            before = temp
        for i in range(x1+1, x2+1):
            temp = arr[i][y2]
            min_v = min(min_v, temp)
            arr[i][y2] = before
            before = temp
        for i in range(y2-1, y1-1, -1):
            temp = arr[x2][i]
            min_v = min(min_v, temp)
            arr[x2][i] = before
            before = temp
        for i in range(x2-1, x1-1, -1):
            temp = arr[i][y1]
            min_v = min(min_v, temp)
            arr[i][y1] = before
            before = temp
        answer.append(min_v)
    return answer


print(solution(100, 97, [[1,1,100,97]]))