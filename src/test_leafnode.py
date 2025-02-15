import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_tag(self):
        node = LeafNode("p","this is a test")
        self.assertEqual(node.to_html(), "<p>this is a test</p>")
    def test_has_prop(self):
        node = LeafNode("a","hello", {"href": "www.test.com"})  
        self.assertEqual(node.to_html(), '<a href="www.test.com">hello</a>')
    def test_has_props(self):
        node = LeafNode("a", "click", {
            "href": "www.test.com",
            "target": "_blank"
            })
        self.assertEqual(node.to_html(), '<a href="www.test.com" target="_blank">click</a>')
    def test_no_tag(self):
        node = LeafNode(None, "hello", {"href": "www.test.com"})
        self.assertEqual(node.to_html(), "hello")
if __name__ == "__main__":
    unittest.main()
