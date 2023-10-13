#AP1

#Projeto 1:

import random


def obter_tamanho_do_dado():
    while True:
        entrada = input("Forneça o tamanho do dado que será rolado (ENTER para sair): ")
        if entrada == "":
            return None

        if entrada.isdigit():
            tamanho = int(entrada)
            if tamanho > 0:
                return tamanho
            else:
                print("O tamanho do dado deve ser maior que zero.")
        else:
            print("Por favor, insira um valor numérico maior que zero ou pressione ENTER para sair.")

def obter_numero_de_dados():
    while True:
        entrada = input("Forneça o número de dados que serão rolados (em branco == 1): ")
        if entrada == "":
            return 1

        if entrada.isdigit():
            numero = int(entrada)
            if numero > 0:
                return numero
            else:
                print("O número de dados deve ser maior que zero.")
        else:
            print("Por favor, insira um valor numérico maior que zero ou pressione ENTER para rolar apenas um dado.")

def simular_rolagem_de_dados():
    tamanho_do_dado = obter_tamanho_do_dado()
    if tamanho_do_dado is None:
        return

    numero_de_dados = obter_numero_de_dados()

    resultados = [random.randint(1, tamanho_do_dado) for _ in range(numero_de_dados)]

    print()
    for i, resultado in enumerate(resultados, 1):
        print(f"Lançamento n. {i} - {resultado}")

    print(f"\n{numero_de_dados} dado(s) de {tamanho_do_dado} lados:")

    for resultado in resultados:
        print(resultado)

simular_rolagem_de_dados()


#Projeto 2:

def calcular_soma(n1, n2):
  return n1 + n2

def calcular_subtracao(n1, n2):
  return n1 - n2

def calcular_multiplicacao(n1, n2):
  return n1 * n2

def calcular_divisao(n1, n2):
  if n2 == 0:
      print("Erro: Divisão por zero!")
      return n1
  return n1 / n2

n1 = float(input("Digite o valor de n1: "))

while True:
  n2 = float(input("Digite o valor de n2: "))

  print("""[1] soma
[2] subtração
[3] multiplicação
[4] divisão
[ENTER] desistir""")

  operacao = input("Digite sua operação: ")

  if operacao == "1":
      total = calcular_soma(n1, n2)
  elif operacao == "2":
      total = calcular_subtracao(n1, n2)
  elif operacao == "3":
      total = calcular_multiplicacao(n1, n2)
  elif operacao == "4":
      total = calcular_divisao(n1, n2)
  elif operacao == "":
      print("Obrigado por tentar!")
      break
  else:
      print("Operação inválida. Obrigado por tentar!")
      break

  n1 = total
  print("O resultado da conta é", total)

  cont = input("Deseja continuar com o resultado (c), limpar a conta (X) ou desistir (ENTER)? ")

  if cont == "x" or cont == "X":
      n1 = float(input("Digite o valor de n1: "))
  elif cont == "":
      print("Obrigado por tentar!")
      break
     