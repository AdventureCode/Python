salario = float(input("Informe quanto voce ganha por hora: "))
horas = int(input("informe o numero de horas trabalhadas: "))

salarioBruto = salario * horas

IR = salarioBruto * 0.11
INSS = salarioBruto * 0.08
Sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - (IR + INSS + Sindicato)

print("Salario bruto: R$", salarioBruto)
print("INSS: R$", INSS)
print("Sindicato: R$", Sindicato)
print("Salario liquido: R$", salarioLiquido)
