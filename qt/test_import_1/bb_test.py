

class B:
    def __init__(self, a):
        super(B, self).__init__()
        a.test(self)


if __name__ == '__main__':
    from test_import_0.aa_test import A
    b = B(A())
