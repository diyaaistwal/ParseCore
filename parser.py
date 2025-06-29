class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

def parse_expression(tokens):
    tokens = tokens[::-1]
    
    def parse_expr():
        node = parse_term()
        while tokens and tokens[-1][1] in ('+', '-'):
            op = tokens.pop()
            right = parse_term()
            node = Node(op[1], [node, right])
        return node

    def parse_term():
        node = parse_factor()
        while tokens and tokens[-1][1] in ('*', '/'):
            op = tokens.pop()
            right = parse_factor()
            node = Node(op[1], [node, right])
        return node

    def parse_factor():
        if not tokens:
            raise SyntaxError("Unexpected end of input")
        token = tokens.pop()
        if token[0] == 'NUMBER' or token[0] == 'ID':
            return Node(token[1])
        elif token[0] == 'LPAREN':
            node = parse_expr()
            if not tokens or tokens.pop()[0] != 'RPAREN':
                raise SyntaxError("Missing closing parenthesis")
            return node
        else:
            raise SyntaxError(f"Unexpected token: {token}")

    root = parse_expr()
    if tokens:
        raise SyntaxError(f"Unexpected token: {tokens[-1]}")
    return root

def evaluate(node):
    if not node.children:
        try:
            return int(node.value)
        except ValueError:
            raise ValueError(f"Cannot evaluate variable: {node.value}")
    left = evaluate(node.children[0])
    right = evaluate(node.children[1])
    if node.value == '+':
        return left + right
    elif node.value == '-':
        return left - right
    elif node.value == '*':
        return left * right
    elif node.value == '/':
        return left / right
    else:
        raise ValueError(f"Unknown operator {node.value}")
