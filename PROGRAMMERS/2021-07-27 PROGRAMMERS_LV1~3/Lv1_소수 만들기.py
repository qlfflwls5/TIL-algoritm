# 소수 만들기
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.


# 제한사항
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.


# 입출력 예
# nums	result
# [1,2,3,4]	1
# [1,2,7,6,4]	4


prime_list = [0, 0] + [1]*3000
for i in range(2, 3001):
    if prime_list[i]:
        for j in range(i + i, 3001, i):
            prime_list[j] = 0


# 1
# 어차피 세 번 반복이니깐 for문
def solution(nums):
    n = len(nums)
    answer = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            if i != j:
                for k in range(j+1, n):
                    if i != k and j != k and prime_list[(nums[i] + nums[j] + nums[k])]:
                        answer += 1

    return answer


# 2
# 재귀로 조합 구현
def solution2(nums):
    def combi(level, idx, S):
        if level == 3:
            if prime_list[S]:
                answer[0] += 1
            return

        for i in range(idx, n - 2 + level):
            combi(level+1, i+1, S+nums[i])

    n = len(nums)
    answer = [0]
    combi(0, 0, 0)
    return answer[0]


print(solution([1, 2, 7, 6, 4]))