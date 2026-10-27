# Análise de variação de preços da cesta básica
# Entrada: nome, preço do mês anterior e preço do mês atual de 3 produtos
# Saída: preços, variação percentual e situação (AUMENTO, QUEDA ou ESTÁVEL)

def ler_preco(mensagem):
    """Lê um preço digitado pelo usuário, aceitando vírgula ou ponto."""
    return float(input(mensagem).replace(",", "."))


# LEITURA
nomeprod1 = input("Digite o nome do primeiro produto: ")
valorantprod1 = ler_preco("Digite o preço do primeiro produto no mês anterior: ")
valoratualprod1 = ler_preco("Digite o preço do primeiro produto no mês atual: ")

nomeprod2 = input("Digite o nome do segundo produto: ")
valorantprod2 = ler_preco("Digite o preço do segundo produto no mês anterior: ")
valoratualprod2 = ler_preco("Digite o preço do segundo produto no mês atual: ")

nomeprod3 = input("Digite o nome do terceiro produto: ")
valorantprod3 = ler_preco("Digite o preço do terceiro produto no mês anterior: ")
valoratualprod3 = ler_preco("Digite o preço do terceiro produto no mês atual: ")

# CÁLCULO
variacaoprod1 = (valoratualprod1 - valorantprod1) / valorantprod1 * 100
variacaoprod2 = (valoratualprod2 - valorantprod2) / valorantprod2 * 100
variacaoprod3 = (valoratualprod3 - valorantprod3) / valorantprod3 * 100

# DECISÃO
if variacaoprod1 > 0:
    situacaoprod1 = "AUMENTO"
elif variacaoprod1 < 0:
    situacaoprod1 = "QUEDA"
else:
    situacaoprod1 = "ESTÁVEL"

if variacaoprod2 > 0:
    situacaoprod2 = "AUMENTO"
elif variacaoprod2 < 0:
    situacaoprod2 = "QUEDA"
else:
    situacaoprod2 = "ESTÁVEL"

if variacaoprod3 > 0:
    situacaoprod3 = "AUMENTO"
elif variacaoprod3 < 0:
    situacaoprod3 = "QUEDA"
else:
    situacaoprod3 = "ESTÁVEL"

# SAÍDA
print()
print("========== ANÁLISE DA CESTA BÁSICA ==========")
print()

print("----- PRODUTO 1 -----")
print("Produto:", nomeprod1)
print(f"Preço anterior: R$ {valorantprod1:.2f}")
print(f"Preço atual: R$ {valoratualprod1:.2f}")
print(f"Variação: {variacaoprod1:.2f}%")
print("Situação:", situacaoprod1)
print()

print("----- PRODUTO 2 -----")
print("Produto:", nomeprod2)
print(f"Preço anterior: R$ {valorantprod2:.2f}")
print(f"Preço atual: R$ {valoratualprod2:.2f}")
print(f"Variação: {variacaoprod2:.2f}%")
print("Situação:", situacaoprod2)
print()

print("----- PRODUTO 3 -----")
print("Produto:", nomeprod3)
print(f"Preço anterior: R$ {valorantprod3:.2f}")
print(f"Preço atual: R$ {valoratualprod3:.2f}")
print(f"Variação: {variacaoprod3:.2f}%")
print("Situação:", situacaoprod3)
