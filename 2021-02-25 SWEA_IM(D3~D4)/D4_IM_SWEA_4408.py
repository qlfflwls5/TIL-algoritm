# 자기 방으로 돌아가기
# 고등학교 학생들이 학교에서 수련회를 갔다. 수련회에 간 학생들은 친구들과 음주가무를 즐기다가 밤 12시가 되자 조교들의 눈을 피해 자기방으로 돌아가려고 한다.
# 제 시간에 자기방으로 돌아가지 못한 학생이 한 명이라도 발견되면 큰일나기 때문에 최단 시간에 모든 학생이 자신의 방으로 돌아가려고 한다.
# 숙소는 긴 복도를 따라 총 400개의 방이 다음과 같이 배열되어 있다.
# room1, room3, room5, ..., room399
# room2, room4, room6, ..., room400
# 모든 학생들은 현재 위치에서 자신의 방으로 돌아가려고 하는데, 만약 두 학생이 자기방으로 돌아가면서 지나는 복도의 구간이 겹치면 두 학생은 동시에 돌아갈 수 없다.
# 예를 들어 (방1 -> 4) 와 (방3 -> 6) 은 복도 구간이 겹치므로 한 사람은 기다렸다가 다음 차례에 이동해야 한다. 이동하는 데에는 거리에 관계없이 단위 시간이 걸린다고 하자.
# 각 학생들의 현재 방 위치와 돌아가야 할 방의 위치의 목록이 주어질 때, 최소 몇 단위시간만에 모든 학생들이 이동할 수 있는지를 구하시오.


# [입력]
# 입력은 T(≤10)개의 테스트 케이스로 되어 있다. 각 테스트 케이스의 첫 줄에는 돌아가야 할 학생들의 수 N이 주어진다.
# 다음 N 줄에는 각 학생의 현재 방 번호(≤400)와 돌아가야 할 방의 번호(≤400)가 주어진다. 주어지는 2N개의 방 번호 중 중복되는 것은 없다.


# [출력]
# 테스트 케이스 T에 대한 결과는 “#T ”을 찍고, 각 테스트 케이스마다 필요한 시간을 한 줄에 하나씩 출력한다.


T = int(input())
for t in range(1, T+1):
    N = int(input())
    room_list = [0]*401
    for _ in range(N):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        if s % 2 == 0:
            s -= 1
        if e % 2:
            e += 1
        for i in range(s, e+1):
            room_list[i] += 1

    print('#%d %d' % (t, max(room_list)))

# s, e를 정렬하는 풀이법이 있는데, 이 때 정렬의 특성을 매우 유의해야 한다.
# ['100', '4000', '90']을 정렬하면 '100', '4000', '90'이 된다. 왜? -> 문자열은 앞 글자부터 정렬이 되기 때문에