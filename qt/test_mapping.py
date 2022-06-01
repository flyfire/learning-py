class Test:
    def __init__(self):
        super(Test, self).__init__()


if __name__ == '__main__':
    mapping = {
        "test": Test
    }
    print(mapping.__contains__('test'))
    print(mapping.__contains__('hello'))
    hello = "a b c\n"
    x = hello.split()
    for i in x:
        print(i)
    print('*' * 40)
