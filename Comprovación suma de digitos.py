#Comprovación suma de digitos 
import random
# Bienvenida
def hola():
    menu = 'Bienvenido a comprovación suma digitos'
    return menu


# Generar un número aleatorio de 5 cifras
def aleatorio():
    global num_str
    num = random.randint(10000, 99999)
    print(f'Número aleatorio de 5 cifras: {num}')

    # Convertir el número en una cadena para poder acceder 
    # a los dígitos individuales
    num_str = str(num)


# Sumar los primeros 3 dígitos y los últimos 2 dígitos
def suma():
    primeros_tres = int(num_str[0]) + int(num_str[1]) + int(num_str[2])
    print(f'Suma primeros 3 números: {primeros_tres}')
    ultimos_dos = int(num_str[3]) + int(num_str[4])
    print(f'Suma ultimos 2 númros: {ultimos_dos}')

    # Comprobar si la suma de los primeros 3 dígitos es igual a la suma de los últimos 2 dígitos
    if primeros_tres == ultimos_dos:
        print("La suma de los primeros 3 dígitos es igual a la suma de los últimos 2 dígitos.")
    else:
        print("La suma de los primeros 3 dígitos no es igual a la suma de los últimos 2 dígitos.")


#llamar funciones
if __name__ == '__main__':
    print(hola())
    print()
    aleatorio()
    suma()

