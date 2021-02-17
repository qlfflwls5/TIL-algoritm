# Flatten
# 한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.
# 높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.
# 평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.
# 평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때,
# 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.
# 가장 높은 곳에 있는 상자를 가장 낮은 곳으로 옮기는 작업을 덤프라고 정의한다.


# [제약 사항]
# 가로 길이는 항상 100으로 주어진다.
# 모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.
# 덤프 횟수는 1이상 1000이하로 주어진다.
# 주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다 (주어진 data에 따라 0 또는 1이 된다).


# [입력]
# 총 10개의 테스트 케이스가 주어지며, 각 테스트 케이스의 첫 번째 줄에는 덤프 횟수가 주어진다. 그리고 다음 줄에 각 상자의 높이값이 주어진다.


# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 최고점과 최저점의 높이 차를 출력한다.


import sys


sys.stdin = open("hw_Flatten_input.txt")

# 1
# 재귀로 푼 것
# 매 시행마다 전체 박스 중 가장 높은 것과 가장 낮은 것을 찾고 높은 것은 -1, 낮은 것은 +1을 해준다.
# 이후 다시 가장 높은 것과 가장 낮은 것을 찾아 둘의 차이를 구한다.
# 가장 높이가 높은 박스와 낮은 박스의 인덱스를 반환하는 함수
def max_min_index(boxes):
    max_i, min_i = 0, 0
    for i in range(len(boxes)):
        if boxes[i] > boxes[max_i]:
            max_i = i
        elif boxes[i] < boxes[min_i]:
            min_i = i
    return max_i, min_i


# 한 번의 덤프를 실행하는 함수(가장 높은 것에서 가장 낮은 것에 1을 주고 다시 가장 높은 것과 낮은 것을 구해 차이를 확인하는 작업 수행)
def do_dump(boxes, dump):
    max_i, min_i = max_min_index(boxes)
    boxes[max_i] -= 1
    boxes[min_i] += 1
    dump -= 1
    max_i, min_i = max_min_index(boxes)
    if boxes[max_i] - boxes[min_i] < 2:
        return boxes[max_i] - boxes[min_i]
    if dump == 0:
        return boxes[max_i] - boxes[min_i]
    else:
        return do_dump(boxes, dump)

for t in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    print('#%d %d' %(t, do_dump(boxes, dump)))

# 2
# 정석으로 푼 것
def max_min_index(boxes):
    max_i, min_i = 0, 0
    for i in range(len(boxes)):
        if boxes[i] > boxes[max_i]:
            max_i = i
        elif boxes[i] < boxes[min_i]:
            min_i = i
    return max_i, min_i

for t in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    while dump:
        max_i, min_i = max_min_index(boxes)
        boxes[max_i] -= 1
        boxes[min_i] += 1
        dump -= 1
        if boxes[max_i] - boxes[min_i] < 2:
            max_i, min_i = max_min_index(boxes)
            result = boxes[max_i] - boxes[min_i]
            break
    else:
        max_i, min_i = max_min_index(boxes)
        result = boxes[max_i]- boxes[min_i]

    print('#%d %d' %(t, result))


# 3
# 카운트 리스트 이용 방법 => 이런 방법을 잘 알고 있어야 한다.
for t in range(1, 11):
    N = int(input())
    box = list(map(int, input()))

    # 높이 카운트 리스트
    h_cnt = [0] * 101

    # 초기화
    min_value = 100
    max_value = 1  # 최저의 높이는 0이 아니라 1이다.

    # 박스의 높이를 카운트하면서 최고점과 최저점을 찾아보자.
    for i in range(100):
        h_cnt[box[i]] += 1
        if box[i] > max_value:
            max_value = box[i]
        if box[i] < min_value:
            min_value = box[i]

    while N > 0 and min_value < max_value - 1:
        # 상자 옮기기
        h_cnt[min_value] -= 1
        h_cnt[min_value + 1] += 1

        h_cnt[max_value] -= 1
        h_cnt[max_value - 1] += 1

        # 포인터를 변경하자.
        if h_cnt[min_value] == 0:
            min_value += 1

        if h_cnt[max_value] == 0:
            max_value -= 1

        # 덤프 줄이기
        N -= 1

        print(max_value - min_value)