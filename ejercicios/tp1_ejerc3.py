def asignar_aula(dia):
    """Asigna el aula según el día de la semana"""
    if dia % 2 == 0:
        return "A-300"
    else:
        return "A-315"

def calcular_descuento(turno, num_materias, cuota):
    """Calcula el valor de la cuota con descuento basado en el turno y el número de materias"""
    if turno.lower() == "tarde" and num_materias > 3:
        descuento = 0.25
    else:
        descuento = 0.05
    cuota_descuento = cuota * (1 - descuento)
    return cuota_descuento

def calcular_estacionamiento(medio_transporte):
    """Calcula el costo de estacionamiento según el medio de transporte"""
    if medio_transporte.lower() in ["auto", "moto"]:
        return 300
    elif medio_transporte.lower() == "bicicleta":
        return 50
    else:
        return 0

def main():
    # Entrada de datos
    try:
        dia = int(input("Ingrese el número del día (1 al 6): "))
        if dia < 1 or dia > 6:
            raise ValueError("El día debe estar entre 1 y 6.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    aula = asignar_aula(dia)
    print(f"Aula asignada: {aula}")

    try:
        turno = input("Ingrese el turno (mañana/tarde): ").strip()
        num_materias = int(input("Ingrese el número de materias: "))
        cuota = float(input("Ingrese el valor de la cuota: "))
    except ValueError:
        print("Error: Ingrese valores válidos.")
        return

    cuota_descuento = calcular_descuento(turno, num_materias, cuota)
    print(f"Valor de la cuota con descuento: ${cuota_descuento:.2f}")

    medio_transporte = input("Ingrese el medio de transporte (auto/moto/bicicleta): ").strip()
    costo_estacionamiento = calcular_estacionamiento(medio_transporte)
    print(f"Costo diario de estacionamiento: ${costo_estacionamiento:.2f}")

if __name__ == "__main__":
    main()