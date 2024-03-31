def get_dict_set(s):
    res_set = set()
    res_dict = dict()
    for idx in range(len(s) - 1):
        temp = s[idx] + s[idx + 1]
        if temp.isalpha() == False:
            continue
        if temp not in res_dict:
            res_dict[temp] = 0
        res_dict[temp] += 1
        res_set.add(temp)
    return res_dict, res_set


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    dict1, set1 = get_dict_set(str1)
    dict2, set2 = get_dict_set(str2)

    i_set = set1 & set2
    u_set = set1 | set2

    if len(u_set) < 1:
        return 65536

    num = 0
    for ele in i_set:
        num += min(dict1[ele], dict2[ele])

    deno = 0
    for ele in u_set:
        m1 = dict1[ele] if ele in dict1 else 0
        m2 = dict2[ele] if ele in dict2 else 0
        deno += max(m1, m2)
    jk = int((num / deno) * 65536)
    return jk


print(solution("FRANCE",	"french"))  # 16384
