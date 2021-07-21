preço = float(input('Qual é o preço do produto? R$ '))
desc = float(input('Qual é a % de desconto? '))
novo = preço - (preço * desc / 100)

print(f'O preço que custava R${preço :.2f}, na promoção com desconto de {desc :.2f}% vai custar R${novo :.2f} ')