# https://school.programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    answer = []
    musics = dict()
    genres_total = dict()
    for i in range(len(genres)):
        if genres[i] not in musics:
            musics[genres[i]] = dict()
        musics[genres[i]][i] = plays[i]
        if genres[i] not in genres_total:
            genres_total[genres[i]] = 0
        genres_total[genres[i]] += plays[i]
    sorted_g = sorted(genres_total.items(), key=lambda x: -x[1])
    for ele in sorted_g:
        sorted_m = sorted(musics[ele[0]].items(), key=lambda x: -x[1])
        answer.append(sorted_m[0][0])
        if len(sorted_m) > 1:
            answer.append(sorted_m[1][0])
    return answer


print(
    solution(["classic", "pop", "classic", "classic", "pop"],
             [500, 600, 150, 800, 2500]))  # 	[4, 1, 3, 0]
