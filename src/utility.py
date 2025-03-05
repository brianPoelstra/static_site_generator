from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextType
from textnode import TextNode
import re

def text_node_to_html_node(text_node):
    
    if text_node.text_type==TextType.TEXT:
        return LeafNode(None, text_node.text)
    
    if text_node.text_type==TextType.BOLD:
        return LeafNode("b", text_node.text)

    if text_node.text_type==TextType.ITALIC:
        return LeafNode("i", text_node.text)

    if text_node.text_type==TextType.CODE:
        return LeafNode("code", text_node.text)

    if text_node.text_type==TextType.LINKS:
        return LeafNode("link", "", {"href": text_node.url, "alt text": text_node.text})

    if text_node.text_type==TextType.IMAGES:
        return LeafNode("img", "", {"src": text_node.url, "alt text": text_node.text})

    raise Exception("invalid text type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes=[]

    for node in old_nodes:
        if node.text_type!=TextType.TEXT:
            new_nodes.append(node)
        elif node.text.find(delimiter)!=-1 and node.text.find(delimiter, node.text.find(delimiter)+1)==-1:
            raise Exception("Invalid markdown syntax")
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



def extract_markdown_images(text):
    matches_alt_text=re.findall("!\[(.*?)\]", text)
    matches_url=re.findall("\((.*?)\)", text)
    
    return list(zip(matches_alt_text, matches_url))

def extract_markdown_links(text):
    matches_anchor_text=re.findall("\[(.*?)\]", text)
    matches_url=re.findall("\((.*?)\)", text)

    return list(zip(matches_anchor_text, matches_url))

def split_nodes_image(old_nodes):
    return_nodes=[]
    for node in old_nodes:
        text=node.text
        text_list=extract_markdown_images(text)

        if node.text_type!=TextType.TEXT:
            return_nodes.append(node)

        elif len(text_list)==0:
            return_nodes.append(node)

        else:
            for item in text_list:
                start=text.find(item[0])
                if start>2: #can start with ![item]
                    return_nodes.append(TextNode(text[:start-2], TextType.TEXT))
                return_nodes.append(TextNode(item[0], TextType.IMAGES, item[1]))
                text=text[text.find(item[1])+len(item[1])+1:] #location of end of image in string+]
                if len(text)>0:
                    old_nodes.append(TextNode(text, TextType.TEXT))
                 
    return return_nodes


def split_nodes_link(old_nodes):
    return_nodes=[]
    for node in old_nodes:
        text=node.text
        text_list=extract_markdown_links(text)

        if node.text_type!=TextType.TEXT:
            return_nodes.append(node) 

        elif len(text_list)==0:
            return_nodes.append(node)

        else: 
            for item in text_list:
                start=text.find(item[0])
                if start>1: #can start with [item]
                    return_nodes.append(TextNode(text[:start-2], TextType.TEXT))
                return_nodes.append(TextNode(item[0], TextType.LINKS, item[1]))

                text=text[text.find(item[1])+len(item[1])+1:]
                if len(text)>0:
                    old_nodes.append(TextNode(text, TextType.TEXT))

    return return_nodes

def text_to_textnodes(text):
    textnode = TextNode(text, TextType.TEXT)
    nodes = split_nodes_delimiter([textnode], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes

def markdown_to_blocks(markdown):
    strings = markdown.split("\n\n")
    for string in strings:
        string.strip()

    return strings

def block_to_block_type(markdown):
    lines = markdown.split("\n")

    if len(lines)==1 and markdown[0:3] == "```" and markdown[-3:] == "```":
        return "code"
    elif len(lines)==1 and markdown[0] == "#" and markdown.lstrip("#")[0]== " ":
        head_count=markdown.find(" ")
        return f"h{head_count}"
    elif len(list(filter(lambda line: line[0]==">", lines)))==len(lines):
        return "blockquote"
    elif len(list(filter(lambda line: line[0]=="*" or line[0]=="-", lines)))==len(lines):
        return "ul"
    for i in range(0, len(lines)):
        if lines[i].find(f"{i+1}.")!=0:
            return "p"
    return "ol"

def block_markdown_strip(markdown):
    lines = markdown.split("\n")
    
    if len(lines)==1 and markdown[0:3] == "```" and markdown[-3:] == "```":
        return markdown.strip("```")
    elif len(lines)==1 and markdown[0] == "#" and markdown.lstrip("#")[0]== " ":
        head_count=markdown.find(" ")
        return markdown.lstrip("#".lstrip(" "))

    elif len(list(filter(lambda line: line[0]==">", lines)))==len(lines):
        for i in range(0, len(lines)):
            lines[i]=lines[i].lstrip(">").rstrip("<")
            return "\n".join(lines)
    
    return markdown


def markdown_to_html_node(markdown):
    markdown_blocks=markdown_to_blocks(markdown)
    converted_nodes=[]
    
    for block in markdown_blocks:
        converted_nodes.append(ParentNode(block_to_block_type(block), text_to_children(block)))
    
    return ParentNode("div", converted_nodes).to_html()

def text_to_children(text):
    text = block_markdown_strip(text)
    nodes = text_to_textnodes(text)
    convert_nodes=[]
    
    for node in nodes:
        convert_nodes.append(text_node_to_html_node(node))

    return convert_nodes

def extract_title(markdown):
    lines=markdown.split("\n")
    print(lines[:2])
    if lines[0][:2]=="# ":
        return lines[0]
    else:
        raise Exception("no header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as file:
        path_content=file.read()
        file.close()
    with open(from_template) as file:
        template_content=file.read()
        file.close()





