def main():
    try:
        x = int(input("Ingresa el primer número: "))
        y = int(input("Ingresa el segundo número: "))
        z = int(input("Ingresa el tercer número: "))
        
        if x <= y and x <= z:
            print(x)
            if y <= z:
                print(y)
                print(z)
            else:
                print(z)
                print(y)
        elif y <= x and y <= z:
            print(y)
            if x <= z:
                print(x)
                print(z)
            else:
                print(z)
                print(x)
        else:
            print(z)
            if x <= y:
                print(x)
                print(y)
            else:
                print(y)
                print(x)
    except ValueError:
        print("Por favor, ingresa solo números enteros.")

if __name__ == "__main__":
    main()
