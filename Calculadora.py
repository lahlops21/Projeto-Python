# Calculadora

resultado = 0
usuario = 0
opcao = '1'
print('Bem vindo à nossa Calculadora!')
print('=-' * 30)

while opcao != 's':
  print('')
  print('Escolha entre as seguintes opções: ')
  print('[1] Somar')
  print('[2] Multiplicar')
  print('[3] Saber qual o maior')
  print('[4] Novos números')
  print('[s] Sair do programa')
  usuario = int(input('Insira o 1o valor: '))
  usuario2 = int(input('Insira o 2o valor: '))
  opcao = input('O que você gostaria de fazer? ')

# Criando as condições

  if opcao == '1':
    print('Você escolheu somar!')
    resultado = usuario + usuario2
    print(f' {usuario} + {usuario2} = {resultado}')

  elif opcao == '2':
    print('Você escolheu multiplicar!')
    resultado = usuario * usuario2
    print(f'{usuario} x {usuario2} = {resultado}')

  elif opcao == '3':
    print('Você decidiu saber qual deles é o maior')
    if usuario > usuario2:
      print(f'{usuario} é maior que {usuario2}')
    elif usuario < usuario2:
      print(f'{usuario2} é maior que {usuario}')
    elif usuario == usuario2:
      print('Eles são iguais')

  elif opcao == '4':
    print('Escolha novos números: ')

print('')
print('Obrigada por usar nossa calculadora!')
print('Até breve!')