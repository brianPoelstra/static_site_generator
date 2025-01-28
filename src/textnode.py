from enum import Enum

class TextType(Enum):
    TEXT="text"
    BOLD="bold"
    ITALIC="italic"
    CODE="code"
    LINKS="links"
    IMAGES="images"

class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text=text
        self.url=url
        self.text_type=text_type

    
    def __eq__(self, other):
        if self.text==other.text and self.url==other.url and self.text_type==other.text_type:
            return True
        else:
            return False

    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type.value}, {self.url})")


