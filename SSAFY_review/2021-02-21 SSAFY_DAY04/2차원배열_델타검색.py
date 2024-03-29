# 델타검색
# 5x5 2차 배열에 무작위로 25개의 숫자로 초기화 한 후
# 25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오.
# 예를 들어 아래 그림에서 7 값의 이웃한 값은 2, 6, 8, 12 이며 차의 절대값의 합은 12 이다.
# | 2 – 7 | + | 6 – 7 | + | 8 – 7 | + | 12 – 7 | = 12


# 25개의 요소에 대해서 모두 조사하여 총합을 구하시오.
# 벽에 있는 요소는 이웃한 요소가 없을 수 있음을 주의하시오.
# 예를 들어 [0][0]은 이웃한 요소가 2개이다.


import sys
sys.stdin = open("delta_input.txt")


# 각 요소에서 상하좌우 이웃한 요소에 접근하기 위한 델타 리스트. 이런건 밖으로 빼자
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for t in range(1, T+1):
    # 2차원 배열 입력 받기
    arr = [list(map(int, input().split())) for _ in range(5)]
    # 각 요소에서의 이웃한 요소와의 차의 절대값의 전체 합을 담을 변수
    total = 0
    for i in range(5):
        for j in range(5):
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                # 상하좌우 중에 이차원 배열을 벗어나는 인덱스를 갖게 되는 경우, 혹은 인덱스가 -1인 경우가 아닐 때만 실행
                if 0 <= nr < 5 and 0 <= nc < 5:
                    dif = arr[nr][nc] - arr[i][j]
                    # 절대값을 구해야하므로 음수이면 -부호를 붙인다.
                    if dif < 0:
                        dif = -dif
                    total += dif
    print('#%d %d' %(t, total))