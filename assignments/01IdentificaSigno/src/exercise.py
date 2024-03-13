def main():
    numero = int(input("Dame un número: "))
    
    if numero > 0:
        print("Es positivo")
    elif numero < 0:
        print("Es negativo")
    else:
        print("Es cero")

if __name__ == "__main__":
    main()

