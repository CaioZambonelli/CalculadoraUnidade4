from funcionalidade.operacoes import soma, subtracao, multiplicacao, divisao


def calculo(num1, num2, operador):

    if operador == '+':
        resultado = soma(num1, num2)
        return resultado
    elif operador == '-':
        resultado = subtracao(num1, num2)
        return resultado
    elif operador == '*':
        resultado = multiplicacao(num1, num2)
        return resultado
    elif operador == '/':
        resultado = divisao(num1, num2)
        return resultado
    else:
        print('Operador inválido')
