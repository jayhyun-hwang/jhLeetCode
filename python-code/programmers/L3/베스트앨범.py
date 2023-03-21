# https://school.programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    answer = []
    music_dict = dict()
    for i in range(len(genres)):
        if genres[i] not in music_dict:
            music_dict[genres[i]] = dict()
            music_dict[genres[i]]['total'] = 0
        music_dict[genres[i]][i] = plays[i]
        music_dict[genres[i]]['total'] += plays[i]
    # print(music_dict.items())
    print(music_dict)
    music_dict = dict(
        sorted(music_dict.items(), key=lambda item: -item[1]['total']))
    print(music_dict)
    # print(music_dict.items())
    for m in music_dict.items():
        # print(m)
        # print(m[1]['total'])
        sort_music = sorted(m[1].items(), key=lambda item: -item[1])
        print(sort_music)
        answer.append(sort_music[1][0])
        if len(sort_music) >= 3:
            answer.append(sort_music[2][0])
    return answer


print(
    solution(["classic", "pop", "classic", "classic", "pop"],
             [500, 600, 150, 800, 2500]))  # 	[4, 1, 3, 0]
