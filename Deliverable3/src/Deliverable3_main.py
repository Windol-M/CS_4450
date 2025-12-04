import sys
from antlr4 import *
from Deliverable3Lexer import Deliverable3Lexer
from Deliverable3Parser import Deliverable3Parser

def main():
    print(">>> Running parser...")   # debug print

    if len(sys.argv) < 2:
        print("Usage: python Deliverable3_main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    print(f">>> Reading: {input_file}")  # debug print

    input_stream = FileStream(input_file, encoding="utf-8")

    lexer = Deliverable3Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Deliverable3Parser(token_stream)

    print(">>> Parsing now...")  # debug print
    tree = parser.prog()

    print(">>> Parse complete. Here is the tree:\n")
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()
