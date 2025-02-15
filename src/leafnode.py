from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("value cannot be None.")
        if not self.tag:
            return self.value    
        else:
            return f"<{self.tag}{self.__get_props()}>{self.value}</{self.tag}>"
        
    def __get_props(self):
        return self.props_to_html()    