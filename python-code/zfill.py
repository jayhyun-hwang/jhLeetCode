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
        s = strParam[1:]
        print(s)
        return firstIdx + valueFill(strParam[1:], filling, length-1)
    # n 길이만큼 filling 채우기
    for i in range(length):
        if length > len(strParam):
            strParam = filling + strParam
        else:
            break
    
    return strParam

print(valueFill("+132", "0", 10))
print(valueFill("+++132", "0", 10))
print(valueFill("-132", "0", 10))
print(valueFill("---132", "0", 10))
print("---132".zfill(10))
print("---132".rjust(10, "0"))


# Python program to demonstrate working of 
# rjust()
string = 'geeks'
length = 8
  
# If no fill character is provided, space
# is used as fill character
print(string.rjust(length))

print("abcd".rjust(10))
print("abcd".rjust(10, '0'))
print("abcd".ljust(10, '0'))