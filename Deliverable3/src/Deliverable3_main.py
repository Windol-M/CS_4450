import sys
from antlr4 import *
from Deliverable3Lexer import Deliverable3Lexer
from Deliverable3Parser import Deliverable3Parser
from antlr4.tree.Trees import Trees

# Put the path to the input test file here
input = "../tests/project_deliverable_3.py"

def print_tree(node, parser, indent=0):
    """Recursively pretty-print the ANTLR parse tree."""
    rule_names = parser.ruleNames

    # Node label
    try:
        text = Trees.getNodeText(node, rule_names)
    except:
        text = str(node)

    print("  " * indent + str(text))

    # Print children
    for child in getattr(node, "children", []):
        print_tree(child, parser, indent + 1)


def main(argv):

    # Load input file
    input_stream = FileStream(input, encoding='utf-8')

    # Create lexer + parser
    lexer = Deliverable3Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Deliverable3Parser(token_stream)

    # Parse
    tree = parser.prog()

    # Uncomment to see a string tree representation
    # print("\nANTLR toStringTree")
    # print(tree.toStringTree(recog=parser))

    # Human friendly printout
    print("\nTree (in terminal):")
    print_tree(tree, parser)

    
    print("\nSaving tree to parse_tree.txt")

    with open("parse_tree.txt", "w", encoding="utf-8") as f:
        # Temporarily redirect stdout into the file
        original_stdout = sys.stdout
        sys.stdout = f
        print_tree(tree, parser)
        sys.stdout = original_stdout

    print("Tree saved to parse_tree.txt\n")


if __name__ == "__main__":
    main(sys.argv)
