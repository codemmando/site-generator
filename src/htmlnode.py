class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented!")
    
    def props_to_html(self):
        props_html_string = ""
        for prop in self.props:
            props_html_string += f' {prop}="{self.props[prop]}"'
        return props_html_string

    def __repr___(self):
        return f"HTMLNode: tag={self.tag} value={self.value} children={self.children} props={self.props}"    