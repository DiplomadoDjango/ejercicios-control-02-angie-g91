def calcular_imc(peso, altura):
    indice = peso / (altura ** 2)
    if peso <= 0 or altura <= 0:
        return "Revisa tus datos, alguno de ellos es erróneo."
    elif indice < 20:
        return "PESO BAJO"
    elif 20 <= indice < 25:
        return "NORMAL"
    elif 25 <= indice < 30:
        return "SOBREPESO"
    elif 30 <= indice < 40:
        return "OBESIDAD"
    else:
        return "OBESIDAD MORBIDA"

def main():
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    
    resultado = calcular_imc(peso, altura)
    print(resultado)


if __name__ == "__main__":
