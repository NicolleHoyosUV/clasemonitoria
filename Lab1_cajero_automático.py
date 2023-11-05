#Cajero Automático

#Bienvenida
def hello():
    menu = 'Bienvenido al cajero automatico'
    return menu


# Definir la lista de tarjetas con sus respectivas claves y saldos disponibles
def cards_list():
    global tarjetas
    tarjetas = [
        {"numero": "1234567890", "clave": "1234", "saldo": 10000},
        {"numero": "0987654321", "clave": "4321", "saldo": 5000},
        {"numero": "5678901234", "clave": "5678", "saldo": 20000}
    ]


# Solicitar al usuario que ingrese el número de tarjeta
def entrance():
    global numero_tarjeta
    numero_tarjeta = input("Por favor, ingrese el número de su tarjeta: ")


# Verificar si el número de tarjeta ingresado se encuentra en la lista de tarjetas
def valid_card():
    global tarjeta_valida, tarjeta_seleccionada
    tarjeta_valida = False
    for tarjeta in tarjetas:
        if tarjeta["numero"] == numero_tarjeta:
            tarjeta_valida = True
            tarjeta_seleccionada = tarjeta
            break


def process():
    if tarjeta_valida:
        # Solicitar al usuario que ingrese la clave
        clave = input("Por favor, ingrese su clave: ")

        # Verificar si la clave ingresada coincide con la clave asociada a la tarjeta
        if clave == tarjeta_seleccionada["clave"]:
            # Verificar si el saldo de la tarjeta es mayor o igual a $10,000
            if tarjeta_seleccionada["saldo"] >= 10000:
                # Solicitar al usuario que ingrese el monto a retirar
                monto = int(input("Por favor, ingrese el monto a retirar: "))

                # Verificar si el monto a retirar es menor o igual al saldo disponible en la tarjeta
                if monto <= tarjeta_seleccionada["saldo"]:
                    # Realizar el retiro y actualizar el saldo restante
                    tarjeta_seleccionada["saldo"] -= monto

                    # Entregar el dinero solicitado al usuario
                    print(f"Retire su dinero: ${monto}")
                else:
                    print("El monto a retirar es mayor que el saldo disponible en la tarjeta.")
            else:
                print("El saldo de la tarjeta es menor que $10,000.")
        else:
            print("La clave ingresada no coincide con la clave asociada a la tarjeta.")
    else:
        print("El número de tarjeta ingresado no se encuentra.")


#Llamar funciones
if __name__ == '__main__':
    print(hello())
    cards_list()
    entrance()
    valid_card()
    process()