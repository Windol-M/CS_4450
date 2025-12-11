# CS_4450
Principles of Programming Languages

# CS_4450
Principles of Programming Languages

Project Explaination:

This project implements a custom Python 3.x parser using the ANTLR4 parsing framework. The goal of the project is to design and build a working grammar capable of parsing a well-defined subset of the Python language, as specified across Deliverables 1, 2, and 3 of the assignment. The grammar is written from scratch and is designed to correctly recognize Python’s indentation-sensitive structure, generate a valid parse tree, and handle nested control flow constructs. The parser supports arithmetic expressions, assignment operators, arrays, and basic expression evaluation structures required for Deliverable 1. For Deliverable 2, the grammar extends to conditional statements, including if, elif, and else blocks, along with comparison operators (<, <=, >, >=, ==, !=) and boolean operations (and, or, not). Deliverable 3 expands the grammar further to include iteration structures such as while loops and for loops, nested combinations of loops and conditionals, indentation-based block scoping, and both single-line (# ...) and multi-line (''' ... ''') comments. The results is a functional parser that reads a Python source file, tokenizes it, applies the grammar rules, and outputs a complete parse tree showing the syntactic structure of the program. This parse tree is printed in a readable console format and also saved to a file for inspection. Overall, the project demonstrates how ANTLR4 can be used to construct a domain-specific parser that handles complex language features such as indentation, nested structures, and mixed control flow logic.

Team Members:

Raj Thiara
Windol McNutt

Requirements:

This parser requires Python 3.10 or newer, along with the ANTLR4 Python runtime, which can be installed using:
pip install antlr4-python3-runtime. ANTLR itself must also be installed. This requires downloading the ANTLR 4.13.1 JAR and making sure the antlr4 command is available on the system. The grammar file, Deliverable3.g4, is located inside the grammar/ directory. To generate the lexer and parser files used by the project, the user must run ANTLR from inside the grammar directory using "antlr4 -Dlanguage=Python3 <GrammarFile.g4> -o <output_folder>". This command produces all necessary Python files, including <GrammarFile.g4>Lexer.py and <GrammarFile.g4>Parser.py, which the main script relies on. The project environment should therefore include Python, Java (for ANTLR), and the ANTLR runtime.

How to run:

1. Go to this github "https://github.com/Windol-M/CS_4450"

2. Clone the Repository:
    By opening command prompt. Run the command "git clone <Repository Link>"

3. Then enter the folder using "cd <Your Project Folder>"

4. Install Required Software:
    This includes Installing Python 3, Check version: python --version. Install Java (Required for ANTLR) Check version: java -version. Then Install the ANTLR4 Python Runtime. Then Run: pip install antlr4-python3-runtime. Then Download the ANTLR4 Tool by going to: https://www.antlr.org/download.html. Download the file named similar to: antlr-4.13.1-complete.jar. 

5. Generate Lexer & Parser Files
    Everytime you updated <GrammarFile.g4>, you must regenerate ANTLR files. Then navigate to the grammar folder: cd grammar. Then Run the ANTLR tool manually using Java. Then copy and paste exactly the command below, replacing <PATH> with your actual path to the ANTLR jar: java -jar C:\antlr\antlr-4.13.1-complete.jar, antlr4 -Dlanguage=Python3 <GrammarFile.g4> -o <output_folder>.

6. Test Your Own Files
    To test a different Python file, place it inside the tests/ folder. Then run: python Deliverable3_main.py ../tests/<your_file>.py. Replace <your_file>.py with your filename.



