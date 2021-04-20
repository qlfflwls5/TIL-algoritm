# 삼성시의 버스 노선
# 삼성시에 있는 5,000개의 버스 정류장은 관리의 편의를 위해 1에서 5,000까지 번호가 붙어 있다.
# 그리고 버스 노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고,
# Bi이하인 모든 정류장만을 다니는 버스 노선이다.
# P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N ( 1 ≤ N ≤ 500 )이 주어진다.
# 다음 N개의 줄의 i번째 줄에는 두 정수 Ai, Bi ( 1 ≤ Ai ≤ Bi ≤ 5,000 )가 공백 하나로 구분되어 주어진다.
# 다음 줄에는 하나의 정수 P ( 1 ≤ P ≤ 500 )가 주어진다.
# 다음 P개의 줄의 j번째 줄에는 하나의 정수 Cj ( 1 ≤ Cj ≤ 5,000 ) 가 주어진다.


# [출력]
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고 한 칸을 띄운 후,
# 한 줄에 P개의 정수를 공백 하나로 구분하여 출력한다.
# j번째 정수는 Cj번 버스 정류장을 지나는 버스 노선의 개수여야 한다.


T = int(input())
for t in range(1, T+1):
    N = int(input())
    # 입력받는 A와 B들을 담을 리스트
    AB_list = []
    for i in range(N):
        AB = list(map(int, input().split()))
        # A와 B를 요소로 갖는 리스트 자체를 요소로 하여 AB_list에 집어넣는다.
        AB_list += [AB]
    P = int(input())
    # 각 C에 대해 지나가는 버스 노선의 개수를 담을 count 역할 리스트이다.
    cnt_list = [0]*P
    # 각 C를 입력받을 때마다 진행하는 방법을 떠올리자. => C를 따로 모아놓지 않아도 되는 방법
    for i in range(P):
        C = int(input())
        # 각 C마다 count 0부터 시작
        cnt = 0
        # 모든 A와 B짝에 대해 수행해야 하므로 N번 반복한다.
        for j in range(N):
            # C가 A보다 크거나 같고 B보다 작거나 같으면 노선이 지나가는 것이다. count += 1
            if AB_list[j][0] <= C <= AB_list[j][1]:
                cnt += 1
        # i번째로 입력받는 C에 대해 지나가는 버스 노선의 개수를 count 리스트의 i번째에 넣는다.
        cnt_list[i] = cnt

    ans = ' '.join(map(str, cnt_list))
    print('#%d %s' %(t, ans))
    
    
# *** 알고리즘의 기본
# 입력받은 것을 다 저장해놓고 쓸 생각을 하지말고
# 입력받을 때마다 작업을 수행할 수 있는지를 생각해보자.
# 따로 저장해두는 작업 하나하나가 전부 메모리, 시간 낭비


# 문제의 조건을 잘 이용  =>  이 풀이를 반드시 외워야한다.

# T = int(input())
# for i in range(1, T + 1):
#     N = int(input())
#     bus_stop = [0] * 5001
#
#     for i in range(N):
#         A, B = map(int, input().split())
#
#         # 해당 정류장에 지나는 버스의 대수 누적
#         for j in range(A, B + 1):
#             bus_stop[j] += 1
#
#     P = in (input())  # 우리가 확인하고 싶은 버스정류장의 수
#
#     print('#{}'.format(t), end='')
#     for i in range(P):
#         C = int(input())  # 우리가 확인하고 싶은 정류장의 번호
#         print(bus_stop[C], end='')
#     print()