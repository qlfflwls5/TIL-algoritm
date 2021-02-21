import sys


# 풀이한 논리
# 팰린드롬은 결국 '증심 문자'로부터 양옆으로 뻗어져나갈 때 양옆이 같은 문자열이다. (중심 문자에 대한 정의는 center_palindrome함수 내에 있다)
# 그러므로, 중심 문자를 구하는 부분과 그를 기준으로 양옆으로 뻗어져 나가며 팰린드롬을 구하는 부분으로 나뉘어 작동하는 방식이다.

# 중심 문자로부터 양옆으로 뻗어나가  팰린드롬을 검사할 함수
def max_palindrome(string):
    N = len(string)
    max_len = 0
    i = 1
    while i < N-1:
        # 이하 center는 현재 i번째의 문자이며 '중심 문자'란 center가 반복되는 총 문자를 말한다. 예를 들어, 'ABBBA'에 i가 2라면 center는 'B', 중심 문자는 'BBB'이다.
        center = string[i]
        # center의 양 옆에서 시작, temp_i는 왼쪽으로 나아갈 것이고 temp_j는 오른쪽으로 나아갈 것이며, temp_len은 중심 문자의 총 길이다.
        temp_i, temp_j, temp_len = i - 1, i + 1, 1
        # 나아가다 끝에 도달하면 더 이상 나아가지 말아야 하므로 각각 temp_i와 temp_j의 플래그를 만든다. temp_i는 0에, temp_j는 N-1에 도달하면 끝까지 간 것이다.
        is_i_end, is_j_end = 0, 0
        while center == string[i - 1] or center == string[i + 1]:
            # 중심 문자의 왼쪽 문자(string[temp_i])가 center와 같다면 중심 문자의 길이를 1 늘리고 temp_i를 왼쪽 칸으로 옮긴다.
            if string[temp_i] == center and not is_i_end:
                # temp_i가 0이면서 0번째 문자가 center와 같다면 중심 문자의 길이만 1 늘려주고 is_i_end를 1로 바꿔 이후 temp_i에 대한 작업은 종료한다.
                if temp_i == 0:
                    is_i_end = 1
                    temp_len += 1
                else:
                    temp_i -= 1
                    temp_len += 1
            # 중심 문자의 오른쪽 문자(string[temp_j)가 center와 같다면 중심 문자의 길이를 1 늘리고 temp_j를 오른쪽 칸으로 옮긴다.
            if string[temp_j] == center and not is_j_end:
                # temp_j가 N-1이면서 N-1번째 문자가 center와 같다면 중심 문자의 길이만 1 늘려주고 is_j_end를 1로 바꿔 이후 temp_i에 대한 작업은 종료한다.
                if temp_j == N - 1:
                    is_j_end = 1
                    temp_len += 1
                else:
                    temp_j += 1
                    temp_len += 1
            # 매 temp_i, temp_j에 대한 작업에서 중심 문자의 탐색이 끝나는 세 가지 경우의 수가 있다. 양 끝에 도달하지 않은 채로 끝난 경우, 한 쪽이 끝에 도달해서 끝난 경우
            # 전자의 경우 현재 temp_i와 temp_j번째 문자가 center와 다른 경우이다. 예) ABBBA에서 temp_i, temp_j는 각각 왼쪽 A, 오른쪽 A의 인덱스가 된다.
            # 후자의 경우 끝에 도달하지 않은 쪽의 문자가 center와 다른 경우이다. 예) ABBBB에서 temp_i는 A의 인덱스가 되고, BBBBA라면 temp_j는 A의 인덱스가 된다.
            # 각 경우에서 temp_i가 중심 문자의 시작, temp_j사 중심문자의 끝 번째가 되도록 조정한다.
            if string[temp_i] != center and string[temp_j] != center:
                temp_i += 1
                temp_j -= 1
                break
            elif temp_i == 0 and string[temp_j] != center:
                temp_j -= 1
                break
            elif temp_j == N - 1 and string[temp_i] != center:
                temp_i += 1
                break
        else:
            temp_i, temp_j = i, i

        # i를 중심 문자의 + 1번째로 계속 이동한다. 불필요한 반복을 줄일 수 있다.
        # 예) BBBABC가 있을 때, 첫 번째 B에서의 팰린드롬 검사를 실시했다면, 이후 중심 문자 내 연속되는 B에서는 검사를 안해도 된다. 다음 검사는 A부터 한다.
        i = temp_j + 1

        while 0 < temp_i and temp_j < N - 1:
            temp_i -= 1
            temp_j += 1
            if string[temp_i] != string[temp_j]:
                break
            temp_len += 2

        if max_len < temp_len:
            max_len = temp_len

    return max_len


sys.stdin = open('palidrome2_input.txt')
for t in range(1, 11):
    n = int(input())
    arr_row = [input() for _ in range(100)]
    max_result = 0
    for arr in arr_row, zip(*arr_row):
        for string in arr:
            temp_result = max_palindrome(string)
            if max_result < temp_result:
                max_result = temp_result

    print('#%d %d' % (t, max_result))