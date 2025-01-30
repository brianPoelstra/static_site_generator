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


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes=[]

    for node in old_nodes:
        if node.text_type!=TextType.TEXT:
            new_nodes.append(node)
        elif node.text.find(delimiter)==-1:
            raise Exception(f"delimiter not found in node with text {node.text}")
        else:
            new_nodes.extend(find_delimiter(node.text, delimiter, text_type))

    return new_nodes


def find_delimiter(text, delimiter, text_type):
    nodes=[]
    if text.find(delimiter)==-1:
        return [TextNode(text, TextType.TEXT)]
    if len(text)<=2:
        return nodes

    start=text.find(delimiter)
    end=text.find(delimiter, start+1)

    if start>0:
        nodes.append(TextNode(text[:start], TextType.TEXT))
    nodes.append(TextNode(text[start+len(delimiter):end], text_type))
    
#if delimiter is at very end of string, return node
    if len(text)==end+len(delimiter):
        return nodes
    else:
        nodes.extend(find_delimiter(text[end+len(delimiter):], delimiter, text_type))

    return nodes



