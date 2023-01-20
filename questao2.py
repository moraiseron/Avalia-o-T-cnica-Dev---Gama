'''
2. Elabore um programa que leia um número que o usuário digitar. Dependendo do
número informado, das frases abaixo, o sistema imprimirá somente as que forem
verdadeiras.
○ O número é menor que 10.
○ O número é par.
○ O número está entre 8 e 16.
○ O número é 51 ou 80.
Por exemplo, se o usuário digitar o número “12”, o programa irá imprimir:
O número é par.
O número está entre 8 e 16.
Se o usuário digitar o número “51”, então será impresso:
O número é 51 ou 80.
Ou, se o usuário digitar “101”, então o programa não imprime nada.
'''
numero = int(input('Digite um numero: '))
par = numero % 2

if numero < 10:
    print('O número é menor que 10.')

if par == 0:
    print('O número é par.')

if numero >= 8 and numero <= 16:
    print('O número está entre 8 e 16.')

if numero == 51 or 80:
    print('O número é 51 ou 80.')
    

