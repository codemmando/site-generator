import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_with_one_child(self):
        node = ParentNode("div",
        [LeafNode("p", "Hello World!")],
        props={"class": "container", "id": "main-div"}
        )
        expected_html = '<div class="container" id="main-div"><p>Hello World!</p></div>'
        self.assertEqual(node.to_html(), expected_html)

    def test_parent_with_two_children(self):
        node = ParentNode("div",
        [LeafNode("p", "Hello World!"), LeafNode("a", "click me", {"href": "www.test.dk", "target": "_blank"})],
        props={"class": "container", "id": "main-div"}
        )
        expected_html = '<div class="container" id="main-div"><p>Hello World!</p><a href="www.test.dk" target="_blank">click me</a></div>'
        self.assertEqual(node.to_html(), expected_html)
        
    def test_value_error_when_tag_is_none(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode(None, [])
            node.to_html()
        self.assertEqual(str(context.exception), "ParentNode: tag cannot be None.")

    def test_parent_with_no_children_empty_list(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode("div", [])
            node.to_html()
        self.assertEqual(str(context.exception), "ParentNode: children cannot be None.")

    def test_parent_without_props(self):
        node = ParentNode("div", [LeafNode("p", "Hello World!")])
        expected_html = '<div><p>Hello World!</p></div>'
        self.assertEqual(node.to_html(), expected_html)

    def test_nested_parent_nodes(self):
        inner_parent = ParentNode(
            "span",
            [LeafNode("p", "Hello")]
        )
        outer_parent = ParentNode(
            "div",
            [inner_parent]
        )
        expected_html = '<div><span><p>Hello</p></span></div>'
        self.assertEqual(outer_parent.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()
    