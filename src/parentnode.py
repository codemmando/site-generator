from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode: tag cannot be None.")
        if not self.children:
            raise ValueError("ParentNode: children cannot be None.")
        else:
            children_html = ""
            for child in self.children:
                children_html += child.to_html()
            return f"<{self.tag}{self.__get_props()}>{children_html}</{self.tag}>"
        
    def __get_props(self):
        return self.props_to_html()    

