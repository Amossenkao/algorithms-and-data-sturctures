import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        self.assertEqual(stack.len, 0)
        stack.push(45, 29)
        self.assertEqual(stack.peek, 29)
        self.assertEqual(stack.len, 2)

    def test_pop(self):
        stack = Stack()
        stack.push(56, 18, 90)
        stack.pop()
        self.assertEqual(stack.len, 2)

    def test_has_item(self):
        stack = Stack()
        stack.push(56, 18, 90)
        self.assertTrue(stack.has_item(18))
        self.assertFalse(stack.has_item(40))


if __name__ == '__main__':
    unittest.main()
