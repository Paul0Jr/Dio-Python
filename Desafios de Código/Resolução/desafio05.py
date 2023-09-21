valor = float(input())

if valor > 0:
    print(f"Deposito realizado com sucesso!\ngSaldo atual: R$ {valor:.2f}")
    #TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
elif valor == 0:
    print("Encerrando o programa...")
   #TODO: Imprimir a mensagem de valor inválido.
else:
    print("Valor invalido! Digite um valor maior que zero.")
  #TODO: Imprimir a mensagem de encerrar o programa.