from textnode import TextNode, TextType

def main():
    text_node = TextNode("text", TextType.bold, "www.hello.world")
    print(text_node)

if __name__ == "__main__":
    main()
