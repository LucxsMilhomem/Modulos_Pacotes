comp = float(input("Qual o comprimento do Aquário? "))

alt = float(input("Qual a altura do Aquário? "))

larg = float(input("Qual a largura do Aquário? "))

vol = (comp * alt * larg) / 1000

temp_d = float(input("Qual a temperatura desejada? "))

temp_a = float(input("Qual a temperatura ambiente? "))

pot = vol * 0.05 * (temp_d - temp_a)

filt = vol * 2.5

print("Volume do Aquário:", vol,"L")

print("Potência do termostato necessária:", pot)

print("Quantidade  necessária de filtragem por hora:", filt)