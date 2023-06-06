import spacy
import heapq

nlp = spacy.load("en_core_web_sm")

def anonymize_text(sentences):
    parser = nlp(sentences)
    print(parser.ents)
    answer = sentences
    for ele in parser.ents:
        print(ele.text)
        tmp = ""
        for _ in range(len(ele.text)):
            tmp += "X"
        answer = answer.replace(ele.text, tmp)
    return answer

# print(anonymize_text("John is old. John is now."))
# print(anonymize_text("Mark Oldham ate an apple"))

def main():
    heap = []
    heapq.heappush(heap, -3)
    heapq.heappush(heap, -34123)
    heapq.heappush(heap, -3123)
    heapq.heappush(heap, -341231)
    while True:
        if len(heap) < 1:
            break
        print(heapq.heappop(heap))
    l = list(reversed([1,2,3,4,56, 1, 1, 1, 1]))
    print(l)
main()
