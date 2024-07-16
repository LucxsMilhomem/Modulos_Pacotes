peso = float(input("Qual seu peso? "))

alt = float(input("Qual sua altura? "))

IMC = peso / (alt * alt)

clsf = ""

peso_necessario = 0

if IMC < 18.5:
    clsf = "Baixo Peso"
    peso_necessario = (18.5 * alt * alt) - peso
    print(f"Seu IMC é {IMC:.2f} e você se encaixa no ", clsf, f", precisa ganhar {peso_necessario:.2f}KG para chegar no peso normal.")
    
if IMC >= 18.5 and IMC < 25.0:
    clsf = "Peso Normal"
    print(f"Seu IMC é {IMC:.2f} e você se encaixa no ", clsf)
    
if IMC >= 25.0 and IMC < 30.0:
    clsf = "Excesso de Peso"
    
if IMC >= 30.0 and IMC < 35.0:
    clsf = "Obesidade de Classe 1"
    
if IMC >= 35.0 and IMC < 40.0:
    clsf = "Obesidade de Classe 2"
    
if IMC >= 40.0:
    clsf = "Obesidade de Classe 3"
    
if IMC >= 25.0:
    peso_necessario = peso - (24.9 * alt * alt)
    print(f"Seu IMC é {IMC:.2f} e você se encaixa no ", clsf, f", precisa perder {peso_necessario:.2f}KG para chegar no peso normal.")