def solution(s):
    answer = ''
    splited_word = s.split(' ')
    result_list = []
    for word in splited_word:
        if word == '':
            result_list.append(word)
            continue
        first_char = word[0]
        if first_char.isalpha() == True:
            word = word[0].upper() + word[1:].lower()
        else:
            word = word.lower()
        result_list.append(word)
    answer = ' '.join(result_list)
    return answer

print(solution("3people unFollowed me")) # "3people Unfollowed Me"
print(solution("for the last week")) # "For The Last Week"
