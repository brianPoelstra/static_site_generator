import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "paragraph")
        node2 = LeafNode("a", "click me", {"href": "https://www.google.com"})
        node3 = LeafNode("h1", "this is a header")
        node4 = LeafNode("h2", "this is a header with hyperlink", {"href": "github.com"})

        print(node)
        print(node2)
        print(node3)
        print(node4)


if __name__ == "__main__":
    unittest.main()

