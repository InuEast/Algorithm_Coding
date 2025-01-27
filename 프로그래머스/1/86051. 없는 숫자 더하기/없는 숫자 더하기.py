def solution(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
        if sum != 45:
            answer = 45 - sum
    return answer