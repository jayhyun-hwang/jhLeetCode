# https://programmers.co.kr/learn/courses/30/lessons/17681

# replace 꼭 쓰기, python의 string은 golang처럼 인덱스 순환 검사가 편하지 않으므로
    # replace builtin 들여다보기
    # 1. str의 n번째 문자를 바꾸고 싶다.
    # 2. str[:n] + 문자 삽입 + str[n+1:]

# zfill
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        val = bin(arr1[i] | arr2[i])
        val = val[2:]
        # val = val.zfill(n)
        for i in range(n):
            if n != len(val):
                val = "0" + val
            else:
                break
        val = val.replace("0"," ")
        val = val.replace("1","#")
        answer.append(val)
    return answer

print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))

def valueFill(self, filling: str, length: int) -> str:
    # 파라미터 길이 체크
    if len(self) < 1: return

    # + / - 일 때 처리
    if self[:1] == '-' or self[:1] == '+':
        return self.valueFill(filling, length-1)
    
    for i in range(length):
        if length > len(self):
            self = filling + self
        else:
            break
    
    return self

