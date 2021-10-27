larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print(f'Sua parede tem a dimensão de {larg :.2f}x{alt :.2f} e sua área é {area :.2f}m².')
tinta = area / 2
print(f'Para pintar esta parede, você precisará de {tinta :.2f}L de tinta.')
