# 0121_ws의 3번을 응용해 본 문제이다.

# 강한 이름
# 문자열을 여러 개 전달 받아 각 문자에 대응되는 아스키 숫자들의 합을 비교하여 가장 큰 합을 가진 문자열을 반환하는
# get_strog_word 함수를 작성하시오.

def get_strog_word(*args):
    # 각 args에 대하여 아스키 숫자들의 합을 저장할 리스트. 차후 이를 사용해 최대값의 index를 구하여 문자열을 반환
    total_list = []

    # 전달받은 문자열들을 하나씩 꺼내어
    for word in args:
        # 각 문자열에서 문자들을 하나씩 꺼내고 아스키 숫자값을 구해 일시적인 total에 더한다.
        temp_total = 0
        for char in word:
            temp_total += ord(char)
        # 한 문자열에 대한 아스키 숫자들의 합인 temp_total을 total_list에 추가한다.
        total_list.append(temp_total)
    
    # total_list에서 최대값을 찾고, 인덱스를 찾아야 한다. 증가할 인덱스의 변수도 필요하다.
    max_idx = 0
    idx = 0
    max_total = total_list[0]
    for total in total_list:
        if total > max_total:
            max_total = total
            max_idx = idx
            idx += 1
        else:
            idx += 1
    
    return args[max_idx]


print(get_strog_word('tom', 'john', 'z', 'a', 'b', 'elice'))
