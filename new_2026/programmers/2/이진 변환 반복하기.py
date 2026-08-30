def solution(s):
    conversion_count = 0
    remove_count = 0

    while s != "1":
        tmp_str = ""
        for val in s:
            if val == "0":
                remove_count += 1
                continue
            tmp_str += val
        s = str(bin(len(tmp_str)))[2:]
        conversion_count += 1
    return [conversion_count, remove_count]
