import unittest
from utility import text_node_to_html_node
from leafnode import LeafNode
from textnode import TextNode
from textnode import TextType

class TestUtility(unittest.TestCase):
    def test_eq(self):
        #text_node1=TextNode("hi", TextType.BOLD)
        #text_node2=TextNode("", TextType.LINKS, "www.blah.com")
        #text_node3=TextNode("text", TextType.IMAGES, "www.imagefromhere")

        #print(text_node_to_html_node(text_node1).to_html())
        #print(text_node_to_html_node(text_node2).to_html())
        #print(text_node_to_html_node(text_node3).to_html())

        


if __name__=="__main__":
    unittest.main()

