import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node=HTMLNode("p", "hello world")
        node2=HTMLNode("p", "hello world")
        node3=HTMLNode("h1", "this is a header", [node], {"href": "https://www.google.com", "target": "_blank"})
        node4=HTMLNode("a", "aloha", [node, node2])

        print(node)
        print(node2)
        print(node3)
        print(node4)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)





if __name__ == "__main__":
    unittest.main()
