from ply import lex


class Lexer:

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
                 , 'RSB', 'SEMICOLON', 'COLON', 'COMMA', 'ID', 'ERROR'
             ]
    tokens += reserved.values()
    # t_TRUE = r'True'
    # t_FALSE = r'False'

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
    t_ignore = ' \t'

    def t_TRUE(self, t):
        r'True'
        return t

    def t_FALSE(self, t):
        r'False'
        return

    # def t_ERROR(self, t):
    #     r'(ERROR)|([\+\-\*\/\%](\s*[\+\-\*\/\%])+)|([A-Z0-9]+[_a-z]+)|([0-9]{9}[0-9]+([.][0-9]*)?)|([0-9]+[.][0-9]+([.][0-9]+)+)'
    #     return t

    def t_ID(self, t):
        r'[a-z_][_a-zA-Z0-9]*'
        if t.value in self.reserved:
            t.type = self.reserved[t.value]
        return t

    def t_FLOATNUMBER(self, t):
        r'[0-9]{1,9}[.][0-9]+'
        t.value = str(float(t.value))
        return t

    def t_INTEGERNUMBER(self, t):
        r'[0-9]{1,9}'
        t.value = str(int(t.value))
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # def t_ERROR(self, t):
    #     r'[A-Z0-9][_a-zA-Z0-9]*'
    #     return t

    def t_error(self, t):
        i = 0
        while t.value[i] != " ":
            i += 1
        t.lexer.skip(i)
        return 'ERROR'

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer
