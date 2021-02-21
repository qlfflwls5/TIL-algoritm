# 특별한 정렬
# 보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
# N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.


# 예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
# 10 1 9 2 8 3 7 4 6 5
# 주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.


# 1
# 단순한 선택 정렬 10까지만 정렬하기 때문에 arr이 쓸데없이 긴 경우 효율적이다.
T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst_num = list(map(int, input().split()))
    for i in range(0, 10):
        if i%2:
            min_i = i
            # 최소값을 찾아 현재 i번째의 값과 자리를 바꾼다.
            for j in range(i + 1, len(lst_num)):
                if lst_num[j] < lst_num[min_i]:
                    min_i = j

            lst_num[i], lst_num[min_i] = lst_num[min_i], lst_num[i]
        else:
            max_i = i
            # 최대값을 찾아 현재 i번째의 값과 자리를 바꾼다.
            for j in range(i + 1, len(lst_num)):
                if lst_num[j] > lst_num[max_i]:
                    max_i = j

            lst_num[i], lst_num[max_i] = lst_num[max_i], lst_num[i]

    # result 만드는 방법. 이렇게 깔끔하게 인덱싱해와서 join활용하는 것이 좋다.
    result = ' '.join(map(str, lst_num[:10])) # 이거 lst_num[10]은 인덱스 범위를 넘어가지만 에러가 안난다. 참조하지 않는 것이기 때문에
    print('#%d %s' %(t, result))


# 2
# 함수화하여 선택정렬을 전부 시행해 오름차순으로 만들고 인덱싱으로 큰값 작은값 가져오기
def selectionSort(arr):
    for i in range(len(arr)-1):
        min_i = i
        for j in range(i+1, len(arr)):
            if arr[min_i] > arr[j]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst_num = list(map(int, input().split()))
    selectionSort(lst_num)
    lst_result = []
    for i in range(5):
        lst_result += [lst_num[N-1-i]]
        lst_result += [lst_num[i]]

    print('#%d ' % t, end='')
    print(*lst_result)


# 3
# 함수화하면서도 정렬을 작은값 5개 큰값 5개씩만 하기
# 이 코드 중요함
# 각 get_MaxM과 get_MinM 함수의 동작을 알아야 한다.
def get_MaxM(num, M):
  N = len(num)
  # M번째 큰 값까지를 리턴 i = 0~M-1
  for i in range(M):
    # j는 i+1부터 끝까지. 만약 num[i]보다 num[j]가 크다면 swap. 이 과정에서 num[i]는 가장 큰 값으로 계속 갱신되면서 비교함
    # 이것은 선택정렬도 버블정렬도 아니고 그냥 단순한 교환정렬. 선택정렬은 인덱스를 갱신하면서 목표값을 찾으면 1번만 교환한다면
    # 얘는 num[i]를 계속 교환하면서 갱신하여 목표값인지를 확인하는 방법
    for j in range(i+1, N):
      if num[i] < num[j]:
        num[i], num[j] = num[j], num[i]
  return num[:M]


def get_MinM(num, M):
  N = len(num)
  for i in range(M):
    for j in range(i+1, N):
      if num[i] > num[j]:
        num[i], num[j] = num[j], num[i]
  return num[:M]


T = int(input())
for t in range(1, T+1):
  N = int(input())
  num = list(map(int, input().split()))
  a = get_MaxM(num, 5)
  b = get_MinM(num, 5)
  answer = ['%d %d' % (a[i], b[i]) for i in range(5)]
  sol = ' '.join(answer)
  print('#%d %s' %(t, sol))