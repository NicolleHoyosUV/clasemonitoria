#Excepciones

#prevención
while(True):
    try:
        num = int(input('Ingrese un numero: '))
        print(num)
        break
    except ValueError:
        print('No se permite una letra')
    except ZeroDivisionError:
        print('No se permite divider por cero')

#Ejemplo con calcuar un salario
def calcular_salario(numero):
    return numero *-1

if __name__ == '__main__':
    #salario = 1_000_000
    while(True):
        try:
            salario = int(input('Ingrese su salario: '))
            salario_nuevo = calcular_salario(salario)
            if salario_nuevo < 0:
                raise Exception
            else:
                print('Salario nuevo: ', salario_nuevo)
                break
        except ValueError:
            print('solo puede ingresar un numero. ')
        except: 
            print('El salario no es negativo: ', salario_nuevo)
    
    