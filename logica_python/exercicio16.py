graus_celcius = float(input("Digite uma temperatura em Celsius para transformar em fahrenheit: "))

def celsius_para_fahrenheit(graus_celcius):
    return graus_celcius * 1.8 + 32

print (f"A temperatura em graus fahrenheit é de {celsius_para_fahrenheit(graus_celcius)}")