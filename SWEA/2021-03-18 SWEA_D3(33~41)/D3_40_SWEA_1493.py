# 수의 새로운 연산
# 2차원 평면 제 1사분면 위의 격자점 (x,y)에 위 그림과 같이 대각선 순서로 점에 수를 붙인다.
# 점 (x,y)에 할당된 수는 #(x,y)로 나타낸다.
# 예를 들어 #(1,1) = 1, #(2,1)=3, #(2,2) = 5, #(4,4) = 25이다.
# 반대로 수 p가 할당된 점을 &(p)로 나타낸다.
# 예를 들어 &(1) = (1,1), &(3) = (2,1), &(5) = (2,2), &(25) = (4,4)이다.
# 두 점에 대해서 덧셈을 정의한다. 점 (x,y)와 점 (z,w)를 더하면 점 (x+z, y+w)가 된다.
# 즉, (x,y) + (z,w) = (x+z, y+w)로 정의한다.
# 우리가 해야 할 일은 수와 수에 대한 새로운 연산 ★를 구현하는 것으로, p★q는 #(&(p)+&(q))으로 나타난다.
# 예를 들어, &(1)=(1,1), &(5) = (2,2)이므로, 1★5 = #(&(1)+&(5)) = #((1,1)+(2,2)) = #(3,3) = 13이 된다.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 두 정수 p,q(1 ≤ p, q ≤ 10,000)가 주어진다.


# [출력]
# 각 테스트 케이스마다 ‘#t’(t는 테스트 케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 각 테스트 케이스마다 p★q의 값을 출력한다.


# 첫 번째 대각선 (1, 1) = 1
# 두 번째 대각선 (1, 2), (2, 1) = 2, 3
# 세 번째 대각선 (1, 3), (2, 2), (3, 1) = 4, 5, 6
# ...
# n번째 대각선까지 대하여 for i in range(1, n+1)에서 (i, n+1-i)가 1씩 누적증가하는 규칙이다.
for t in range(1, int(input())+1):
    p, q = map(int, input().split())
    # p / q를 찾았는지의 플래그
    flag_p, flag_q = 0, 0
    # level번째 대각선
    level = 1
    num = 0
    while not flag_p or not flag_q:
        for i in range(1, level+1):
            num += 1
            if not flag_p and num == p:
                flag_p = 1
                p_x, p_y = i, level+1-i
            if not flag_q and num == q:
                flag_q = 1
                q_x, q_y = i, level+1-i

        level += 1

    o_x, o_y = p_x + q_x, p_y + q_y
    flag_o = 0
    o_level = 1
    result = 0
    while not flag_o:
        for i in range(1, o_level+1):
            result += 1
            if i == o_x and o_level+1-i == o_y:
                flag_o = 1
                break
        o_level += 1

    print('#%d %d' % (t, result))


# 2
# 승현님 코드
def find_xy(num):
    # _sum은 (_add, 1)의 값, _add는 몇 번째 대각선인지(내 코드의 level)
    _sum, _add = 0, 0
    while _sum < num:
        _add += 1
        _sum += _add
    dif = _sum - num # (_add, 1) 기준 dif만큼의 거리가 목표 x, y위치다.

    return (_add - dif, 1 + dif)


for t in range(1, int(input())+1):
    a, b = map(int, input().split())
    a_loc, b_loc = find_xy(a), find_xy(b)
    c_loc = (a_loc[0]+b_loc[0], a_loc[1] + b_loc[1])
    dif = c_loc[1] - 1
    cross = (c_loc[0] + dif)*(c_loc[0] + dif + 1)//2
    print("#%d %d" %(t, cross-dif))
