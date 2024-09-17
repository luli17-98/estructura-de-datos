def evaluar_desempeno(nota1, nota2):
    if nota2 > nota1:
        return "Mejoró su desempeño"
    elif nota2 == nota1:
        return "Mantuvo la nota"
    else:
        return "Empeoró su desempeño"

def determinar_estado(promedio):
    if promedio >= 7:
        return "Promocionó la materia"
    elif promedio >= 4:
        return "Debe rendir final"
    else:
        return "Debe recursar"

def cargar_notas_y_evaluar():
    print("Registro de Notas y Evaluación del Alumno")
    
    
    try:
        nota1 = float(input("Ingrese la nota del primer examen: "))
        nota2 = float(input("Ingrese la nota del segundo examen: "))
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")
        return
    
    
    promedio = (nota1 + nota2) / 2
    
    
    if nota2 >= 7:
        resultado_examen = "Aprobó el último examen"
    else:
        resultado_examen = "Desaprobó el último examen"
    
    desempeño = evaluar_desempeno(nota1, nota2)
    
    estado = determinar_estado(promedio)

    print("\n--- Evaluación del Alumno ---")
    print("Nota del primer examen:", nota1)
    print("Nota del segundo examen:", nota2)
    print("Promedio:", promedio)
    print("Resultado del último examen:", resultado_examen)
    print("Desempeño entre exámenes:", desempeño)
    print("Estado del alumno:", estado)

cargar_notas_y_evaluar()
