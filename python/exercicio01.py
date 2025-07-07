# **Exercício:** Escreva um programa em Python que imprima os números de 1 a 100.
# Para múltiplos de três, imprima "Fizz" em vez do número.
# Para múltiplos de cinco, imprima "Buzz".
# Para números que são múltiplos tanto de três quanto de cinco, imprima "FizzBuzz".
# ---



for numero in range (1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        print ("FizzBuzz")
    elif numero % 5 == 0:
        print("buzz"),
    elif numero % 3 == 0:
        print ("fizz")
    else:
        print(numero)

        
