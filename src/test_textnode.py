import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq_one(self):
        node = TextNode("test 1", TextType.ITALLIC)
        node2 = TextNode("test 1", TextType.ITALLIC, "www.test.positive")
        self.assertNotEqual(node, node2)    
    def test_not_eq_two(self):
        node = TextNode("test 1", TextType.ITALLIC)
        node2 = TextNode("test 2", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_not_eq_three(self):
        node = TextNode("test 1", TextType.ITALLIC, "www.test.negative")
        node2 = TextNode("test 1", TextType.ITALLIC, "www.test.positive")
        self.assertNotEqual(node, node2)    

if __name__ == "__main__":
    unittest.main()
