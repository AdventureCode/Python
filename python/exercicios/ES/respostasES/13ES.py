h = float(input("Informe a sua altura: "))
s = input("m = Masculino, f = feminino: ")
p = float(input("Informe seu peso: "))


if(s == 'm' or s == 'M'):
	idM = (72.7 * h) - 58
	if(p < idM):
		print("Abaixo do peso ideal.")
	else:
		print("Acima do peso ideal.")
elif(s == 's' or s == 'S'):
	idF = (62.1 * h) - 44.7
	if(s < idF):
		print("Abaixo do peso ideal.")
	else:
		print("Acima do peso ideal.")
else:
	print("ERRO!")
