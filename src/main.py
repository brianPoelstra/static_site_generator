from textnode import TextNode
from textnode import TextType

def main():
    new_node=TextNode("this is text", TextType.BOLD, "www.text.com")
    new_node_two=TextNode("this is text", TextType.BOLD, "www.text.com")
    new_node_three=TextNode("this is not text", TextType.NORMAL, "www.hithere")

    print(new_node)
    print(new_node==new_node_two)
    print(new_node==new_node_three)

main()
