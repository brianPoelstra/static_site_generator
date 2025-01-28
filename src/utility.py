from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextType
from textnode import TextNode


def text_node_to_html_node(text_node):
    
    if text_node.text_type==TextType.TEXT:
        return LeafNode(None, text_node.text)
    
    if text_node.text_type==TextType.BOLD:
        return LeafNode("b", text_node.text)

    if text_node.text_type==TextType.ITALIC:
        return LeafNode("i", text_node.text)

    if text_node.text_type==TextType.CODE:
        return LeafNode("cold", text_node.text)

    if text_node.text_type==TextType.LINKS:
        return LeafNode("link", "", {"href": text_node.url})

    if text_node.text_type==TextType.IMAGES:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    raise Exception("invalid text type")
