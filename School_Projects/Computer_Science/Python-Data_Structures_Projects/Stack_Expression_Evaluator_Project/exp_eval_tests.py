# Start of unittest - add to completely test functions in exp_eval
import unittest
from exp_eval import *
from stack_array import *
import operator

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self) -> None:
        self.assertAlmostEqual(postfix_eval("3  5 +"), 8)

    def test_postfix_eval_02(self) -> None:
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self) -> None:
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self) -> None:
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self):
        self.assertEqual(postfix_eval("2 3 +"), 5)
        self.assertEqual(postfix_eval("2 3 **"), 8)
        self.assertEqual(postfix_eval("8 2 >>"), 2)
        self.assertEqual(postfix_eval("6 4 3 + 2 - * 6 /"), 5)
        self.assertEqual(postfix_eval("5 2 4 * + 7 2 - 4 6 2 / 2 - * + 4 - +"), 18)

    def test_postfix_eval_06(self):
        with self.assertRaises(PostfixFormatException) as e:
            postfix_eval("")
        self.assertEqual(str(e.exception), "Empty input")


    def test_postfix_eval_07(self):
        with self.assertRaises(ValueError) as e:
            postfix_eval("3 0 /")
        self.assertEqual(str(e.exception), "Divisor is Zero")

    def test_postfix_eval_08(self):
        with self.assertRaises(PostfixFormatException) as e:
            postfix_eval("3 3.5 >>")
        self.assertEqual(str(e.exception), "Illegal bit shift operand")

    def test_postfix_eval_09(self):
        self.assertEqual(postfix_eval("1000000000 1 +"), 1000000001)
        self.assertEqual(postfix_eval("3 2.5 +"), 5.5)

    def test_postfix_eval_10(self):
        with self.assertRaises(PostfixFormatException) as e:
            postfix_eval("3 + +")
        self.assertEqual(str(e.exception), "Insufficient operands")

    def test_postfix_eval_11(self):
        self.assertEqual(postfix_eval("2 3 + 5 * 6 -"), 19)

    def test_postfix_eval_12(self):
        self.assertEqual(postfix_eval("5"), 5)

    def test_postfix_eval_13(self):
        self.assertEqual(postfix_eval("7.0 2 /"), 3.5)



    def test_infix_to_postfix_01(self) -> None:
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("2 ** 3 ** 2"), "2 3 2 ** **")
        self.assertEqual(infix_to_postfix("2 * ( 3 + 4 )"), "2 3 4 + *")
        self.assertEqual(infix_to_postfix("2 ** 3 ** 2"), "2 3 2 ** **")
        self.assertEqual(infix_to_postfix("2 * 3 + 4 / 2"), "2 3 * 4 2 / +")
        self.assertEqual(infix_to_postfix("2 + 3 * 4"), "2 3 4 * +")
        self.assertEqual(infix_to_postfix("2 * ( 3 + ( 4 / 2 ) )"), "2 3 4 2 / + *")
        self.assertEqual(infix_to_postfix("( 1 + ( 2 * 3 ) ) ** 2"), "1 2 3 * + 2 **")
        with self.assertRaises(PostfixFormatException) as e:
            infix_to_postfix("")
        self.assertEqual(str(e.exception), "Empty input")

    def test_prefix_to_postfix(self) -> None:
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("+ ** 2 3 ** 4 5"), "2 3 ** 4 5 ** +")
        self.assertEqual(prefix_to_postfix("- + 7 3 * 5 2"), "7 3 + 5 2 * -")
        self.assertEqual(prefix_to_postfix("* + 2 3 4"), "2 3 + 4 *")
        self.assertEqual(prefix_to_postfix("<< >> 5 1 3"), "5 1 >> 3 <<")
        self.assertEqual(prefix_to_postfix("6"), "6")
        self.assertEqual(prefix_to_postfix("- + 3 * 4 5 / 6 2"), "3 4 5 * + 6 2 / -")
        self.assertEqual(prefix_to_postfix("* + 1 2 - 3 4"), "1 2 + 3 4 - *")
        with self.assertRaises(PostfixFormatException) as e:
            prefix_to_postfix("")
        self.assertEqual(str(e.exception), "Empty input")
        with self.assertRaises(PostfixFormatException) as e:
            prefix_to_postfix("+ 3")
        self.assertEqual(str(e.exception), 'Insufficient operands')
        with self.assertRaises(PostfixFormatException) as e:
            prefix_to_postfix("+ 3 4 5")
        self.assertEqual(str(e.exception), 'Too many operands')


if __name__ == "__main__":
    unittest.main()
