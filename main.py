from lexer import Lexer
# from parser import Parser

if __name__ == "__main__":
    lexer = Lexer().build()
    file = open('test1.txt')
    text_input = file.read()
    file.close()
    lexer.input(text_input)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
    # parser = Parser()
    # parser.build().parse(text_input, lexer, False)
