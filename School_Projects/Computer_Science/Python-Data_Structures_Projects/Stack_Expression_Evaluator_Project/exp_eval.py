import operator

from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str: str) -> float:
    '''Evaluates a postfix expression

    Input argument:  a string containing a postfix expression where tokens
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation.
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '>>': operator.rshift,
        '<<': operator.lshift
    }
    stack = Stack(40)
    p_list = input_str.split()
    if len(p_list) == 0:
        raise PostfixFormatException('Empty input')
    for token in p_list:
        if token in operators:
            if stack.size() < 2:
                raise PostfixFormatException('Insufficient operands')
            b = stack.pop()
            a = stack.pop()
            if token == '/' and b == 0:
                raise ValueError('Divisor is Zero')
            if ">>" == token or "<<" == token:
                try:
                    answer = operators[token](a, b)
                except TypeError:
                    raise PostfixFormatException('Illegal bit shift operand')
            else:
                answer = operators[token](a, b)
            stack.push(answer)
        else:
            try:
                if "." in token:
                    stack.push(float(token))
                else:
                    stack.push(int(token))
            except ValueError:
                raise PostfixFormatException('Invalid token')
    if stack.size() > 1:
        raise PostfixFormatException('Too many operands')
    return stack.pop()


def infix_to_postfix(input_str: str) -> str:
    '''Converts an infix expression to an equivalent postfix expression

    Input argument:  a string containing an infix expression where tokens are
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression '''
    Precedence = {
        '+': 1, '-': 1,
        '*': 2, '/': 2,
        '**': 3,
        '>>': 4, '<<': 4
    }

    Associativity = {
        '+': 'L', '-': 'L',
        '*': 'L', '/': 'L',
        '>>': 'L', '<<': 'L',
        '**': 'R'
    }

    stack = Stack(40)
    if len(input_str) == 0:
        raise PostfixFormatException('Empty input')
    p_list = input_str.split()
    new_list = []
    for token in p_list:
        if token.isnumeric():
            new_list.append(token)
        elif token in Precedence:
            while (stack.size() > 0 and stack.peek() != '(' and
                   (Precedence[stack.peek()] > Precedence[token] or
                    (Precedence[stack.peek()] == Precedence[token]
                     and Associativity[token] == 'L'))):
                new_list.append(stack.pop())
            stack.push(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while stack.size() > 0 and stack.peek() != '(':
                new_list.append(stack.pop())
            stack.pop()
    while stack.size() > 0:
        top = stack.pop()
        if top != '(':
            new_list.append(top)
    return ' '.join(new_list)


def prefix_to_postfix(input_str: str) -> str:
    '''Converts a prefix expression to an equivalent postfix expression

    Input argument:  a string containing a prefix expression where tokens are
    space separated.  Tokens are either operators + - * / ** >> << or numbers
    Returns a String containing a postfix expression (tokens are space separated)'''
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '>>': operator.rshift,
        '<<': operator.lshift
    }
    stack = Stack(40)
    if len(input_str) == 0:
        raise PostfixFormatException('Empty input')
    p_list = input_str.split()
    rev_list = p_list[::-1]
    for token in rev_list:
        if token not in operators:
            stack.push(token)
        if token in operators:
            if stack.size() < 2:
                raise PostfixFormatException('Insufficient operands')
            op1 = stack.pop()
            op2 = stack.pop()
            new_string = op1 + ' ' + op2 + ' ' + token
            stack.push(new_string)
    if stack.size() != 1:
        raise PostfixFormatException('Too many operands')
    return stack.pop()






