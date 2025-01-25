from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.value==None:
            raise ValueError("all leaf nodes require a value")
        if self.tag==None:
            return str(value)
        if self.props==None:
            return f"<{tag}>{value}</{tag}>"
        else:
            return f'<{tag} {self.props.keys[0]()} "{self.props.values()[0]}">{value}</{tag}'

