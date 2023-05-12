# La importación de time es para usar la función time.sleep() donde le asigno un segundo entre respuesta a la terminal para que no sea tan rápido toda la carga. Se puede obviar todos los time.sleep(1) de las funciones.
import time

# Defino una variable login para que se ejecute cuando sea True, pero como todavia no se cargo al usuario correcto el login es False.

login = False

# Defino la funcion acces que es la que va a determinar si el login es True o False. Como necesito traer la variable login que tengo fuera de la funcion uso la palabra reservada global para hacer referencia que no es solo una variable de la funcion sino que es global a todo el codigo y a otras funciones. 
# la funcion usa un contador que parte de desde 0 para contar los 'intentos' que tiene el usuario de acceder, por eso mientras el while sea menor o igual a 3 pida por input acceder a un usuario y clave. Una vez que lo pida el contador pasa a sumar 1, y esto se va a repetir hasta mientras no salga (va a salir cuando el login sea True).
# Definimos que si user es admin y clave 1234, el login pase a ser True, se imprima el mensaje Ingresos Exitoso y salga del bucle (break). Cuando llegue a tres va a imprimir usuario y contraseña incorrecta y va a salir.
#Al final de la función le pedimos que regrese el valor login (True o False de acuerdo a lo que ingresemos)

def acces():
    global login
    contador = 0
    while contador <= 3:
        user = input("Ingrese usuario: ")
        password = input("Ingrese contraseña: ")
        contador += 1
        if user == 'admin' and password == '1234':
            login = True
            print("Ingreso exitoso")
            break
        else:
            print("Usuario y/o contraseña incorrecta")
        if contador == 3:
            print('Cuenta bloqueada')
            break
    return login

# La función see_menues() lo que hace es imprimir el menu del cajero y pide ingresar una opción, guardada en una variable que se retorna.

def see_menues():
    print('''
    CAJERO AUTOMATICO

ISPC

Listado de opciones:

1)      Ingreso de dinero

2)      Extracción de dinero

3)      Consulta de saldo

4)      Salir"''')
    time.sleep(1)
    option = input('\n Ingrese su opción: ')
    return option

# La funcion options es la más compleja ya que tiene todo lo que pasa cuando elegimos cada una de ellas. Para esa función partimos del saldo inicial ya que si no lo definimos no tendríamos ningun importe para las sumas o restas por las depositos o extracciones (necesitamos definir una variable). Option None o cualquier valor distinto a 4 porque solo vamos a salir de las opciones si elegimos la opcion 4 (que es salir), es importante definir esa opción antes de comenzar el bucle porque va a pasar como el login inicial (se necesita un valor que cumpla con la condicion del bucle porque si no definimos va a salir error en la función ya que no option no está definido). Al poner el options = see_menues() le estamos diciendo que la variable sea el valor de la función (que esa funcion eran el numero ingresado de las opciones). Acá las variables option y options no son iguales y son funciones propias de cada uno, no hay relación. Cada opción suma, resta o dice cuanto es el saldo. En el caso de las extracciones hay otro if adentro por si quiere sacar $5.000 más de lo que tiene en la cuenta.

def options():
    balance = 10000
    options = None
    while options != '4':
        time.sleep(1)
        options = see_menues()
        if options == '1':
            time.sleep(1)
            deposit = int(input('Usted ingresó la opción 1 ¿Cuanto dinero desea depositar?: '))
            balance += deposit
            print( 'Su nuevo saldo es:', balance)
            call_back()
        elif options == '2':
            time.sleep(1)
            extract = int(input('Usted ingresó la opción 2 ¿Cuanto dinero desea extraer?: '))
            if extract > balance:
                limit = balance + 5000
                print("El monto a retirar es mayor al saldo actual. Sin embargo, tiene hasta $5.000,00 en descubierto. El limite maximo disponible en esta extraccion es de: ", limit)
                opt1 = input("¿Desea Continuar? 1. SI 2. NO ")
                if opt1 == '1':
                    time.sleep(1)
                    extract = int(input("Ingrese el monto a extraer: "))
                    if extract <= limit:
                        balance -= extract
                        print( 'Su nuevo saldo es:', balance)
                    else: 
                        print("Lo ingresado es mayor a lo disponible")
                elif opt1 == '2':
                    time.sleep(1)   
                    call_back()
                else:
                    time.sleep(1)
                    print("Lo ingresado no es válida")
                    call_back()
            else:
                balance -= extract
                print('Su nuevo saldo es:', balance)
            call_back()
        elif options == '3':
            time.sleep(1)
            extract = print('Usted ingresó la opción 3. El saldo de la cuenta es: ', balance)
            call_back()
        elif options == '4':
            time.sleep(1)
            print("Muchas gracias por utlizar nuestros servicios")
        else:
            time.sleep(1)
            print('Opcion no valida')
            call_back()

# La función call_back() es solo un mensaje cuando vuelve al menú.

def call_back():
    time.sleep(1)
    print('''
        Volviendo al menú de Inicio
        ''')
    

#Y acá está todo. Ejecuto la función acces() y le digo si login = True ejecutá la función de las opciones (y esa trae todas las otras), y una vez que arranca no sale del bucle hasta que se seleccione la opción 4.

acces()
if login == True:
    options()
