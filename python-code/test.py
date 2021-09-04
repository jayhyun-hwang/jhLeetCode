print("12345".zfill(3))
# 12345

print("12345".zfill(10))
# 0000012345

print("-12345".zfill(10))
# -000012345

print("+12345".zfill(10))
# +000012345

def valueFill(strParam: str, filling: str, length: int) -> str:
    # 파라미터 길이 체크
    if len(strParam) >= length: return strParam

    # + / - 일 때 처리
    firstIdx = strParam[:1]
    if firstIdx == '-' or firstIdx == '+':
        return firstIdx + valueFill(strParam[1:], filling, length-1)
    
    # n 길이만큼 filling 채우기
    for i in range(length):
        if length > len(strParam):
            strParam = filling + strParam
        else:
            break
    
    return strParam

# print(valueFill("12345", "0", 3))
# print(valueFill("12345", "0", 10))
# print(valueFill("-12345", "0", 10))
# print(valueFill("+12345", "0", 10))
# print(valueFill("+12345", "0", 5))
# print(valueFill("+12345", "123", 6))
# print(valueFill("+12345", "123", 4))
# print(valueFill("-12345", "123", 5))
# print(valueFill("-12345", "123", 6))
# print(valueFill("-12345", "77", 7))
# print(valueFill("-12345", "77", 4))

print(valueFill("BTotheY", "얍", 10))
print(valueFill("BTotheY", "얍얍얍", 10))
print(valueFill("BTotheY", "얍", 30))


