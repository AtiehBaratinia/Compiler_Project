from ply import lex


class Lexer:
    # tokens = [
    #     'INTEGERNUMBER', 'FLOATNUMBER',
    #     'INTEGER', 'FLOAT', 'BOOLEAN', 'FUNCTION', 'TRUE', 'FALSE', 'PRINT', 'RETURN', 'MAIN',
    #     'IF', 'ELSE', 'ELSEIF', 'WHILE', 'ON', 'WHERE', 'FOR', 'AND', 'OR', 'NOT', 'IN',
    #     'ASSIGN', 'SUM', 'SUB', 'MUL', 'DIV'
    #     , 'MOD', 'GT', 'GE', 'LT', 'LE', 'EQ', 'NE', 'LCB', 'RCB', 'LRB', 'RRB', 'LSB'
    #     , 'RSB', 'SEMICOLON', 'COLON', 'COMMA', 'ID'
    # ]

    reserved = {
        'if': 'IF',
        'then': 'THEN', 'int': 'INTEGER', 'float': 'FLOAT', 'bool': 'BOOLEAN', 'fun': 'FUNCTION', 'print': 'PRINT',
        'return': 'RETURN', 'main': 'MAIN', 'else': 'ELSE',
        'while': 'WHILE',
        'elseif': 'ELSEIF',
        'on': 'ON',
        'where': 'WHERE', 'for': 'FOR', 'and': 'AND', 'or': 'OR', 'not': 'NOT', 'in': 'IN'
    }

    tokens = [
                 'INTEGERNUMBER', 'FLOATNUMBER',
                 'TRUE', 'FALSE',
                 'ASSIGN', 'SUM', 'SUB', 'MUL', 'DIV'
                 , 'MOD', 'GT', 'GE', 'LT', 'LE', 'EQ', 'NE', 'LCB', 'RCB', 'LRB', 'RRB', 'LSB'
                 , 'RSB', 'SEMICOLON', 'COLON', 'COMMA', 'ID'
             ] + list(reserved.values())

    t_TRUE = r'True'
    t_FALSE = r'False'

    t_ASSIGN = r'\='
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_MOD = r'\%'
    t_GT = r'\>'
    t_GE = r'\>='
    t_LT = r'\<'
    t_LE = r'\<='
    t_EQ = r'\=='
    t_NE = r'\!='
    t_LCB = r'\{'
    t_RCB = r'\}'
    t_LRB = r'\('
    t_RRB = r'\)'
    t_LSB = r'\['
    t_RSB = r'\]'
    t_SEMICOLON = r';'
    t_COLON = r':'
    t_COMMA = r','

    def t_ID(self, t):
        r'[a-z_][_a-zA-Z0-9]*'
        # t.type = reserved.get(t.value, 'ID')
        return t

    def t_FLOATNUMBER(self, t):
        r'[-+]?[1-9][0-9]*[.][0-9]*[1-9]'
        return t


    def t_INTEGERNUMBER(self, t):
        r'[-+]?[1-9][0-9]* | 0'
        return t


    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = '\n \t'

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer
