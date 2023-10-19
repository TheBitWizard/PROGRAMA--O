# código sem função

fluxo_caixa = []

def exibir_titulo(titulo):
    print("----------------")
    print(titulo)
    print("----------------")

def inicio():
    exibir_titulo("Fluxo de caixa")
    print("1 - Adicionar receita")
    print("2 - Adicionar despesa")
    print("\n# Digite outro número para encerrar. #\n")

def adicionar_item(tipo, nome, valor):
    fluxo_caixa.append({
            "tipo": tipo,
            "nome": nome,
            "valor": valor * balanco
        })

inicio()

while True:
    tipo = ""
    balanco = 1

    opcao = int( input("Opçao: ") )
    if opcao == 1:
        tipo = "Receita"
    elif opcao == 2:
        tipo = "Despesa"
        balanco = -1
    else:
        exibir_titulo("Nota fiscal")
        break

    nome = input("Nome: ")
    valor = float( input("Valor: ") )

    adicionar_item(tipo, nome, valor)

# nota fiscal
total = 0
for fc in fluxo_caixa:
    print(fc['tipo'], "\tNome:", fc['nome'], "\tValor: R$", fc['valor'])
    total = total + fc['valor']

print("Saldo atual:\tR$", total)