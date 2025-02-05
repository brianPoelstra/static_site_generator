from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.value==None:
            raise ValueError("all leaf nodes require a value")
        if self.tag==None:
            return str(value)
        elif self.tag=="code":
            return f'<pre><{self.tag} {self.props_to_html()}">{self.value}</{self.tag}><pre>'


        return f'<{self.tag} {self.props_to_html()}">{self.value}</{self.tag}>'

