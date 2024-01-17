from simplify.simplify_expression import simplify_polynomials
import re

def distribute_negation(expression):
    terms = re.split(" ",expression)
    print("terms", terms)
    for index, term in enumerate(terms):
        if index != 0 and term.startswith('-'):
            terms[index] = term.replace('-', '+')
        elif index != 0 and term.startswith('+'):
            terms[index] = term.replace('+', '-')
        elif index == 0 and not term.startswith('-'):
            terms[index] = '-' + term
        elif index == 0 and term.startswith('-'):
            terms[index] = term.replace('-', '')
    result = ''.join(terms)
    return result

def set_up_to_solve_quadratic(equation):
    left, right = equation.split('=')
    left = simplify_polynomials(left)
    right = simplify_polynomials(right)
    # Distribute the negation across the right side
    right = distribute_negation(right)
    result = left + right
    result = simplify_polynomials(result)
    result = result + " = 0"
    return result


def solve_quad_no_factor(equation):
    pass