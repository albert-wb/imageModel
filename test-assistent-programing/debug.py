#                                      CÓDIGO COM ERROS                           
# ENTRADA DE DADOS
# A conversão explícita para int (quantidade) e float (valor financeiro) é feita 
# imediatamente na entrada para permitir operações matemáticas mais adiante.
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input(Preço do item 1? ))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
# O valor total de cada item é obtido multiplicando sua quantidade pelo seu preço unitário.
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

# O subtotal agrega os valores de todos os itens e atua como valor base 
# para os cálculos de taxas e descontos.
subtotal = total_item1 + total_item2 + total_item3

# A regra de negócios aplica uma alíquota fixa de imposto de 10% sobre o subtotal.
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
# O desconto incide estritamente sobre o valor dos produtos (subtotal),
# não englobando o valor dos impostos já calculados.
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
# O total real cobrado do cliente repassa o custo dos impostos e abate o benefício do desconto.
total = subtotal + imposto - desconto

# EXIBIÇÃO
# Geração de strings de separação dinâmica para simular o layout de um cupom fiscal no terminal.
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)

# A formatação ':.2f' nas interpolações é utilizada para garantir a 
# exibição padronizada de duas casas decimais, requisito para representação monetária.
print(f" Item 1:        R$ {total_item1:.2f}")
print(" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

# Exibe a linha detalhando o desconto no recibo apenas de forma condicional (se foi aplicado).
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
# Utiliza round() no total para evitar inconsistências de precisão de ponto flutuante,
# garantindo que o valor final exibido bata com a soma matemática das parcelas.
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)