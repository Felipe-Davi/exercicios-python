real = float(input('Quantos reais você têm? R$'))
dolar = real / 5.6
euro = real / 6.8

print(f'Com R${real :.2f} você pode comprar US${dolar :.2f}, \
ou EUR${euro} ')
