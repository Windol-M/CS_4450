import sys
from antlr4 import *
from Deliverable3Lexer import Deliverable3Lexer
from Deliverable3Parser import Deliverable3Parser
from antlr4.tree.Trees import Trees

# -----------------------------
# Pretty-printing function
# -----------------------------
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


# -----------------------------
# Main program
# -----------------------------
def main(argv):
    if len(argv) < 2:
        print("Usage: python Deliverable3_main.py <inputfile>")
        return

    # Load input file
    input_stream = FileStream(argv[1], encoding='utf-8')

    # Create lexer + parser
    lexer = Deliverable3Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Deliverable3Parser(token_stream)

    # Parse
    tree = parser.prog()

    # ========== Print in terminal ==========
    print("\n===== ANTLR toStringTree =====")
    print(tree.toStringTree(recog=parser))

    # ========== Pretty-print to terminal ==========
    print("\n===== Pretty Printed Tree (first part) =====")
    print_tree(tree, parser)

    # ========== SAVE FULL TREE TO FILE ==========
    print("\nSaving full pretty tree to parse_tree.txt ...")

    with open("parse_tree.txt", "w", encoding="utf-8") as f:
        # Temporarily redirect stdout into the file
        original_stdout = sys.stdout
        sys.stdout = f
        print_tree(tree, parser)
        sys.stdout = original_stdout

    print("Done! Tree saved to parse_tree.txt\n")


# -----------------------------
# Run program
# -----------------------------
if __name__ == "__main__":
    main(sys.argv)
