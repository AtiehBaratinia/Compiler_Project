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

    def p_block(self, p):
        "block : LCB stmtlist RCB"

        print("block : LCB stmtlist RCB")

    def p_stmtlist(self, p):
        """stmtlist : stmt
        | stmtlist stmt
        | epsilon"""

        print("stmtlist : stmt | stmtlist stmt | epsilon")

    def p_lvalue(self, p):
        """lvalue : ID
        | ID LSB exp RSB"""

        print("lvalue : ID | ID LSB exp RSB")

    def p_case(self, p):
        "case : WHERE const COLON stmtlist"

        print("case : WHERE const COLON stmtlist")

    def p_cases(self, p):
        """cases : case
        | cases case
        | epsilon"""

        print("cases : case | cases case | epsilon")

    def p_stmt(self, p):
        """stmt : RETURN exp SEMICOLON
        | exp SEMICOLON
        | block
        | vardec
        | WHILE LRB exp RRB stmt
        | ON LRB exp RRB LCB cases RCB SEMICOLON
        | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt
        | FOR LRB ID IN ID RRB stmt
        | IF LRB exp RRB stmt elseiflist
        | IF LRB exp RRB stmt elseiflist ELSE stmt
        | PRINT LRB ID RRB SEMICOLON"""

        print("""stmt : RETURN exp SEMICOLON | exp SEMICOLON | block | vardec
        | WHILE LRB exp RRB stmt | ON LRB exp RRB LCB cases RCB SEMICOLON
        | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt | FOR LRB ID IN ID RRB stmt
        | IF LRB exp RRB stmt elseiflist | IF LRB exp RRB stmt elseiflist ELSE stmt
        | PRINT LRB ID RRB SEMICOLON""")

    def p_elseiflist(self, p):
        # """elseiflist : ELSEIF LRB exp RRB stmt
        # | elseiflist ELSEIF LRB exp RRB stmt
        # | epsilon"""
        """elseiflist : elseiflist ELSEIF LRB exp RRB stmt
        | epsilon"""

        print("elseiflist : elseiflist ELSEIF LRB exp RRB stmt | epsilon")

    def p_relopexp(self, p):
        """relopexp : exp relop exp
        | relopexp relop exp"""

        print("relopexp : exp relop exp | relopexp relop exp")

    def p_exp(self, p):
        """exp : ID LSB exp RSB ASSIGN exp
        | ID ASSIGN exp
        | exp operator exp
        | relopexp
        | const
        | lvalue
        | ID LRB explist RRB
        | LRB exp RRB
        | ID LRB RRB
        | SUB exp
        | NOT exp"""

        print("""exp : lvalue ASSIGN exp | exp operator exp | relopexp |
        const | lvalue | ID LRB explist RRB | LRB exp RRB | ID LRB RRB | SUB exp | NOT exp""")

    def p_operator(self, p):
        """operator : AND
        | OR
        | SUM
        | SUB
        | MUL
        | DIV
        | MOD"""

        print("operator : AND | OR | SUM | SUB | MUL | DIV | MOD")

    def p_const(self, p):
        """const : INTEGERNUMBER
        | FLOATNUMBER
        | TRUE
        | FALSE"""

        print("const : INTEGER | FLOAT | True | False")

    def p_relop(self, p):
        """relop : GT
        | LT
        | NE
        | EQ
        | LE
        | GE"""

        print("relop : GT | LT | NE | EQ | LE | GE")

    def p_explist(self, p):
        """explist : exp
        | explist COMMA exp"""

        print("explist : exp | explist COMMA exp")

    # def p_exp_sum(self, p):
    #     "exp : exp SUM exp"
    #
    #     print("exp : exp SUM exp")
    #
    # def p_exp_sub(self, p):
    #     "exp : exp SUB exp"
    #
    #     print("exp : exp SUB exp")
    #
    # def p_exp_mul(self, p):
    #     "exp : exp MUL exp"
    #
    #     print("exp : exp MUL exp")
    #
    # def p_exp_div(self, p):
    #     "exp : exp DIV exp"
    #
    #     print("exp : exp DIV exp")
    #
    # def p_exp_integer(self, p):
    #     "expdfg : INTEGERNUMBER"
    #
    #     print("exp : INTEGERNUMBER")
    #     # p[0] = NonTerminal()
    #     # p[0].value = p[1]

    def p_epsilon(self, p):
        'epsilon :'
        pass

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
