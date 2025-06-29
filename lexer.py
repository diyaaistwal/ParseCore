import re

TOKEN_SPECIFICATION = [
    ('NUMBER',   r'\d+'),
    ('ID',       r'[a-zA-Z_]\w*'),
    ('OP',       r'[+\-*/]'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('SKIP',     r'[ \t]+'),
    ('MISMATCH', r'.'),
]

def tokenize(code):
    tokens = []
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER' or kind == 'ID' or kind == 'OP' or kind in ('LPAREN', 'RPAREN'):
            tokens.append((kind, value))
        elif kind == 'MISMATCH':
            raise SyntaxError(f'Unexpected token {value}')
    return tokens
