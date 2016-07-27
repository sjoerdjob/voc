from unittest import expectedFailure

from .. utils import TranspileTestCase


class IsTests(TranspileTestCase):
    def test_nonetype_identical(self):
        self.assertCodeExecution("""
            print(None is None)
        """)

    @expectedFailure
    def test_small_ints_identical(self):
        # VOC transpilation does not cache small integers.
        self.assertCodeExecution("""
            print(1 is 1)
        """)

    def test_ints_different(self):
        self.assertCodeExecution("""
            print(1 is 2)
        """)

    @expectedFailure
    def test_intern_string_identical(self):
        # VOC transpilation does not intern strings.
        self.assertCodeExecution("""
            print('a' is 'a')
        """)

    def test_noninterned_string_identical(self):
        self.assertCodeExecution("""
            # We need to force the values to be different.
            x = 'a'
            y = 'b'
            print((x + y) is 'ab')
        """)

    def test_different_string_different(self):
        self.assertCodeExecution("""
            print('hello' is 'world')
        """)

    def test_same_variable_identical(self):
        self.assertCodeExecution("""
            x = 0
            print(x is x)
        """)


class IsNotTests(TranspileTestCase):
    def test_nonetype_identical(self):
        self.assertCodeExecution("""
            print(None is not None)
        """)

    @expectedFailure
    def test_small_ints_identical(self):
        # VOC transpilation does not cache small integers.
        self.assertCodeExecution("""
            print(1 is not 1)
        """)

    def test_ints_different(self):
        self.assertCodeExecution("""
            print(1 is not 2)
        """)

    @expectedFailure
    def test_intern_string_identical(self):
        # VOC transpilation does not intern strings.
        self.assertCodeExecution("""
            print('a' is not 'a')
        """)

    def test_noninterned_string_identical(self):
        self.assertCodeExecution("""
            # We need to force the values to be different.
            x = 'a'
            y = 'b'
            print((x + y) is not 'ab')
        """)

    def test_different_string_different(self):
        self.assertCodeExecution("""
            print('hello' is not 'world')
        """)

    def test_same_variable_identical(self):
        self.assertCodeExecution("""
            x = 0
            print(x is not x)
        """)


class InTests(TranspileTestCase):
    def test_1_in_set1(self):
        self.assertCodeExecution("""
            print(1 in set([1]))
        """)

    def test_2_in_set1(self):
        self.assertCodeExecution("""
            print(2 in set([1]))
        """)

    @expectedFailure
    def test_5_in_range_10(self):
        # Range does not implement "__contains__" yet.
        self.assertCodeExecution("""
            print(5 in range(10))
        """)


class NotInTests(TranspileTestCase):
    def test_1_not_in_set1(self):
        self.assertCodeExecution("""
            print(1 not in set([1]))
        """)

    def test_2_not_in_set1(self):
        self.assertCodeExecution("""
            print(2 not in set([1]))
        """)


class LessThanTests(TranspileTestCase):
    def test_0_less_than_1(self):
        self.assertCodeExecution("""
            print(0 < 1)
        """)

    def test_hello_less_then_world(self):
        self.assertCodeExecution("""
            print("hello" < "world")
        """)


class GreaterThanTests(TranspileTestCase):
    def test_0_greater_than_1(self):
        self.assertCodeExecution("""
            print(0 > 1)
        """)

    def test_hello_greater_then_world(self):
        self.assertCodeExecution("""
            print("hello" > "world")
        """)
