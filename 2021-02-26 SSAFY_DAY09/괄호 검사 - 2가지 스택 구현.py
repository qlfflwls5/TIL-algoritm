# 괄호 검사 - 2가지 스택 구현
# 주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
# 예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
# 정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
# print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# 1
# 길이를 정해놓지 않은 스택
def push(v):
    stack.append(v)


def pop():
    if not stack:
        return
    return stack.pop(-1)


T = int(input())
for t in range(1, T+1):
    string = input()
    stack = []
    result = 1
    for v in string:
        if v == '(' or v == '{':
            push(v)
        elif v == ')':
            if pop() != '(':
                result = 0
                break
        elif v == '}':
            if pop() != '{':
                result = 0
                break

    if stack:
        result = 0

    print('#%d %d' %(t, result))


# 2
# 길이가 정해져있는 스택
def push(v):
    global top
    if top == len(stack)-1:
        return
    top += 1
    stack[top] = v


def pop():
    global top
    if top == -1:
        return
    temp = stack[top]
    stack[top] = '' # 이것은 stack 자체의 값을 출력해야 할 때 말고는 안넣어도 되긴 하다.
    top -= 1

    return temp


T = int(input())
for t in range(1, T+1):
    string = input()
    stack = ['']*len(string)
    top = -1
    result = 1
    for v in string:
        if v == '(' or v == '{':
            push(v)
        elif v == ')':
            if pop() != '(':
                result = 0
                break
        elif v == '}':
            if pop() != '{':
                result = 0
                break
    
    # top이 -1까지 안내려갔다면 스택에 아직 잔존물이 있는 것
    if top != -1:
        result = 0

    print('#%d %d' % (t, result))