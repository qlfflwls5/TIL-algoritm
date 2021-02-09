# 패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.


# [제약 사항]
# 각 문자열의 길이는 30이다. 마디의 최대 길이는 10이다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 길이가 30인 문자열이 주어진다.


# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


T = int(input())
for t in range(1, T+1):
    word = input()
    # 마디의 최대 길이는 10이므로 1~10까지 확인
    for i in range(1, 11):
        # 반복이 아니게 되면 flag가 0으로 바뀔 것
        flag = 1
        # 1~i까지 i스텝 마다 같은 문자가 나오는지 확인할 것
        for j in range(1, i+1):
            # range를 통해 j부터 끝까지 i마다 나오는 문자가 다르다면 flag를 0으로 설정
            for k in range(j, len(word), i):
                if word[j] != word[k]:
                    flag = 0
        # 각 i마다 모든 작업 완료 후 flag를 확인하여 1이면 출력하고 break
        if flag:
            print('#%d %d' %(t, i))
            break


# 승현님 코드: i개씩 잘라서 단어단어 비교

# T = int(input())

# for t in range(1, T+1):
#     string = input()
#     for i in range(1, len(string)+1):
#         flag = 1
#         test = string
#         length = i
#         pattern = string[:i]
#         while len(test) >= i:
#             if pattern == test[:i]:
#                 test = test[i:]
#             else:
#                 flag = 0
#                 break
#         if flag == 1:
#             print("#%d %d" %(t, length))
#             break
                


            
