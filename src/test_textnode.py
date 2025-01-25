import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is not a text node", TextType.ITALIC)
        node4 = TextNode("This is not a text node", TextType.ITALIC, "www.helloworld.com")

        self.assertEqual(node, node2)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node, node3)


if __name__ == "__main__":
    unittest.main()
