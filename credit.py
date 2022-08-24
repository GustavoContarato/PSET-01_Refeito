def Validacao(quantidadeNumero):
  if numeroCartaoLista[0] == 3 and (numeroCartaoLista[1] == 4 or numeroCartaoLista[1] == 7):
      if quantidadeNumero == 15:
        cartao = "American Express"
  elif numeroCartaoLista[0] == 5 and (numeroCartaoLista[1] >= 1 and numeroCartaoLista[1] <= 5):
      if quantidadeNumero == 16:
        cartao = "MasterCard"
  elif numeroCartaoLista[0] == 4:
      if quantidadeNumero == 16:
        cartao = "Visa"
  else:
    print("Cartão Inválido")
  print(cartao)

def AlgoritmoLuhn(quantidadeNumero):
  soma = 0
  aux = 0
  for i in range(quantidadeNumero):
    if i % 2 == 0:
      aux = numeroCartaoLista[i] * 2
      if aux > 9:
        aux -= 9
      soma += aux
    else:
      soma += numeroCartaoLista[i]
  if soma % 10 == 0:
    Validacao(quantidadeNumero)
  else:
    print("Cartão Inválido!")

if __name__ == "__main__":
  numeroCartao = input("Digite o número do cartão: ")
  numeroCartaoLista = []

  #salvando o número em uma lista
  for i in numeroCartao:
    numeroCartaoLista.append(int(i))

  quantidadeNumero = len(numeroCartaoLista)
  AlgoritmoLuhn(quantidadeNumero)
