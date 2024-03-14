def es_bisiesto(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def siguiente_fecha(year, month, day):
    # Definir el número de días por mes (considerando si es bisiesto)
    days_in_month = [31, 28 + es_bisiesto(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Determinar si es el último día del mes y si el mes siguiente es diciembre
    if day == days_in_month[month - 1] and month == 12:
        year += 1
        month = 1
        day = 1
    # Determinar si es el último día del mes
    elif day == days_in_month[month - 1]:
        month += 1
        day = 1
    # Determinar si es el 29 de febrero
    elif month == 2 and day == 28 and es_bisiesto(year):
        day += 1
    # Si no se cumple ninguna condición especial, simplemente aumentamos el día
    else:
        day += 1

    return year, month, day

def main():
    # Obtener la fecha
    year = int(input("Año: "))
    month = int(input("Mes: "))
    day = int(input("Día: "))

    # Calcular la siguiente fecha
    next_year, next_month, next_day = siguiente_fecha(year, month, day)

    # Imprimir la siguiente fecha
    print(next_year)
    print(next_month)
    print(next_day)

if __name__ == "__main__":
    main()
