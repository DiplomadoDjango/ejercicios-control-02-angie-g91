
import math

def main():
    try:
        edad = int(input("Ingresa tu edad: "))
        if edad < 0:
            print("No cumples requisitos")
            return
        
        identificacion = input("¿Tienes identificación oficial? (s/n): ")
        if identificacion.lower() == 's':
            if edad >= 18:
                print("Trámite de licencia concedido")
            else:
                print("No cumples requisitos")
        elif identificacion.lower() == 'n':
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")
    except ValueError:
        print("No cumples requisitos")

if __name__ == "__main__":
    main()
