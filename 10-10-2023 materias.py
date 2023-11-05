
def calcularDefinitiva(parcial,examen,tarea1,tarea2,participacion):
    parcial = 20/100 * parcial
    examen = 40/100 * examen
    tareas = 20/100 * ((tarea1+tarea2)/2)
    participacion = 20/100 * participacion
    
    return (parcial,examen,participacion,tareas)

nombre = str(input("Ingrese su nombre: "))
nombre_materia = str(input("Ingre el nombre de la materia: "))
parcial = float(input("Ingrese la nota del parcial 1: "))
tarea1 = float(input("Ingrese la nota de la tarea 1: "))
tarea2 = float(input("Ingrese la nota de la tarea 2: "))
examen = float(input("Ingrese la nota del examen: "))
participacion = float(input("Ingrese la nota de participación: "))

def calcularClasificacion(nota, materia):
    if materia == "Fundamentos":
        if nota < 2:
            return "malo"
        elif nota >= 2 and nota < 3:
            return "deficiente"
        elif nota >= 3 and nota < 3.8:
            return "regular"
        elif nota >= 3.8 and nota < 4.5:
            return "bueno"
        elif nota >= 4.5 and nota < 5:
            return "Excelente"
        else:
            return "Nota invalida."
    elif materia == "CalculoI":
        if nota < 2:
            return "malo"
        elif nota >= 2 and nota < 3:
            return "deficiente"
        elif nota >= 3 and nota < 3.5:
            return "regular"
        elif nota >= 3.5 and nota < 4.5:
            return "bueno"
        elif nota >= 4.5 and nota < 5:
            return "Excelente"
        else:
            return "Nota invalida"
    elif materia == "Ingles 1":
        if nota < 3:
            return "deficiente"
        elif nota >= 3 and nota < 4:
            return "regular"
        elif nota >= 4 and nota < 4.5:
            return "bueno"
        elif nota >= 4.5 and nota < 5:
            return "Excelente"
        else:
            return "Nota invalida"
    elif materia == "Deporte":
        if nota < 3:
            return "deficiente"
        elif nota >= 3 and nota < 4:
            return "regular"
        elif nota >= 4 and nota <5:
            return "excelente"
        else:
            return "Nota invalida"

if __name__ == '__main__':
    print ("Nombre Alumno: ", nombre)
    print ("Nombre de la asigatura", nombre_materia)
    print ("Clasificación: ", calcularClasificacion())
        
