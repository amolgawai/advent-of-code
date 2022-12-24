'''Day 18 solution'''
import sys
import re
from collections import namedtuple, deque


NUM    = r'(?P<NUM>\d+)'
PLUS   = r'(?P<PLUS>\+)'
MINUS  = r'(?P<MINUS>-)'
TIMES  = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS     = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES,
                                  DIVIDE, LPAREN, RPAREN, WS]))

# Tokenizer
Token = namedtuple('Token', ['type', 'value'])


def generate_tokens(text):
    """Generates tokens from the text
    """
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok


def parse_input(input_f_name):
    '''parses input from the given file name and returns data'''
    with open(input_f_name) as input_f:
        data = input_f.readlines()
        # data = input_f.read().split('\n\n')

    # create and return data structure
    data = [ln.strip() for ln in data]
    return data


def evaluate_expre(expr):
    """Evaluates the expression and returns the result
    Keyword Arguments:
    expr -- expression to be evaluated
    """
    print(expr)
    # if expr.find('(') != -1:
    #     para_expr = list(parenthetic_contents(expr))
    #     print(para_expr)
    statements = deque()
    for a_token in generate_tokens(expr):
        print(a_token)


def main(input_f_name):
    '''The main function'''
    data_struct = parse_input(input_f_name)
    # print(data_struct[3])
    # para_expr = list(parenthetic_contents(data_struct[3]))
    # print(para_expr)
    for expr in data_struct:
        evaluate_expre(expr)


if __name__ == '__main__':
    main(sys.argv[1])
