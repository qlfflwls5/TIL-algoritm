# 110 사전
# 0과 1로 이루어진 어떤 문자열 x에 대해서, 당신은 다음과 같은 행동을 통해 x를 최대한 사전 순으로 앞에 오도록 만들고자 합니다.

# x에 있는 "110"을 뽑아서, 임의의 위치에 다시 삽입합니다.
# 예를 들어, x = "11100" 일 때, 여기서 중앙에 있는 "110"을 뽑으면 x = "10" 이 됩니다. 뽑았던 "110"을 x의 맨 앞에 다시 삽입하면 x = "11010" 이 됩니다.

# 변형시킬 문자열 x가 여러 개 들어있는 문자열 배열 s가 주어졌을 때, 각 문자열에 대해서 위의 행동으로 변형해서 만들 수 있는 문자열 중
# 사전 순으로 가장 앞에 오는 문자열을 배열에 담아 return 하도록 solution 함수를 완성해주세요.


# 제한사항
# 1 ≤ s의 길이 ≤ 1,000,000
# 1 ≤ s의 각 원소 길이 ≤ 1,000,000
# 1 ≤ s의 모든 원소의 길이의 합 ≤ 1,000,000


# 입출력 예
# s	result
# ["1110","100111100","0111111010"]	["1101","100110110","0110110111"]


# 틀린 풀이
# 주어진 키 '110'을 앞부터 찾아서 골라낸 후, 키를 빼낸 문자열에서 1이 처음으로 세 개 연속인 부분의 앞에 키를 끼워넣는다.
# 끼워넣고 나면 키를 끼워넣은 자리까지가 확정된다. 확정된 부분을 결과에 더하고 이 뒤의 문자열에 대하여 앞 작업을 반복한다.
# 만약 1이 세 개 연속인 부분이 없다면 뒷부분이 확정된다.
# 문자열의 맨 마지막이 1이라면 끝부터 시작하여 0이 처음으로 나오는 곳에 키를 넣고, 이를 결과에 더한 뒤 키부터 마지막까지 확정된다. 마지막이 1이 아니라면 맨 마지막에 키를 넣고 확정된다.
# 만약 문자열에 키가 없다면 모든 작업이 끝난 것이다. 키가 없는 부분을 결과에 더하고 끝낸다.
key = '110'
def solution(s):
    answer = []
    for x in s:
        result_front = ''
        result_rear = ''
        while True:
            print('처음', x)
            key_idx = x.find(key)
            if key_idx == -1:
                result = result_front + x + result_rear
                break
            sub_key_x = x[:key_idx] + x[key_idx + 3:]
            i = 0
            cnt = 0
            while i < len(sub_key_x):
                if sub_key_x[i] == '1':
                    cnt += 1
                else:
                    cnt = 0
                # 앞부분 확정
                if cnt == 3:
                    result_front += sub_key_x[:i-2] + key
                    x = sub_key_x[i-2:]
                    break

                i += 1
            # 뒷부분 확정
            else:
                if sub_key_x and sub_key_x[-1] == '1':
                    cnt = 0
                    for i in range(len(sub_key_x)-1, -1, -1):
                        if sub_key_x[i] == '1':
                            cnt += 1
                        else:
                            break

                    result_rear = key + sub_key_x[len(sub_key_x)-cnt:] + result_rear
                else:
                    result_rear = key + result_rear

                x = sub_key_x[:len(sub_key_x)-cnt]

        answer.append(result)

    return answer


print(solution(["0110111100110101111001101001010"]))