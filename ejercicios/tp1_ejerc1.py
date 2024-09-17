def registrar_alumno():
    
    print("Registro de Inscripción de Alumnos")

    
    nombre = input("Ingrese el nombre del alumno: ")
    edad = int(input("Ingrese la edad del alumno: "))
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (dd/mm/aaaa): ")
    
    
    tiene_titulo_secundario = True  
    
    monto_matricula = float(input("Ingrese el monto de matrícula: "))
    
    
    cuota = monto_matricula + 1000
    
    
    arancel_python_i = 12000/4


 
    pago_efectivo = input("¿El alumno pagará en efectivo? (sí/no): ").strip().lower()
    
    pago_efectivo == "sí"

    cuota_descuento = arancel_python_i - (arancel_python_i * 0.15)
    print()
    print("=============================================")
    print("\n===Universidad de Python - Inscriciones ===")
    print("=============================================")
    print()
    print("DATOS DE INGRESO")
    print("Nombre:",nombre)
    print("Edad:",edad)
    print("Fecha de Nacimiento:" ,fecha_nacimiento)
    print("Tiene título secundario:",tiene_titulo_secundario)
    print("Monto de matrícula: $",monto_matricula)
    print("la cuota mensual: $",cuota)
    print("arancel_python (sin descuento): $",arancel_python_i)
    print("arancel_python con descuento: $ ",cuota_descuento)


registrar_alumno()