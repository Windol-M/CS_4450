from antlr4 import *
from Deliverable1Lexer import Deliverable1Lexer
from Deliverable1Parser import Deliverable1Parser

def print_tree(node, parser, level=0):
    s = "  " * level
    if isinstance(node, ParserRuleContext):
        print(s + parser.ruleNames[node.getRuleIndex()])
    if hasattr(node, "children") and node.children:
        for c in node.children:
            if hasattr(c, "getRuleIndex"):
                print_tree(c, parser, level + 1)
            else:
                t = c.getText().strip()
                if t:
                    print(f"{s}  └─ {t}")

def main():
    print("Starting the parser: ")
    
    input_file = "../tests/project_deliverable_1.py"
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = Deliverable1Lexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = Deliverable1Parser(tokens)
    
    tree = parser.prog()
    
    print("Parse Tree: ")
    print_tree(tree, parser)

if __name__ == "__main__":
    main()
