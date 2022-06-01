import test_import_1.bb_test as bb_test


class A:
    def __init__(self):
        super(A, self).__init__()

    def test(self, b: bb_test.B):
        print('test')