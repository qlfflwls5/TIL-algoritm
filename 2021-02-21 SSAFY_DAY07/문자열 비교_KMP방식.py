# 다음은 KMP방식을 코드로 구현한 것이다.
# KMP 방식을 이해해보자.


def get_KMPTable(P):
    len_p = len(P)
    pi = [0] * len_p
    j = 0
    for i in range(1, len_p):
        while j > 0 and P[i] != P[j]:
            j = pi[j - 1]
        if P[i] == P[j]:
            j += 1
            pi[i] = j
    return pi


def KMP(table, wd, st):
    s_len = len(st)
    w_len = len(wd)
    cnt = 0
    j = 0
    for i in range(len(st)):
        while j > 0 and st[i] != wd[j]:
            j = table[j-1]
            #print('kmp i, j:', i, j)
        if st[i] == wd[j]:
            if j == w_len - 1:
                cnt += 1
                #print(i - len(wd) + 1)  # 발생위치
                j = table[j]
            else:
                j += 1
            #print('kmp i, j:', i, j)
    return cnt


for _ in range(2):
    test_case, word, sentence = int(input()), input(), input()
    KMP_table = get_KMPTable(word)
    print(KMP_table)
    sol = KMP(KMP_table, word, sentence)
    print('#%d %d' % (test_case, sol))
