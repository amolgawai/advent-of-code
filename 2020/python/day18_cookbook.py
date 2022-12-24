""" Day 18 solution with the help from cookbook"""
import sys
from expr_evaluator import ExpressionEvaluator
from expr_evaluator_1 import ExpressionEvaluator1


def parse_input(input_f_name):
    '''parses input from the given file name and returns data'''
    with open(input_f_name) as input_f:
        data = input_f.readlines()
        # data = input_f.read().split('\n\n')

    # create and return data structure
    data = [ln.strip() for ln in data]
    return data


def get_tot_exprs(evalr, expr_lst):
    """Gets total of expressions from expression list
    Keyword Arguments:
    evalr    -- expression evaluator
    expr_lst -- expression list
    """

    tot = 0
    for expr in expr_lst:
        eval_value = evalr.parse(expr)
        print(eval_value)
        tot += eval_value

    return tot


def main(input_f_name):
    '''The main function'''
    data_struct = parse_input(input_f_name)
    # print(data_struct[3])
    # para_expr = list(parenthetic_contents(data_struct[3]))
    # print(para_expr)
    evalr = ExpressionEvaluator()
    print(get_tot_exprs(evalr, data_struct))

    evalr1 = ExpressionEvaluator1()
    print(get_tot_exprs(evalr1, data_struct))


if __name__ == '__main__':
    main(sys.argv[1])
