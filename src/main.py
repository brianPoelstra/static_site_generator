from textnode import TextNode
from textnode import TextType
from copy_static_to_public import *
def main():
    new_node=TextNode("this is text", TextType.BOLD, "www.text.com")
    new_node_two=TextNode("this is text", TextType.BOLD, "www.text.com")
    new_node_three=TextNode("this is not text", TextType.TEXT, "www.hithere")

    #print(new_node)
    #print(new_node==new_node_two)
    #print(new_node==new_node_three)
    file_path='/home/brian/projects/github.com/brianPoelstra/static_site_generator'
    copy=Copy_To_File(file_path+'/static', file_path+'/public')
    copy.move_files()

main()
