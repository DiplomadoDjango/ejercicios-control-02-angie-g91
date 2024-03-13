import math

def main():
    try:
        numero = int(input("Dame un número: "))
        
        if numero > 0:
            print("Es positivo")
        elif numero < 0:
            print("Es negativo")
        else:
            print("Es cero")
    except ValueError:
        print("Por favor ingresa un número entero válido.")

if __name__ == "__main__":
    main()

