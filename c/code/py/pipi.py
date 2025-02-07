a = input("")
b = input("")
tamanhoA = len(a)
tamanhoB = len(b)

if a == b:
    print("mesmo conteudo")
else:
    print("conteudo diferente")

if tamanhoA == tamanhoB:
    print("mesmo tamanho")
else:
    print(f"tamaho diferente {tamanhoA} {tamanhoB}")
