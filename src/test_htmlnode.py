import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_two_props(self):
        node = HTMLNode(props = {
            "href": "https://test.test",
            "target": "_blank",
        })
        self.assertEqual(node.props_to_html(), ' href="https://test.test" target="_blank"')

    def test_props_to_html_one_prop(self):
        node = HTMLNode(props = {
            "href": "https://www.hestenettet.dk",
        })
        self.assertEqual(node.props_to_html(), ' href="https://www.hestenettet.dk"')

    def test_not_eq(self):
        node = HTMLNode(props = {
            "href": "https://www.test.hub"
        })
        self.assertNotEqual(node.props_to_html(), 'href="https://www.test.hub"')

if __name__ == "__main__":
    unittest.main()