"""
Dijkstra’s Two-Stack Algorithm for Expression Evaluation

This algorithm evaluates arithmetic expressions written in infix notation using two stacks:
1. **Operand Stack:** Stores numbers (operands).
2. **Operator Stack:** Stores operators (+, -, *, /).

eg: "((3 + 2) * 5)" evaluates to 25

### How It Works:
- **When encountering a number:** Push it onto the operand stack.
- **When encountering an operator:** Push it onto the operator stack.
- **When encountering a left parenthesis (`(`):** Do nothing (it just signifies precedence).
- **When encountering a right parenthesis (`)`)**:
  - Pop an operator from the operator stack.
  - Pop two operands from the operand stack.
  - Apply the operator to these two operands.
  - Push the result back onto the operand stack.
- **When expression is fully parsed:** The operand stack contains the final result.

This ensures correct evaluation based on operator precedence and parentheses.
"""

def evaluate_expression(expression: str) -> int:
    """
    Evaluate an arithmetic expression using Dijkstra’s Two-Stack Algorithm.

    :param expression: str - The arithmetic expression in infix notation.
    :return: int - The result of evaluating the expression.
    """
    operators = []
    operands = []
    
    def push_operator(op: str):
        """Push an operator onto the operator stack."""
        operators.append(op)
    
    def push_operand(val: int):
        """Push an operand onto the operand stack."""
        operands.append(val)
    
    def pop_operator() -> str:
        """Pop and return the top operator from the operator stack."""
        return operators.pop()
    
    def pop_operand() -> int:
        """Pop and return the top operand from the operand stack."""
        return operands.pop()
    
    def apply_operator(op: str, val1: int, val2: int) -> int:
        """
        Applies an operator to two operands.

        :param op: str - The operator ('+', '-', '*', '/').
        :param val1: int - The first operand.
        :param val2: int - The second operand.
        :return: int - The result of applying the operator.
        """
        if op == '+':
            return val1 + val2
        elif op == '-':
            return val1 - val2
        elif op == '*':
            return val1 * val2
        elif op == '/':
            return val1 / val2

    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            push_operand(num)
            continue
        elif char in '+-*/':
            push_operator(char)
        elif char == ')':
            op = pop_operator()
            val2 = pop_operand()
            val1 = pop_operand()
            result = apply_operator(op, val1, val2)
            push_operand(result)
        i += 1
    
    """
    Evaluate the expression one character at a time, the operand stack
    will contain the final result at the end
    """
    
    return pop_operand()
