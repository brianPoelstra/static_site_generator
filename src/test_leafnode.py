import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "paragraph")
        node2 = LeafNode("a", "click me", {"href": "https://www.google.com"})
        node3 = LeafNode("h1", "this is a header")
        node4 = LeafNode("h2", "this is a header with hyperlink", {"href": "github.com"})

def test():
    print(node4)
    pass

if __name__ == "__main__":
    unittest.main()

