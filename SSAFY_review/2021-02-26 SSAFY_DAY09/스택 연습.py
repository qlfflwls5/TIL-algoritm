stack = []

# v를 스택의 맨 뒤에 추가한다.
def push(v):
    stack.append(v)


def pop():
    # underflow 체크: data가 없는데 pop을 하라고 했는지
    if not stack:
        print('stack underflow')
        return
    return stack.pop(-1)


push(1)
push(2)
push(3)
print(stack)

# .clear() 메소드를 통해 stack을 완전 비우기
stack.clear()
push(1)
push(2)
push(3)
pop()
pop()
push(4)
push(5)
pop()
print(stack)

#-----------------------------------------------------------------------------#
N = 3
stack2 = ['']*N
top = -1 # 마지막 item의 위치


def push2(v):
    # overflow확인
    # top를 사용해서 조건 작성
    # overflow가 아니면 top를 증가하고, v를 top에 넣기
    global top
    if top >= N - 1: # N-1을 넘을 리는 없지만 그냥 이렇게 쓴다.
        print('overflow')
        return
    top += 1
    stack2[top] = v


def pop2():
    # underflow 확인
    # top에 있는 item을 임시변수에 저장, top가 감소
    # 임시변수에 있는 item을 반환
    global top
    if top == -1: # top < 0 이라고 쓰는게 더 좋다.
        print('underflow')
        return
    temp = stack2[top]
    stack2[top] = '' # 굳이 이건 할 필요는 없다. 스택 자체를 출력하지 않는한
    top -= 1
    return temp

push2(1)
push2(2)
push2(3)
push2(4)
pop2()
pop2()
pop2()
pop2()
push2(1)

print(stack2)