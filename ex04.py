premio = float(input("Digite o valor do premio:"))
desconto = premio*(7/100)
premiodescontado = premio-desconto
p1 = premiodescontado-(premiodescontado*(46/100))
p2 = (premiodescontado)*(32/100)
p3 = premiodescontado-(p1+p2)
print("O total do premio foi: R${}".format(premio))
print("O valor do premio com impostos é de: R${:.2f}".format(premiodescontado))
print("O valor descontado do premio foi de: R${:.2f}".format(desconto))
print("O primeiro ganhador recebeu: R${:.2f}".format(p1))
print("O segundo ganhador recebeu: R${:.2f}".format(p2))
print("O terceiro ganhador recebeu: R${:.2f}".format(p3))