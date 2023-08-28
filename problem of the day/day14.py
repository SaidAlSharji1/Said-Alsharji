def evaluate_postfix(expression):
    stack = []

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            stack.append(result)

    return stack[0]

postfix_expression = "231*+9-"
result = evaluate_postfix(postfix_expression)
print("Result:", result)