import json
from question0 import Question0
from question1 import Question1
from question2 import Question2


class QuestionInfo:
    def __init__(self, t="", title="", subtitle="", video_path="", explain_1="", explain_2="", count_down=10):
        super(QuestionInfo, self).__init__()
        self.t = t
        self.title = title
        self.subtitle = subtitle
        self.video_path = video_path
        self.explain_1 = explain_1
        self.explain_2 = explain_2
        self.count_down = count_down

    def generate_widget(self):
        mapping = {
            "intro_1": Question0,
            "countdown": Question1,
            "result": Question2
        }
        return mapping[self.t](self)

    def __repr__(self):
        return f"t={self.t}, title={self.title}, subtitle={self.subtitle}, video_path={self.video_path}, explain_1={self.explain_1}, explain_2={self.explain_2}, count_down={self.count_down}"


def parse_questions(config_path):
    with(open(config_path, "r")) as f:
        content = '\n'.join(f.readlines())
    data = json.loads(content)
    if not isinstance(data, list):
        raise Exception(f"parse data exception {content}")
    items = []
    for item in data:
        if not isinstance(item, dict):
            raise Exception(f"parse data exception {content}")
        items.append(QuestionInfo(**item))
    return items


def test_parse():
    items = parse_questions("questions.json")
    for item in items:
        print(item)


if __name__ == "__main__":
    test_parse()
