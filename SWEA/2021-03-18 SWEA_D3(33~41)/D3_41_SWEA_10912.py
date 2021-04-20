# 외로운 문자
# 알파벳 소문자 만으로 이루어진 문자열이 주어진다.
# 이 문자열에서 같은 두 문자들을 짝짓고 남는 문자가 무엇인지 구하는 프로그램을 작성하라.
# 같은 문자를 여러 번 짝지어서는 안 된다.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 알파벳 소문자 만으로 이루어진 문자열이 주어진다.
# 이 문자열의 길이는 1이상 100이하이다.


# [출력]
# 각 테스트 케이스 마다 예제와 같은 형식으로 남는 문자를 사전 순서대로 출력한다.
# 만약 어떤 문자도 남지 않는다면 “Good”을 출력하도록 한다.


# 1
for t in range(1, int(input())+1):
    word = sorted(list(input()))
    result = ''
    for i in range(len(word)):
        if i and word[i] == word[i-1]:
            continue
        if word.count(word[i]) % 2:
            result += word[i]

    print('#%d %s' %(t, result if result else 'Good'))


# 2
# while문이 더 느렸다.
for t in range(1, int(input())+1):
    word = sorted(list(input()))
    result = ''
    i = 0
    while i < len(word):
        count = word.count(word[i])
        if count % 2:
            result += word[i]
            i += count
        else:
            i += 1

    print('#%d %s' %(t, result if result else 'Good'))


# 3
# 채은님
# stack을 활용
def get_word(words):
    stack = []
    # 정렬해주어야 인접한 상태에서 비교 가능
    words.sort()
    for word in words:
        if stack and word == stack[-1]:
            stack.pop()
        else:
            stack.append(word)
    if stack:
        return ''.join(stack)
    return 'Good'


T = int(input())
for t in range(1, T+1):
    words = list(input())
    ans = get_word(words)
    print('#%d %s' % (t, ans))