print("==============================")
print("$$$ Calculadora Financeira $$$")
print("==============================")

deposito_inicial = int(input("depósito inicial: R$"))
valor_mensal = int(input("qual o valor mensal que você irá depositar?"))
prazo_final = int(input("por quanto tempo você irá fazer este depósito mensal?"))

Total = deposito_inicial+(valor_mensal*prazo_final)

print(f"seu depósito inicial foi de R${deposito_inicial} reais\n") 
print(f"seu valor mensal será de R${valor_mensal} reais\n") 
print(f"você ira depositar {valor_mensal} reais por {prazo_final} meses\n") 
print(f"Ao final de {prazo_final} meses você terá acumulado o valor de {Total} reais\n")
