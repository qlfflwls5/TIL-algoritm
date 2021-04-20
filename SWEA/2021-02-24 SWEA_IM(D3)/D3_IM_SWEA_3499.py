# 퍼펙트 셔플
# 카드를 퍼펙트 셔플 한다는 것은, 카드 덱을 정확히 절반으로 나누고 나눈 것들에서 교대로 카드를 뽑아 새로운 덱을 만드는 것을 의미한다.
# 정확한 방식은 다음과 같다.
# 카드가 A, B, C, D, E, F 쌓여 있다면 이를 (A, B, C), (D, E, F)로 나누고 교대로 뽑아 A, D, B, E, C, F로 하면 퍼펙트 셔플이다.
# N개의 카드가 있는 덱이 주어질 때 이를 퍼펙트 셔플하면 어떤 순서가 되는지 출력하는 프로그램을 작성하라.
# 만약 N이 홀수이면, 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어가게 하면 된다.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 자연수 N(1 ≤ N ≤ 1,000)이 주어진다.
# 두 번째 줄에는 덱에 카드가 놓인 순서대로 N개의 카드 이름이 공백으로 구분되어 주어진다.
# 카드의 이름은 알파벳 대문자와 ‘-’만으로 이루어져 있으며, 길이는 80이하이다.


# [출력]
# 각 테스트 케이스마다 주어진 덱을 퍼펙트 셔플한 결과를 한 줄에 카드 이름을 공백으로 구분하여 출력한다.


# 1
# zip을 활용해서 풀기
T = int(input())
for t in range(1, T+1):
    N = int(input())
    card = list(input().split())
    # post_card만 마지막에 공백 요소를 추가해주면 zip을 실행했을 때 무조건 pre_card의 길이를 기준으로 zip이 실행된다.
    pre_card, post_card = card[:(N+1)//2], card[(N+1)//2:] + ['']
    print('#%d' % t, end=' ')
    for col in zip(pre_card, post_card):
        print(*col, end=' ')
    print()

# 오른쪽 공백제거 하자 왠만하면 .rstrip()
    

# 2
# insert를 활용해서 풀기
T = int(input())
for t in range(1, T+1):
    N = int(input())
    card = list(input().split())
    pre_card, post_card = card[:(N+1)//2], card[(N+1)//2:]
    for i in range(len(post_card)):
        # insert를 하면 원본인 pre_card에 삽입되면서 이후의 인덱스가 변하므로 insert를 어디 인덱스로 해줘야하는지 잘 생각하자.
        pre_card.insert(i*2+1, post_card[i])
    print('#%d %s' % (t, ' '.join(pre_card)))


# 3
# zip이나 insert보다 새로운 빈 리스트를 하나 만들고 거기에 번갈아 append 해나가는 것이 더 빠를 것이다.