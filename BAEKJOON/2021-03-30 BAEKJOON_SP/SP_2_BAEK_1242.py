# 소풍
# 동호와 동호네 반 친구들은 산정호수로 소풍을 갔다. 총 N명이 소풍에 참가했는데, 산정 호수에는 있는 것이 별로 없어서 무대에 올라가기로 했다.
# 무대에 올라간 N명은 1번부터 N번까지 시계방향으로 원형으로 앉았다. 그런 후에, KIN 이란 게임을 시작했다. 이 게임은 1번부터 시작된다.
# 그리고 한 명씩 시계방향으로 1, 2, ... , K까지 센다. K를 말하는 사람은 퇴장 당한다.
# 그 후에는 다음 자리에 앉아있는 사람이 1부터 다시 센다. 동호도 이 게임에 M번 학생으로 참가한다. 동호는 자기가 몇 번째로 퇴장 당하는지 궁금해졌다.
# 예를 들어, 5명의 학생이 참가하고 K=2이고, 동호는 3번 학생이라고 하면, 가장 처음에는 1 2 3 4 5와 같이 앉아있다.
# 1부터 게임을 시작하기 때문에, 1이 1이라고 말하고, 2가 2라고 말한다. 2가 퇴장 당한다. 3이 1이라고 말하고, 4가 2라고 말한다.
# 4가 퇴장 당한다. 그 다음에는 1이 퇴장 당한다. 그 후에는 5가 퇴장당하고, 마지막으로 3이 퇴장 당한다. 동호는 3번 학생이기 때문에, 5번째로 퇴장 당한다.
# N, K, M가 주어졌을 때, 동호가 몇 번째로 퇴장 당하는지 알아내는 프로그램을 작성하시오.


# [입력]
# 첫째 줄에 N, K, M가 주어진다. N과 K는 5,000,000보다 작거나 같은 자연수이고, M은 N보다 작거나 같다.


# [출력]
# 첫째 줄에 동호가 몇 번째로 퇴장당하는 지 출력한다.


N, K, M = map(int, input().split())
line = [1]*N
i = 0
num = 0
result = 0
while True:
    now = i % N
    if line[now]:
        num += 1
        if num == K:
            if now == M - 1:
                break
            num, line[now] = 0, 0
            result += 1
    i += 1

print(result + 1)


N, K, M = map(int, input().split())
i = 0
num = 0
die = set()
result = 0
while True:
    now = i % N
    if now in die:
        i += 1
        continue
    else:
        num += 1
        if num == K:
            if now == M - 1:
                break
            num = 0
            die.add(now)
            result += 1
    i += 1

print(result + 1)


# 2
N, K, M = map(int, input().split())
kick = 1
cnt = 0
while True:
    kick += K-1
    while kick > N-cnt:
        kick = kick - (N-cnt)
    cnt += 1
    if kick == M or cnt == N:
        break
    elif kick < M:
        M -= 1
print(cnt)