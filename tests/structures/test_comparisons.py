from ..utils import TranspileTestCase


class ComparisonTests(TranspileTestCase):
    def test_is(self):
        # This depends on integer caching.
        #self.assertCodeExecution("""
        #    x = 1
        #    if x is 1:
        #        print('Correct')
        #    else:
        #        print('Incorrect')
        #    print('Done.')
        #    """)

        self.assertCodeExecution("""
            # In CPython, if we were to use 1024 twice, they would share the
            # same slot in the constants. After VOC is done with it, it will
            # still create separate instances of the integer, however.
            x = 512 + 512
            if x is 1024:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

        self.assertCodeExecution("""
            x = 1
            if x is 5:
                print('Incorrect')
            else:
                print('Correct')
            print('Done.')
            """)

        self.assertCodeExecution("""
            x = None
            if x is None:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

        self.assertCodeExecution("""
            x = 1
            if x is None:
                print('Incorrect')
            else:
                print('Correct')
            print('Done.')
            """)

    def test_is_not(self):
        self.assertCodeExecution("""
            x = 1
            if x is not 5:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

        # This depends on integer-caching.
        #self.assertCodeExecution("""
        #    x = 1
        #    if x is not 1:
        #        print('Correct')
        #    else:
        #        print('Incorrect')
        #    print('Done.')
        #    """)

        self.assertCodeExecution("""
            # In CPython, if we were to use 1024 twice, they would share the
            # same slot in the constants. After VOC is done with it, it will
            # still create separate instances of the integer, however.
            x = 512 + 512
            if x is not 1024:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

        self.assertCodeExecution("""
            x = 1
            if x is not None:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

        self.assertCodeExecution("""
            x = None
            if x is not None:
                print('Incorrect')
            else:
                print('Correct')
            print('Done.')
            """)

    def test_lt(self):
        self.assertCodeExecution("""
            x = 1
            if x < 5:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

        self.assertCodeExecution("""
            x = 5
            if x < 5:
                print('Incorrect')
            else:
                print('Correct')
            print('Done.')
            """)

        self.assertCodeExecution("""
            x = 10
            if x < 5:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

    def test_le(self):
        self.assertCodeExecution("""
            x = 1
            if x <= 5:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

        self.assertCodeExecution("""
            x = 5
            if x <= 5:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

        self.assertCodeExecution("""
            x = 10
            if x <= 5:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

    def test_gt(self):
        self.assertCodeExecution("""
            x = 10
            if x > 5:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

        self.assertCodeExecution("""
            x = 5
            if x > 5:
                print('Incorrect')
            else:
                print('Correct')
            print('Done.')
            """)

        self.assertCodeExecution("""
            x = 1
            if x > 5:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

    def test_ge(self):
        self.assertCodeExecution("""
            x = 10
            if x >= 5:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

        self.assertCodeExecution("""
            x = 5
            if x >= 5:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

        self.assertCodeExecution("""
            x = 1
            if x >= 5:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

    def test_eq(self):
        self.assertCodeExecution("""
            x = 10
            if x == 5:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

        self.assertCodeExecution("""
            x = 5
            if x == 5:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

    def test_ne(self):
        self.assertCodeExecution("""
            x = 5
            if x == 5:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)

        self.assertCodeExecution("""
            x = 10
            if x == 5:
                print('Correct')
            else:
                print('Incorrect')
            print('Done.')
            """)
