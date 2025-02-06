import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node=HTMLNode("p", "hello world")
        node2=HTMLNode("p", "hello world")
        node3=HTMLNode("h1", "this is a header", [node], {"href": "https://www.google.com", "target": "_blank"})
        node4=HTMLNode("a", "aloha", [node, node2])

        #test()
def test():
    self.assertNotEqual(node, node4)
    return None




if __name__ == "__main__":
    unittest.main()
