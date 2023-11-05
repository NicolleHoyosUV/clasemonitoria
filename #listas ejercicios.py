#listas ejercicios

#EJERCICIO 1
# def pedir_datos(lista):
#     materia = str(input('Ingrese la materia: '))
#     lista.append(materia)
#     return lista


# if __name__ == '__main__':
#     lista = []
#     for i in range(0, 6):
#         pedir_datos(lista)
#     print(lista)

#EJERCICIO 2
def pedir_materias(lista):
    materia = str(input('Ingrese la materia:  '))
    lista.append(materia)
    return lista


if __name__ == '__main__':
    lista = []
    for i in range(0, 6):
        print('Yo estudio la materia: ' + lista[i])

#EJERCICIO 3
def pedir_materias(lista):
    materia = str(input('Ingrese la materia:  '))
    lista.append(materia)
    return lista


def nota():
    nota = float(input('Nota sacada en la asignatura: '))
    return nota


if __name__ == '__main__':
    lista = []

