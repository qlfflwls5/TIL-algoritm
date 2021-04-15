# 풍선 터트리기
# 일렬로 나열된 n개의 풍선이 있습니다. 모든 풍선에는 서로 다른 숫자가 써져 있습니다.
# 당신은 다음 과정을 반복하면서 풍선들을 단 1개만 남을 때까지 계속 터트리려고 합니다.

# 1. 임의의 인접한 두 풍선을 고른 뒤, 두 풍선 중 하나를 터트립니다.
# 2. 터진 풍선으로 인해 풍선들 사이에 빈 공간이 생겼다면, 빈 공간이 없도록 풍선들을 중앙으로 밀착시킵니다.

# 여기서 조건이 있습니다. 인접한 두 풍선 중에서 번호가 더 작은 풍선을 터트리는 행위는 최대 1번만 할 수 있습니다.
# 즉, 어떤 시점에서 인접한 두 풍선 중 번호가 더 작은 풍선을 터트렸다면, 그 이후에는 인접한 두 풍선을 고른 뒤 번호가 더 큰 풍선만을 터트릴 수 있습니다.

# 당신은 어떤 풍선이 최후까지 남을 수 있는지 알아보고 싶습니다.
# 위에 서술된 조건대로 풍선을 터트리다 보면, 어떤 풍선은 최후까지 남을 수도 있지만, 어떤 풍선은 무슨 수를 쓰더라도 마지막까지 남기는 것이 불가능할 수도 있습니다.

# 일렬로 나열된 풍선들의 번호가 담긴 배열 a가 주어집니다.
# 위에 서술된 규칙대로 풍선들을 1개만 남을 때까지 터트렸을 때 최후까지 남기는 것이 가능한 풍선들의 개수를 return 하도록 solution 함수를 완성해주세요.


# 입출력 예
# a	        result
# [9,-1,-5]	3
# [-16,27,65,-2,58,-92,-71,-68,-61,-33]	6


# 현재 숫자 n이 혼자 남을 수 있는지 가리는 방법은 가장 작은 수 min을 찾고 n을 기준으로 min을 제외한 min이 있는 쪽의 모든 숫자를 지운다.
# -> 두 번째 예에서 n이 27이라면 27을 벽으로 생각해서 27까지의 -92를 제외한 수를 전부 다지 움. -16 27 -92가 된다.
# 이제 min이 없던 쪽에서 나보다 큰 숫자들만 있어야 혼자 남을 수 있다. 지금 다룬 예에서는 -16이 27보다 크지 않으므로 삭제할 수 없으니 안된다.
# 정리하자면, 현재 n을 기준으로 min이 없는 쪽에서 n보다 작은 수가 나오면 불가능하다.
# 그러므로 0번째부터 min까지 내림차순인 개수와 끝에서 min까지 역으로 올때 내림차순인 개수를 구하면 된다.


def solution(a):
    min_i = a.index(min(a))
    # 각 풍선 기준 min_i가 있는 쪽의 반대 쪽 최소값의 정보를 저장해놓는다. 이래야 효율적이다.
    min_front, min_rear = a[0], a[len(a) - 1]
    # 0번째, 마지막 풍선, 최소값 풍선은 무조건 남을 수 있다. 얘네는 미리 셀 것이다. 최소값 풍선이 0번째나 마지막이면 2개, 아니면 3개
    answer = 2 if min_i == 0 or min_i == len(a) - 1 else 3
    # min_i보다 앞에 있는 풍선들은 자기보다 앞의 풍선들이 전부 나보다 크면 된다.
    for i in range(1, min_i):
        if a[i] < min_front:
            answer += 1
            min_front = a[i]
    # min_i보다 뒤에 있는 풍선들은 자기보다 뒤의 풍선들이 전부 나보다 크면 된다.
    for i in range(len(a) - 2, min_i, -1):
        if a[i] < min_rear:
            answer += 1
            min_rear = a[i]

    return answer