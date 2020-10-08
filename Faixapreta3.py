#Laços de repetição
"""
É uma excelente forma de evitar repetição de código
Ele vai executar n vezes uma operação
n => Quatidade de vezes definidas


# for => Nossa palavra-chave para repetição
# variavel => O dado que estamos trabalhando no momento atual
# in => nossa palavra chave para "onde vamos repetir"?

for numero in range(11):
    print(numero)

#    for       numero   in        range(10)
# para cada    numero   onde?     intervalo ate 5

for numero in range(1, 11):
    print('O número atual é:', numero)

texto = 'Trave sim'

for vez in range(10):
    print(vez, texto)

nomes = ['David', 'Noel', 'Ednalva', 'Choquito']
for nome in nomes:
    print('O nome atual é:', nome)
    if nome == 'David':
        print('David')
"""
#Exemplos
"""

#        1  2   3    4  5   6
notas = [5, 10, 7.5, 3, 5, 10]

soma = 0

for nota in notas:
    soma = soma + nota
    # soma = 5 + 10 + 7.5 +3
"""

#Exemplo de listas com uso de len
"""
print('A soma é:', soma)
media = soma / len(notas)
print('A media é', media)


# len => Tamanho em ingles
nomes = ['David', 'noel', 'ednalva']
len(notas)
# range = intervalo em ingles
# range(1, 10) => intervalo de 1 até 10

numero_sorte = 10

numero = int(input('Escolha um numero: '))
if numero != 10:
    print('Errou o numero')
if numero == 10:
    print('Acertou!!!')
"""
"""
lista1 = ['A', 'B', 'C']
lista2 = [1, 2, 3, 4, 5]

tam_lista1 = len(lista1)
tam_lista2 = len(lista2)

print(tam_lista1)
print(tam_lista2)
"""

#Função
"""
#Toda funçao e uma
#if rotina:
#Eu defino (def) uma rotina e a executo quantas
vezes quiser:
É uma excelente forma de deixar nosso ddinamico e sem repetiçãp;
"""
# Definindo a função
"""
def nome_funcao():
    # Código da função
    print('Codigo de função')
# Chamando a função
nome_funcao()

def mostrar_nome():
    print('David B. Nascimento')

def mostrar_nome(nome_atual):
    print(nome_atual)
mostrar_nome('David')
mostrar_nome('Noel')

def calcular_media(nota1, nota2):
    soma = nota1 + nota2
    media = soma / 2
    print(media)
    return media
media_calculada = calcular_media()
"""

#Calculadora Usando somente if (sem def) fiz antes de saber utilizar o (f'{}') clique no mais pf, codigos feitos no pycharm!
"""
escolha = input("Que tipo de conta quer fazer? \n opções: \n  'escolha divisão[0], multiplicação[1], subtração[2] e soma[3]:")
# Divisão = 0
# Multiplicação = 1
# Subtração = 2

if (escolha == "0"):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    divisao = num1 / num2
    resto = num1 % num2
    print()
    print('{} Dividido por {} é: divisao'.format(num1, num2, divisao))
    print('O resto da divisao entre: {} e {} é igual a: {}'.format(num1, num2, resto))

if (escolha == "1"):
    num3 = int(input("Digite o primeiro número: "))
    num4 = int(input("Digite o segundo número: "))
    multiplicação = num3 * num4
    print()
    print('O resultado da multifiplação de {} vezes {} é: {} '.format(num3, num4, multiplicação))

if (escolha == "2"):
    num5 = int(input("Digite o primeiro número: "))
    num6 = int(input("Digite o segundo número:"))
    subtração = num5 - num6
    print()
    print('O resultado da subtração de {} menos {} é: {}'.format(num5, num6, subtração))

if (escolha == "3"):
    num7 = int(input("Digite o primeiro número: "))
    num8 = int(input("Digite o segundo número: "))
    soma = num7 + num8
    print()
    print('O resultado da soma de {} mais {} é: {}'.format(num7, num8, soma))
"""

# Parâmetro/Argumento da função
# É uma maneira de enviar dados para a função
#print('Valor')
#Return
"""
Quando queremos retornar um valor da função, ou seja, a funçao
devolve um valor calculado, nós usamos o Return.
"""
#Exemplos de def! (IMC)

nome = str(input('Olá, Qual é o seu nome? '))
peso = float(input('Me informe seu peso: '))
altura = float(input('Agora sua altura:'))

def numero_quadrado(altura):
    quadrado = altura * altura
    return quadrado

def calcular_imc(peso, altura):
    altura_quadrada = numero_quadrado(altura)
    meu_imc = peso / altura_quadrada
    return meu_imc

def classificar_imc(meu_imc):
    if imc < 18.5:
        print('Abaixo do normal')
    elif imc >= 18.5 and imc < 24.9:
        print('Normal')
    elif imc >= 25 and imc < 29.9:
        print('Pré-obesidade')
    elif imc >= 30 and imc < 34.9:
        print('Obesidade grau um')
    elif imc >= 35 and imc < 39.9:
        print('Obesidade grau dois')
    else:
        print('Obesidade grau três ou mórbida')

imc = calcular_imc(peso, altura)

print(f"Olá {nome}, seu IMC é: %.4f" % imc)
classificar_imc(imc)


