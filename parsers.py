from ply import yacc
from lexer import Lexer
# from nonTerminal import NonTerminal
# from codeGenerator import CodeGenerator

class Parser:

    tokens = Lexer().tokens

    def __init__(self):
        pass
        # self.tempCount = 0
        # self.codeGenerator = CodeGenerator()

    def p_epsilon(self, p):
        'epsilon :'
        pass

    def p_program(self, p):
        "program : declist MAIN LRB RRB block"
        print("program : declist MAIN LRB RRB block")

    #####################
    def p_declist(self, p):
        """declist : dec
                   | declist dec
                   | epsilon"""
        print("declist : dec | declist dec | epsilon")
    ##################

    def p_dec(self, p):
        """dec : vardec
               | funcdec"""
        print("dec : vardec | funcdec")

    def p_type(self, p):
        """type : INTEGER
                | FLOAT
                | BOOLEAN"""
        print("type : INTEGER | FLOAT | BOOLEAN")

    def p_iddec(self, p):
        """iddec : ID
                 | ID LSB exp RSB
                 | ID ASSIGN exp"""
        print("iddec : ID | ID LSB exp RSB | ID ASSIGN exp")

    def p_idlist(self, p):
        """idlist : iddec
                  | idlist COMMA iddec"""
        print("idlist : iddec | idlist COMMA iddec")

    def p_vardec(self, p):
        "vardec : idlist COLON type SEMICOLON"
        print("vardec : idlist COLON type SEMICOLON")

    def p_funcdec(self, p):
        """funcdec : FUNCTION ID LRB paramdecs RRB COLON type block
                   | FUNCTION ID LRB paramdecs RRB block"""
        print("funcdec : FUNCTION ID LRB paramdecs RRB COLON type block | FUNCTION ID LRB paramdecs RRB block")


    def p_paramdecs(self, p):
        """paramdecs : paramdecslist
                     | epsilon"""
        print("paramdecs : paramdecslist | epsilon")


    def p_paramdecslist(self, p):
        """paramdecslist : paramdec
                         | paramdecslist COMMA paramdec"""
        print("paramdecslist : paramdec | paramdecslist COMMA paramdec")

    def p_paramdec(self, p):
        """paramdec : ID COLON type
                    | ID LSB RSB COLON type"""
    print("paramdec : ID COLON type | ID LSB RSB COLON type")


    def p_exp_sum(self, p):
        "exp : exp SUM exp"
        print("exp : exp SUM exp")

    def p_exp_sub(self, p):
        "exp : exp SUB exp"
        print("exp : exp SUB exp")

    def p_exp_mul(self, p):
        "exp : exp MUL exp"
        print("exp : exp MUL exp")

    def p_exp_div(self, p):
        "exp : exp DIV exp"
        print("exp : exp DIV exp")

    def p_exp_integer(self, p):
        "exp : INTEGERNUMBER"
        print("exp : INTEGERNUMBER")
        # p[0] = NonTerminal()
        # p[0].value = p[1]

    precedence = (
        ('left', 'SUM', 'SUB'),
        ('left', 'MUL', 'DIV')
    )

    def p_error(self, p):
        print(p.value)
        raise Exception('ParsingError: invalid grammar at ', p)

    def build(self, **kwargs):
        """build the parser"""
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
