#!/urs/bin/python
#-*- coding: utf-8 -*-

# Condicional SE
nota1 = 1.00
nota2 = 7.00
media = (nota1 + nota2) / 2

if(media >= 7.00):
	print("O aluno foi aprovado!\n")
	print("Parabéns!")
else:
	if media >= 5.00:
		print("Aluno em recuperação")
	else:	
		print("O aluno foi reprovado!\n")
		print("Estude mais!!!")
	
print("A média é %f " %media)
