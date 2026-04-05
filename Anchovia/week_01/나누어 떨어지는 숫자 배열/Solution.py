def solution(arr, divisor):
    answer = []
    arr.sort()
    for item in arr:
        if item % divisor == 0:
            answer.append(item)
    if len(answer) < 1:
        answer.append(-1) 
    return answer