# BruteForce 알고리즘
# 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식으로 동작


p = 'is' # 찾을 패턴
t = 'This is a book~!' # 전체 텍스트
M = len(p)
N = len(t)

def BruteForce(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            # 만약 패턴이 다르다면 패턴을 검색하기 시작했던 위치로 되돌아감
            i = i - j
            # 만약 패턴이 다르다면 j를 반복문의 마지막에 0으로 맞출 수 있도록 1을 미리 빼줌
            j = -1
        i = i + 1
        # 패턴이 다르다면 j는 항상 0이 되고, 패턴이 같은 부분이 있다면 j는 같을 때까지 증가한다.
        j = j + 1
    if j == M:
        # 패턴이 일치하기 시작하는 인덱스를 반환
        return i-M # 검색 성공
    else:
        return -1 # 검색 실패

print(BruteForce(p, t))


# for문으로 작성
def BruteForce2(p, t):
    N = len(t)
    M = len(p)

    #시작 위치를 컨트롤
    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            if t[i+j] == p[j]:
                cnt += 1
            else:
                break

        if cnt == M:
            return i