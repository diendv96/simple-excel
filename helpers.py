def convert_reverse_polish_to_infix(expression):
    expression = expression.split(" ")
    operands = {'+', '-', '*', '/'}
    operand_stack = []
    for ch in expression:
        if ch not in operands:
            operand_stack.append(ch)
        elif ch in operands:
            if len(operand_stack) < 2:
                return None
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            operand_stack.append('(' + op1 + ch + op2 + ')')
    return operand_stack.pop()
