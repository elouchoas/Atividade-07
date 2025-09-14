# imc.py - cálculo de IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def main():
    try:
        peso = float(input("Peso (kg): ").replace(',', '.'))
        altura = float(input("Altura (m): ").replace(',', '.'))
        if peso <= 0 or altura <= 0:
            print("Valores inválidos. Use números positivos.")
            return
        imc = calcular_imc(peso, altura)
        print(f"IMC = {imc:.2f}")
        if imc < 18.5:
            print("Classificação: Abaixo do peso")
        elif imc < 25:
            print("Classificação: Peso normal")
        elif imc < 30:
            print("Classificação: Sobrepeso")
        else:
            print("Classificação: Obesidade")
    except ValueError:
        print("Entrada inválida. Use apenas números (ex: 70 ou 1.75).")

if __name__ == "__main__":
    main()
