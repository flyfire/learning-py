from question import parse_questions

if __name__ == '__main__':
    questions = parse_questions("questions.json")
    for question in questions:
        print(question)
