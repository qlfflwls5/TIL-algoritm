# 3진법 뒤집기
# 자연수 n이 매개변수로 주어집니다.
# n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.


# 제한사항
# n은 1 이상 100,000,000 이하인 자연수입니다.


# 입출력 예
# n	result
# 45	7
# 125	229


# 3으로 나눈 나머지를 answer로 담고 answer를 3곱하면 쉬프트가 일어난다.
# 스터디원들에게 최고의 평가를 받은 풀이...ㅎ
def solution(n):
    answer = 0
    while n:
        answer = answer * 3 + n % 3
        n //= 3

    return answer