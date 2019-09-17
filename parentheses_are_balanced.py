#!/usr/bin/python3
"""
Python script (parentheses_are_balanced.py) to checkup for balanced
parentheses in an string literal.
"""

__author__ = 'Ivan Semernyakov'
__email__ = 'beatuminflow@gmail.com'
__date__ = '17.09.2019'


def parantheses_are_balanced(sequence: str) -> bool:
    """
    Function for checking the balance of brackets
    :param sequence: str
    :return: bool
    """

    # List for counting balance
    stack = []  # type: List[str]
    open = ['[', '{', '(']  # type: List[str]
    close = [']', '}', ')']  # type: List[str]

    if len(sequence) <= 1:
        raise ValueError("Sequence can't be empty! Please, add one or more "
                         "caharacters.")
    else:
        # Loop for string literal
        for i in sequence:
            if i in open:
                # Add element to stack
                stack.append(i)
            elif i in close:
                position = close.index(i)
                if len(stack) > 0 and open[position] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False

    if len(stack) == 0:
        return True


if __name__ == "__main__":
    """
    Run script: python parantheses_are_balanced.py
    """

    print('# ' + '=' * 78)
    print(f'Author: {__author__}')
    print(f'Email: {__email__}')
    print(f'Date: {__date__}')
    print('# ' + '=' * 78)

    items = ['{()}[]', '{()}[', '((])}', '(())']

    for i in items:
        print(f'Input: {i}')
        if parantheses_are_balanced(i):
            print("Output: Balanced")
        else:
            print("Output: Not Balanced")
    print('# ' + '=' * 78)
