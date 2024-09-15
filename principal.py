from utilidades.auxiliares import mensagem_inicial
from funcionalidade.calculo import calculo


if __name__ == "__main__":
    mensagem_inicial()

    num1 = float(input())
    operador = input()
    num2 = float(input())

    resultado = calculo(num1, num2, operador)
    print('-------')
    print(resultado)

    operador = input()

    while operador != 'x':
        num1 = resultado
        num2 = float(input())
        resultado = calculo(num1, num2, operador)
        print('-------')
        print(resultado)
        operador = input()

    print('Programa encerrado! <3')