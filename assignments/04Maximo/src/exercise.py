def main():
        x = int(input("Ingresa el primer número: "))
        y = int(input("Ingresa el segundo número: "))
        z = int(input("Ingresa el tercer número: "))
        
        if x >= y:
            if x >= z:
                print(x)
            else:
                print(z)
        else:
            if y >= z:
                print(y)
            else:
                print(z)
    except ValueError:
        print("Por favor, ingresa solo números enteros.")

if __name__ == "__main__":
    main()

