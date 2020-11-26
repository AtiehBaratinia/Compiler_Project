from lexer import Lexer
from parsers import Parser

if __name__ == "__main__":
    file = open('test3.txt')
    text_input = file.read()
    file.close()
    lexer = Lexer().build()
    lexer.input(text_input)
    # while True:
    #     tok = lexer.token()
    #     if not tok:
    #         break
    #     print(tok)

    parser_p = Parser()
    parser_p.build().parse(text_input, lexer, False)
