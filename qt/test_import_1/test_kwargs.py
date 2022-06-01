import json


class Question:
    def __init__(self, question_type="", title="", subtitle=""):
        self.question_type = question_type
        self.title = title
        self.subtitle = subtitle

    def __repr__(self):
        return f"{self.question_type}, {self.title}, {self.subtitle}"


if __name__ == '__main__':
    with open("questions.json") as f:
        content = '\n'.join(f.readlines())
    data = json.loads(content)
    question = Question(**data)
    print(question)
