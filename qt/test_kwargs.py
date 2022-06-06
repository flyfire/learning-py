def f1(question_type, **kwargs):
    print(question_type)
    for item in kwargs:
        print(item)


if __name__ == "__main__":
    f1("type", a="a", b="b")
    a = "see_pic"
    b = {
        "see_pic": "hello",
        "see_word": "world"
    }
    for key in b.keys():
        print(key)
    if a in b.keys():
        print(True)
    else:
        print(False)
