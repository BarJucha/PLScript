from antlr4 import *
from NewRules.antlr.PLSRulesV2Parser import PLSRulesV2Parser
from NewRules.antlr.PLSRulesV2Lexer import PLSRulesV2Lexer
from NewRules.antlr.PLSRulesV2Visitor import PLSRulesV2Visitor


def parse_code(input_code):
    input_stream = InputStream(input_code)
    lexer = PLSRulesV2Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PLSRulesV2Parser(token_stream)
    tree = parser.program()
    return tree

def main():
    with open("plsCode.txt", 'r') as file:
        text = file.read()
        tree = parse_code(text)
        visitor = PLSRulesV2Visitor()
        visitor.visit(tree)

if __name__ == "__main__":
    main()