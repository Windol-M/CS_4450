import sys
from antlr4 import *
from Q1Lexer import Q1Lexer
from Q1Parser import Q1Parser
from Q2Lexer import Q2Lexer
from Q2Parser import Q2Parser
from Q3Lexer import Q3Lexer
from Q3Parser import Q3Parser
from Q4Lexer import Q4Lexer
from Q4Parser import Q4Parser
# from Q5Parser import Q5Parser
# from Q5Lexer import Q5Lexer

# Please feel free to add possible valid and invalid cases to cover the edge cases to check if your parser is valid for given question
# Note: We will be checking for a robust design and so we will 
# add more valid and invalid cases to check the correctness of your parser
valid = [
    ["aa", "aab", "baa", "baab", "abba", "babab"],  # Q1 valid cases
    ["0100", "001000", "111000", "000000"], # Q2 valid cases
    ["00", "1010", "1111", "011"], # Q3 valid cases
    ["aa", "aba", "aabbaa", "abbba"], # Q4 valid cases
    ["11", "111", "011", "10101"], # Q5 valid cases
]
invalid = [
    ["", "aaa", "b", "abb", "aaaa"],  # Q1 invalid cases
    ["010", "101000", "0011000", "11100"], # Q2 invalid cases
    ["1", "1011", "010101", "01110"], # Q3 invalid cases
    ["a", "abb", "aabbba", "aaa"], # Q4 invalid cases
    ["0", "0000", "111111", "01010101"], # Q5 invalid cases
]

lexer_parser_map = {
    1: ("Q1Lexer", "Q1Parser"),
    2: ("Q2Lexer", "Q2Parser"),
    3: ("Q3Lexer", "Q3Parser"),
    4: ("Q4Lexer", "Q4Parser"),
    5: ("Q5Lexer", "Q5Parser"),
}

passed = 0
failed = 0

def print_boxed_message(valid_cases, invalid_cases):
    # Prepare the message
    message = f"The valid and invalid cases are:\nValid: {valid_cases}\nInvalid: {invalid_cases}"

    # Determine the width of the box
    lines = message.split("\n")
    max_length = max(len(line) for line in lines)
    box_width = max_length + 4  # Adding padding on both sides

    # Print the top border
    print("+" + "-" * (box_width - 2) + "+")

    # Print the message with side borders
    for line in lines:
        print(f"| {line.ljust(max_length)} |")

    # Print the bottom border
    print("+" + "-" * (box_width - 2) + "+\n")

def test_cases(test_list, question_no, should_pass):
    global passed, failed
    q_pass = 0
    q_fail = 0
    lexer_class_name, parser_class_name = lexer_parser_map[question_no]
    LexerClass = eval(lexer_class_name)
    ParserClass = eval(parser_class_name)
    
    for test in test_list:
        stream = InputStream(test)
        lexer = LexerClass(stream)
        tokens = CommonTokenStream(lexer)
        parser = ParserClass(tokens)
        parser.start()
        
        # Check if the number of syntax errors matches the expected outcome
        if parser.getNumberOfSyntaxErrors() > 0:
            if should_pass:
                print(f"Valid fail: {test}")
                failed += 1
                q_fail += 1
            else:
                passed += 1
                q_pass += 1
        else:
            if should_pass:
                passed += 1
                q_pass += 1
            else:
                print(f"Invalid fail: {test}")
                failed += 1
                q_fail += 1
    
    # Results for each class
    if should_pass:
        print("\n" + "="*40)  # Add a separator line
        print(f"Results for Positive Test Cases")
        print(f"    Pass: {q_pass} | Fail: {q_fail} | Total: {len(test_list)}")
        print("="*40+"\n")
    else:
        print("\n" + "="*40)
        print(f"Results for Negative Test Cases")
        print(f"    Pass: {q_pass} | Fail: {q_fail} | Total: {len(test_list)}")
        print("="*40+"\n")

for q, cases in enumerate(valid):
    print("#"*60)
    question_no = q+1
    print(f"Question Number: {question_no}\n")
    valid_cases = cases
    invalid_cases = invalid[q]
    print_boxed_message(valid_cases, invalid_cases)
    # Test valid cases
    test_cases(valid_cases, question_no, should_pass=True)
    # Test invalid cases
    test_cases(invalid_cases, question_no, should_pass=False)
    
    print("#"*60 +"\n\n\n")

# Final result
print('Total Passed cases: ' + str(passed))
print('Total Failed cases: ' + str(failed))
