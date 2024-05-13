from antlr4 import *
from ANTLRGenerated.PLSRulesLexer import PLSRulesLexer
from ANTLRGenerated.PLSRulesParser import PLSRulesParser

def parse_code(input_code):
    input_stream = InputStream(input_code)
    lexer = PLSRulesLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PLSRulesParser(token_stream)
    tree = parser.program()
    return tree

def main():
    with open("plsCode.txt", 'r') as file:
        text = file.read()
        parse_code(text)

if __name__ == "__main__":
    main()