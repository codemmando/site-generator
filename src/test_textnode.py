import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq_one(self):
        node = TextNode("test 1", TextType.ITALIC)
        node2 = TextNode("test 1", TextType.ITALIC, "www.test.positive")
        self.assertNotEqual(node, node2)    
    def test_not_eq_two(self):
        node = TextNode("test 1", TextType.ITALIC)
        node2 = TextNode("test 2", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_not_eq_three(self):
        node = TextNode("test 1", TextType.ITALIC, "www.test.negative")
        node2 = TextNode("test 1", TextType.ITALIC, "www.test.positive")
        self.assertNotEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.test.test")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.test.test", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")    

if __name__ == "__main__":
    unittest.main()
