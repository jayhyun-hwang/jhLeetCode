import spacy

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

print(anonymize_text("John is old. John is now."))
print(anonymize_text("Mark Oldham ate an apple"))