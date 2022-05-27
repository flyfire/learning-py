import json
from question_info import QuestionInfo


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
