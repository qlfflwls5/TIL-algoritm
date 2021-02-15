# View
# 강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.
# 이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만 왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.
# 그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.
# 빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.


import sys

sys.stdin = open("hw_View_input.txt")

for t in range(1, 11):
    N = int(input())
    B = list(map(int, input().split()))
    result = 0
    # 양끝 2칸씩은 건물이 없기 때문에 i도 2부터 시작하고 끝도 N-2로 잡는다.
    i = 2
    while i < N - 2:
        # 자신을 기준으로 양옆 2개의 건물들과 비교를 하고, 자신이 제일 크다면 두 건물을 건너뛴다.
        max_building = B[i-2]
        if B[i-1] > max_building:
            max_building = B[i-1]
        if B[i+1] > max_building:
            max_building = B[i+1]
        if B[i+2] > max_building:
            max_building = B[i+2]
        if B[i] > max_building:
            result += B[i] - max_building
            i += 3
        else:
            i += 1
    print('#%d %d' %(t, result))