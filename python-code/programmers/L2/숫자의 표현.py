def solution(n):
    answer = 0
    left, right, temp_sum = 0, 0, 0
    
    while left < n:
        if temp_sum < n:
            right += 1
            temp_sum += right
        else:
            if temp_sum == n:
                answer += 1
            left += 1
            temp_sum -=  left
            
    return answer