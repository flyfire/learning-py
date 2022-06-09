import os

if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    print(dir)
    filename = os.path.join(dir, 'tmp/tmp.jpg')
    print(filename)
    print(os.path.splitext(__file__))
    import uuid
    uid = uuid.uuid1()
    print(type(uid))
    uid = str(uid)
    print(uid)