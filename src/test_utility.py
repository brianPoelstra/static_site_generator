import unittest
from utility import *
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
        #for item in list:
         #   print(item)
        #print(text_node_to_html_node(text_node1).to_html())
        #print(text_node_to_html_node(text_node2).to_html())
        #print(text_node_to_html_node(text_node3).to_html())
        test_text_to_textnodes()         

def test_extract():
    list=extract_markdown_images("this is text with a ![rick roll](https://i.imgur.com) and ![obi wan](https://stuff)")
    for item in list:
        print(item)

    list=extract_markdown_links("this is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://youtube)")
    for item in list:
        print(item)
        
def test_split_nodes():
    #node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)
    #new_nodes = split_nodes_image([node])
    #for item in new_nodes:
    #    print(item)
    node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
    new_nodes = split_nodes_link([node])
    for item in new_nodes:
        print(item)

def test_text_to_textnodes():
    list=text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
    for item in list:
        print(item)


if __name__=="__main__":
    unittest.main()
