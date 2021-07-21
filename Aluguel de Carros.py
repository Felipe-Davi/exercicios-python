dias = float(input('Quantos dias seu carro foi alugado? '))
km = float(input('Quantos km seu carrou rodou?  '))
valor = (km * 0.15) + (dias * 60)
print(f'o total a pagar é R${valor :.2f}')