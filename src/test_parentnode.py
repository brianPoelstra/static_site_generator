import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node1=LeafNode("b", "don't click me", {"href": "https://www.google.com"})
        node2=LeafNode("p", "paragraph")

        node3=ParentNode("p1", [node1, node2], {"href": "doesparentwork.com"})
        node4=ParentNode("p2", [node3, node1])
    
        print(node3.to_html())
        print(node4.to_html())




if __name__=="__main__":
    unittest.main()

