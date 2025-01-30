import unittest
from utility import text_node_to_html_node
from utility import split_nodes_delimiter
from leafnode import LeafNode
from textnode import TextNode
from textnode import TextType

class TestUtility(unittest.TestCase):
    def test_eq(self):
        text_node1=TextNode("hi", TextType.BOLD)
        text_node2=TextNode("", TextType.LINKS, "www.blah.com")
        text_node3=TextNode("*text*", TextType.IMAGES, "www.imagefromhere")
        text_node4=TextNode("*text*", TextType.TEXT)
        text_node5=TextNode("here is some **text** for you", TextType.TEXT)
        list=split_nodes_delimiter([text_node1, text_node5], "**", TextType.BOLD)
        for item in list:
            print(item)
        #print(text_node_to_html_node(text_node1).to_html())
        #print(text_node_to_html_node(text_node2).to_html())
        #print(text_node_to_html_node(text_node3).to_html())
        

        


if __name__=="__main__":
    unittest.main()
