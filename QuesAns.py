from transformers import pipeline


def QuesAnswer(question,answer):
    print(answer)
    fans=[]
    nlp = pipeline("question-answering")
    for i in answer:
        final_answer=nlp(question, i)
        ans=final_answer.get("answer")
        fans.append(ans)
    return fans
