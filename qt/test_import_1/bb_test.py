

class B:
    def __init__(self, a):
        super(B, self).__init__()
        a.test(self)

    def is_processing(self):
        return True


if __name__ == '__main__':
    from test_import_0.aa_test import A
    b = B(A())
    if b is not None or b.is_processing():
        print("hello")
    if b is not None and b.is_processing():
        print("world")
