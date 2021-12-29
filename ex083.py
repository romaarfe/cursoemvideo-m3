x = str(input('Digite uma expressão usando parênteses: '))
exp = []
for simb in x:
    if simb == '(':
        exp.append('(')
    elif simb == ')':
        if len(exp) > 0:
            exp.pop()
        else:
            exp.append(')')
            break
if len(exp) == 0:
    print('Esta expressão é válida.')
else:
    print('Esta expressão não é válida!')
