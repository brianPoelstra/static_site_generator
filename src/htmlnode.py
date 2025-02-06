


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props

    def to_html(self):
        raise NotImplementedError("not yet implemeneted")

    def props_to_html(self):
        return_string=""
        if self.props==None:
            return ""
        for item in self.props:
            return_string+=f' {item}="{self.props[item]}"'

        return return_string
    
    def __eq__(self, other):
        if self.tag==other.tag and self.value==other.value and self.children==other.children and self.props==other.props:
            return True
        else:
            return False


    def __repr__(self):
        child_string=""
        if self.children!=None:
            for child in self.children:
                child_string+=child.props_to_html()

        return(f"tag={self.tag} value={self.value} children={child_string} props={self.props_to_html()}")


