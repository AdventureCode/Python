q = float(input("Informe o peso: "))

excesso = 0
multa = 0

if(q < 50):
	print("Excesso: ", excesso, "kg")
	print("Multa: " , multa)
else:
	excesso = q - 50
	multa = 4 * excesso
	print("Excesso: ", excesso,"kg")
	print("Multa: R$", multa)
