def sequencia_fibonnacci(num_maximo):
    lista_numeros = [0, 1]

    #Variáveis que serão utilizadas na soma
    num1 = 0
    num2 = 1

    while True:
        #Soma os números, e depois passa o resultado para lista
        resultado = num1 + num2
        num1, num2 = num2, resultado

        if resultado <= num_maximo:
            lista_numeros.append(resultado)

        else:
            break

    return lista_numeros


def numero_pertence_fibonnacci(num, lista_fibonacci):

    if num in lista_fibonacci:
        print(f'O número {num} pertence a sequência Fibonacci.')

    else:
        print(f'O número {num} não pertence a sequência Fibonacci.')


#Programa Principal
print('=== Verificador de numero Fibonacci ===\n')

num = int(input('Digite um número: '))
lista_fibonacci = sequencia_fibonnacci(num)
numero_pertence_fibonnacci(num, lista_fibonacci)
