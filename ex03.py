altura = float(input("Digite a altura da parede:"))
comprimento= float(input("Digite o comprimento da parede:"))
area = altura*comprimento
qutinta = area*(1/3)
precototal = (qutinta/3.6)*107
print("A quantidade de tinta necessária para cobrir a parede é de: {:.2f}L".format(qutinta))
print("O valor para pintura da parede é de: R${:.2f}".format(precototal))