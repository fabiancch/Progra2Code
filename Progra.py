import sys

##Variables Globales##
Aerolineas =[]
Agencias =[]
AVuelos =[]
Aviones =[]
Clientes =[]
CVuelo =[]
Destinos =[]
Func =[]
Rutas =[]
Trip =[]
Tripulacion =[]
TVuela =[]
Vuelos =[]
k = 0 
#################################Funciones######################################
def comapasa(i,lista):##i = Archivo de texto
    ##Cambia ; a , ##
    abre = open(i,"r+")
    p = open("Pasar.txt","w")
    for linea in abre.readlines():
        for x in linea: ##Susituye el ; con una ,
            if x == ";":
                p.write("*")
            else:
                p.write(x)
        abre.close()
    p.close()
    ##Meter a la lista##
    p = open("Pasar.txt","r")
    for linea in p.readlines():
        if linea[-1] == "\n":
            lista += [[linea[:-1]]] ##Linea menos el ultimo caracter"\n"
        else:
            lista += [[linea]]
    p.close()
    ##Hace un split de la lista en los espacios en blanco
    for i in range(len(lista)):
        lista[i] = lista[i][0].split("*")
#-----------------------------------------------------------------------------#
##Validando que las sublistas tengan la cantidad de elementos necesaria##
def valida(lista,numero):
    e = 0
    for i in range(len(lista)):
        if len(lista[i]) != numero:
            del lista[i]
            print('En', lista[i], "no están los datos completos, por tanto se eliminó")
    
#-----------------------------------------------------------------------------#
##############################################
##Llenado de listas##                        #
comapasa("Aerolineas.txt",Aerolineas)        #
comapasa("Agencias.txt",Agencias)            #
comapasa("Asignación de Vuelos.txt",AVuelos) # 
comapasa("Aviones.txt",Aviones)              #
comapasa("Clientes.txt",Clientes)            #
comapasa("ClientesVuelo.txt",CVuelo)         #
comapasa("Destinos.txt",Destinos)            #
comapasa("Funcionarios.txt",Func)            #
comapasa("Rutas.txt",Rutas)                  #
comapasa("Trip.txt",Trip)                    #  
comapasa("Tripulacion.txt",Tripulacion)      #   
comapasa("TripulaVuela.txt",TVuela)          #
comapasa("Vuelos.txt",Vuelos)                #
##############################################
##Validar listas##########################################################################################################################
print ("Errores en los datos ingresados \n")
                                                                                                                                #Agencias#
valida(Agencias,2)
for i in range(len(Agencias)):
    for j in range(i+1,(len(Agencias))):
        if Agencias[i][0] == Agencias[j][0]:
            print("Hay un error con los Id de las agencias:", Agencias[i][1], "y", Agencias[j][1])
            del Agencias[j]
        if Agencias[i][1] == Agencias[j][1]:
            print("Las agencias", Agencias[i][0], "y", Agencias[j][0], "tienen el mismo nombre")
#----------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                              #Aerolineas#
valida(Aerolineas,3)
#Id de Aerolineas diferente#
for i in range(len(Aerolineas)):
    for j in range(i+1,(len(Aerolineas))):
        if Aerolineas[i][1] == Aerolineas[j][1]:
            print("Hay un error con los id de las Aerolíneas:", Aerolineas[i][2], "y", Aerolineas[j][2])
            del Aerolineas[j]
##Valida Id de agencias que se pide se encuentre en Agencias##
for i in range(len(Aerolineas)):
    f = 0 #Se va a usar para las validaciones
    for j in range(len(Agencias)):
        if Aerolineas[i][0] == Agencias[j][0]:
            break
        else:
            if j == len(Agencias)-1:
                print("El Id de la agencia:", Aerolineas[i][1],"""que se pide en Aerolineas, no se encuentra registrado a
                        ninguna Agencia por lo tanto se eliminara la aerolinea""")
                del Aerolineas[i]
##Valida que el Id que se le da a la Aerolinea no sea el mismo que tiene una Agencia## 
for i in range(len(Aerolineas)):
    for j in range(len(Agencias)):
        if Aerolineas[i][1] == Agencias[j][0]:
            print("El Id que se le dio a la Aerolinea", Aerolineas[i][2], ", es igual al que tiene la agencia", Agencias[j][0], "por lo que se eliminara la aerolinea")
            del Aerolineas[i]        
#---------------------------------------------------------------------------------------------------------------------------------------#        
                                                                                                                                #Aviones#
valida(Aviones,5)
#Combustible a entero#
for i in range(len(Aviones)):
    Aviones[i][3] = int(Aviones[i][3])
##Revisa que el id de agencia que se pide se encuentre en la lista correspondiente
for i in range(len(Aviones)):
    for j in range(len(Agencias)):
        if Aviones[i][0] == Agencias[j][0]:
            break
        else:
            if j == len(Agencias)-1:
                print("El Id de la agencia:", Aviones[i][1],"que se pide en Aviones, no se encuentra registrado a ninguna Agencia, por lo tanto se eliminara el avion")
                del Aviones[i]
##Valida que Se encuentre el id de aerolinea que es pide en aviones
for i in range(len(Aviones)):
    f = 0 #Se va a usar para las validaciones
    for j in range(len(Aerolineas)):
        if Aviones[i][1] == Aerolineas[j][1]:
            break
        else:
            if j == len(Aerolineas)-1:
                print("El Id de la aerolinea:", Aviones[i][1],"que se pide en Aviones, no se encuentra registrado a ninguna Aerolinea, por lo tanto este se eliminara")
                del Aviones[i]
#Matricula de Aviones#
for i in range(len(Aviones)):
    for j in range(i+1,(len(Aviones))):
        if Aviones[i][2] == Aviones[j][2]:
            print("La matricula del avion", Aviones[i][2], "esta repetida por lo que se eliminara la segunda")
            del Aviones[j][2]
##Valida el valor del combustible
for i in range(len(Aviones)):
    if Aviones[i][3] < 0:
        print("El valor que tiene combustible debe ser mayor o igual a 0, por defecto se establecio en 0")
        Aviones[i][3] = 0
##Valida el valor de Status
for i in range(len(Aviones)):
    if Aviones[i][4] != "Aeronavegable" and Aviones[i][4] != "No-Aeronavegable":
        print("El valor de status en el avion de matricula:", Aviones[i][2],"no puede ser diferente de Aeronavegable o No-Aeronavegable, por lo tanto se elimino el avion")
        del Aviones[i]
#------------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                                  #Destinos#
valida(Destinos,3)
#Cantidad de horas en Destinos a enteros#
for i in range(len(Destinos)):
    Destinos[i][2] = int(Destinos[i][2])
#Id de destinos no repetidos#
for i in range(len(Destinos)):
    for j in range(i+1,(len(Destinos))):
        if Destinos[i][0] == Destinos[j][0]:
            print("El id del destino :", Destinos[i][1], "esta repetido por lo que se eliminara la segunda aparicion")
            del Destinos[j]
#------------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                                     #Rutas#
valida(Rutas,7)
#Horas de vuelo a entero#
for i in range(len(Rutas)):
    Rutas[i][6] = int(Rutas[i][6])
##Id Rutas no repetido##
for i in range(len(Rutas)):
    for j in range(i+1,(len(Rutas))):
        if Rutas[i][3] == Rutas[j][3]:
            print("Se eliminara la segunda aparicion de:", Rutas[j])
            del Rutas[j]
##Id agencia se encuentre en la lista respectiva##
for i in range(len(Rutas)):
    for j in range(len(Agencias)):
        if Rutas[i][0] == Agencias[j][0]:
            break
        else:
            if j == len(Agencias)-1:
                print("El Id de la agencia:", Rutas[i], "que se pide en Rutas, no se encuentra registrado a ninguna Agencia, por lo que se eliminara la Ruta")
                del Rutas[i]
##Valida que Se encuentre el id de aerolinea que es pide en Rutas
for i in range(len(Rutas)):
    for j in range(len(Aerolineas)):
        if Rutas[i][1] == Aerolineas[j][1]:
            break
        else:
            if j == len(Aerolineas)-1:
                print("El Id de la aerolinea:", Rutas[i][1],"que se pide en Rutas, no se encuentra registrado a ninguna Aerolinea, por lo que se eliminara la Ruta")
                del Rutas[i]
##Validar que se encuentre la matricula del avion que se pide##
for i in range(len(Rutas)):
    for j in range(len(Aviones)):
        if Rutas[i][3] == Aviones[j][2]:
            break
        else:
            if j == len(Aviones)-1:
                print("La matricula", Rutas[i][3], "que se pide en Rutas, no la tiene ningun avion, por lo que se eliminara la Ruta")
                del Rutas[i]
##Validar que se encuentre el Id de los destinos que se requieren##
for i in range(len(Rutas)):
    for j in range(len(Destinos)):
        if Rutas[i][4] == Destinos[j][0]:
            break
        else:
            if j == len(Destinos)-1:
                print("El id del destino de salida", Rutas[i][4], "Que se pide en rutas no se encuentra registrado a ningun destino, por lo que se eliminara la ruta")
                del Rutas[i]
##Validar que nos Id de llegada se encuentren##
for i in range(len(Rutas)):
    for j in range(len(Destinos)):
        if Rutas[i][5] == Destinos[j][0]:
            break
        else:
            if j == len(Destinos)-1:
                print("El Id del destino de llegada", Rutas[i][5], 'que se pide en rutas no se encuentra registrado a ningun destino, por lo que se eliminara la ruta')
                del Rutas[i]
##Validar destino de origen y llegada en destinos##
for i in range(len(Rutas)):
    if Rutas[i][4] == Rutas[i][5]:
        print("El destino de salida y llegada deben ser distintos en", Rutas[i], " por tal razon se eliminara la ruta")
        del Rutas[i]
#Valida que horas sea positivo#
for i in range(len(Rutas)):
    if Rutas[i][6] < 0:
        print("La cantidad de horas debe ser positiva para", Rutas[i], "como esta no lo es entonces se eliminara la ruta")
        del Rutas[i]
#------------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                                  #Clientes#
valida(Clientes,2)
for i in range(len(Clientes)):
    for j in range(i+1,(len(Clientes))):
        if Clientes[i][0] == Clientes[j][0]:
            print("La segunda aparicion del la cedula: ", Clientes[i][1],"Ha sido eliminado de la lista de clientes")
            del Clientes[i]
#------------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                              #Funcionarios#
valida(Func,3)
##Valida que los id de los funcionarios no se repitan##
for i in range(len(Func)):
    for j in range(i+1,(len(Func))):
        if Func[i][0] == Func[j][0]:
            print("La segunda aparicion del siguiente funcionario fue eliminada", Func[i][1])
            del Func[j]
##Valida el rango del funcionario##
for i in range(len(Func)):
    if Func[i][2] in ["CAP","CO","JC","BCA","F-F"]:
        break
    else:
        print("El rango del funcionario", Func[i][2], "no corresponde a los estipulados, por lo que se elimino")
        del Func[i]
#------------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                                      #Trip#
valida(Trip,2)
##Valida el Id de trip no se repita##
for i in range(len(Trip)):
    for j in range(i+1,(len(Trip))):
        if Trip[i][0] == Trip[j][0]:
            print("Hubo un error con el id de :", Trip[i],"por lo que se eliminara la segunda repeticion")
            del Trip[i]
#------------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                                    #Vuelos#
valida(Vuelos,6)
#Capacidad y Libres a enteros#
for i in range(len(Vuelos)):
    Vuelos[i][3] = int(Vuelos[i][3])
    Vuelos[i][4] = int(Vuelos[i][4])
##Id agencia se encuentre en la lista respectiva##
for i in range(len(Vuelos)):
    for j in range(len(Agencias)):
        if Vuelos[i][0] == Agencias[j][0]:
            break
        else:
            if j == len(Agencias)-1:
                print("El Id de la agencia:", Vuelos[i][0],"que se pide en Rutas, no se encuentra registrado a ninguna Agencia, por lo que se eliminara el vuelo")
                del Vuelos[i]
##Valida que Se encuentre el id de aerolinea que es pide en Rutas
for i in range(len(Vuelos)):
    for j in range(len(Aerolineas)):
        if Vuelos[i][1] == Aerolineas[j][1]:
            break
        else:
            if j == len(Aerolineas)-1:
                print("El Id de la aerolinea:", Vuelos[i][1],"que se pide en Rutas, no se encuentra registrado a ninguna Aerolinea, por lo que se eliminara el vuelo")
                del Vuelos[i]
##Validar que se encuentre la matricula del avion que se pide##
for i in range(len(Vuelos)):
    for j in range(len(Aviones)):
        if Vuelos[i][2] == Aviones[j][2]:
            break
        else:
            if j == len(Aviones)-1:
                print("La matricula", Vuelos[i][3], "que se pide en Vuelos, no la tiene ningun avion, por lo que se eliminara el vuelo")
                del Vuelos[i]
##Capacidad y libres##
for i in range(len(Vuelos)):
    if Vuelos[i][3] < 0 or Vuelos[i][4] < 0:
        print("Los espacios libres y la capacidad en", Vuelos[i], "Tiene que ser mayor o igual a 0, como es diferente de estos valores se eliminara el vuelo")
        del Vuelos[i]
    if Vuelos[i][3] < Vuelos[i][4]:
        print("Los espacios libres no pueden ser mayores a la capacidad en", Vuelos[i],"Razon por la que se eliminara el vuelo")
        del Vuelos[i]
##Conexion si o no##
for i in range(len(Vuelos)):
    if Vuelos[i][5] in ["SI","NO"]:
        break
    else:
        print("La conexion de un vuelo debe ser SI ó NO, en", Vuelos[i], "no se cumple, por lo que se eliminara el vuelo")
        del Vuelos[i]
#------------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                      #Asignacion de Vuelos#
valida(AVuelos,5)
##Validar que se encuentre la matricula del avion que se pide##
for i in range(len(AVuelos)):
    for j in range(len(Aviones)):
        if AVuelos[i][0] == Aviones[j][2]:
            break
        else:
            if j == len(Aviones)-1:
                print("La matricula", AVuelos[i][0], "que se pide en asignacion de vuelos, no la tiene ningun avion, por lo que se eliminara esta asignacion")
                del AVuelos[i]
##Id agencia se encuentre en la lista respectiva##
for i in range(len(AVuelos)):
    for j in range(len(Agencias)):
        if AVuelos[i][1] == Agencias[j][0]:
            break
        else:
            if j == len(Agencias)-1:
                print("El Id de la agencia:", AVuelos[i][1],"que se pide en asignacion de vuelos, no se encuentra registrado a ninguna Agencia, por lo que se eliminara esta asignacion")
                del AVuelos[i]
##Valida que Se encuentre el id de aerolinea 
for i in range(len(AVuelos)):
    for j in range(len(Aerolineas)):
        if Vuelos[i][2] == Aerolineas[j][1]:
            break
        else:
            if j == len(Aerolineas)-1:
                print("El Id de la aerolinea:", AVuelos[i][2],"que se pide en Asignacion de Vuelos, no se encuentra registrado a ninguna Aerolinea, por lo que se eliminara esta asignacion")
                del AVuelos[i]
##Validar que se encuentre el Id de los destinos DE SALIDA que se requieren##
for i in range(len(AVuelos)):
    for j in range(len(Destinos)):
        if AVuelos[i][3] == Destinos[j][0]:
            break
        else:
            if j == len(Destinos)-1:
                print("El id del destino de salida", AVuelos[i][3], "Que se pide en asignacion de vuelos no se encuentra registrado a ningun destino, por lo que se eliminara esta asignacion")
                del AVuelos[i]
##Validar que nos Id DE LLEGADA se encuentren##
for i in range(len(AVuelos)):
    for j in range(len(Destinos)):
        if AVuelos[i][4] == Destinos[j][0]:
            break
        else:
            if j == len(Destinos)-1:
                print("El Id del destino de llegada", Avuelos[i][4], 'que se pide en asignacion de vuelos no se encuentra registrado a ningun destino, por lo que se eliminara esta asignacion')
                del AVuelos[i]
##Validar destino de origen y llegada distintos##
for i in range(len(AVuelos)):
    if Vuelos[i][3] == AVuelos[i][4]:
        print("El destino de salida y llegada deben ser distintos en", AVuelos[i], ", por lo que se eliminara esta asignacion")
        del AVuelos[i]
#------------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                               #Tripulacion#
valida(Tripulacion,3)
##Valida que Se encuentre el id de aerolinea 
for i in range(len(Tripulacion)):
    for j in range(len(Aerolineas)):
        if Tripulacion[i][0] == Aerolineas[j][1]:
            break
        else:
            if j == len(Aerolineas)-1:
                print("El Id de la aerolinea:", Tripulacion[i][0],"que se pide en Tripulacion, no se encuentra registrado a ninguna Aerolinea, por lo que se eliminara :", Tripulacion[i])
                del Tripulacion[i]
##Valida que el Id de trip exista##
for i in range(len(Tripulacion)):
    for j in range(len(Trip)):
        if Tripulacion[i][1] == Trip[j][0]:
            break
        else:
            if j == len(Trip)-1:
                print("El id :", Tripulacion[i][1], "no existe por lo que se eliminara a de la lista")
                del Tripulacion[i]
##Valida que el nombre se encuentre en la lista de funcionarios##
for i in range(len(Tripulacion)):
    for j in range(len(Func)):
        if Tripulacion[i][2] == Func[j][1]:
            break
        else:
            if j == len(Func)-1:
                print("El nombre del", Tripulacion[i][2], "no es un funcionario por lo que se eliminara de la lista")
                del Tripulacion[i]
#------------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                                    #CVuelo#
valida(CVuelo,2)
##Valida que las matriculas de los aviones sean correctas##
for i in range(len(CVuelo)):
    for j in range(len(Aviones)):
        if CVuelo[i][0] == Aviones[j][2]:
            break
        else:
            if j == len(Aviones)-1:
                print("La matricula", CVuelo[i][0], "que se pide en ClientesVuelo, no se encuentra registrada, por lo que se eliminaran los clientes y la matricula")
                del CVuelo[i]
##Valida que los id de cliente sean verdaderos##
for i in range(len(CVuelo)):
    for j in range(len(Clientes)):
        if CVuelo[i][1] == Clientes[j][0]:
            break
        else:
            if j == len(Clientes) - 1:
                print("El Id del cliente",CVuelo[i][1],"no esta registrado a ningun cliente por lo que se eliminara el cliente")
                del CVuelo[i][1]
#------------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                                    #TVuela#
valida(TVuela,2)
##Valida que las matriculas de los aviones sean correctas##
for i in range(len(TVuela)):
    for j in range(len(Aviones)):
        if TVuela[i][0] == Aviones[j][2]:
            break
        else:
            if j == len(Aviones)-1:
                print("La matricula de avion que se pide en", TVuela[i], "no se encuentra registrada, por lo que se eliminara de la lista")
                del TVuela[i]
##Id trip exista en una lista##
for i in range(len(TVuela)):
    for j in range(len(Trip)):
        if TVuela[i][1] == Trip[j][0]:
            break
        else:
            if j == len(Trip)-1:
                print("El Id de trip que se pide en",TVuela[i],"No esta registrado en Trip, por lo que se eliminara de la lista")
                del TVuela[i]
#------------------------------------------------------------------------------------------------------------------------------------------#
                                                     ##Validaciones Complejas##
#------------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                                    #Vuelos#
for i in range(len(Vuelos)):
    for j in range(i+1,len(Vuelos)):
        if Vuelos[i][:4] == Vuelos[j][:4]:
            print("Hay un problema con los primeros tres elementos en la lista de vuelos \n especificamente en las sublistas",Vuelos[i], "y", Vuelos[j])
            print("Se eliminara la segunda aparicion de estos")
            del Vuelos[j]
#------------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                                   #AVuelos#
for i in range(len(AVuelos)):
    for j in range(i+1,len(AVuelos)):
        if AVuelos[i][:4] == AVuelos[j][:4]:
            print("Hay un problema con los primeros tres elementos en la lista de asignacion de vuelos \n especificamente en las sublistas",AVuelos[i], "y", AVuelos[j])
            print("Se eliminara la segunda aparicion de estos")
            del AVuelos[j]
#------------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                               #Tripulacion#
for i in range(len(Tripulacion)):
    for j in range(i+1,len(Tripulacion)):
        if Tripulacion[i][:3] == Tripulacion[j][:3]:
            print("Hay un problema con los primeros dos elementos en la lista de tripulacion \n especificamente en las sublistas",Tripulacion[i], "y", Tripulacion[j])
            print("Se eliminara la segunda aparicion de estos")
            del Tripulacion[j]
##############################################################################################################################################
##############################################################################################################################################
###################################################"""Poniendo las listas dentro de otras"""##################################################
##############################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------#Rutas en aviones##
for i in range(len(Aviones)):
    temp = []
    for j in range(len(Rutas)):
        if Aviones[i][2] == Rutas[j][2]:
            temp += [Rutas[j][3:]]
    Aviones[i] += temp
#-------------------------------------------------------------------------------------------------------------------#Aviones en Aerolineas##
for i in range(len(Aerolineas)):
    temp = []
    for j in range(len(Aviones)):
        if Aerolineas[i][1] == Aviones[j][1]:
            temp += Aviones[j][2:]
    Aerolineas[i] += temp
#------------------------------------------------------------------------------------------------------------------#Aerolineas in Agencias##
for i in range(len(Agencias)):
    temp = []
    for j in range(len(Aerolineas)):
        if Agencias[i][0] == Aerolineas[j][0]:
            temp += Aerolineas[j][1:]
    Agencias[i] += temp
############################################################################################################################################
#-----------------------------------------------------------------------------------------------------------------------#TVuela en AVuelos##
for i in range(len(AVuelos)):
    temp = []
    for j in range(len(TVuela)):
        if AVuelos [i][0] == TVuela[j][0]:
            temp += TVuela[j][1]
    AVuelos[i] += temp
#-----------------------------------------------------------------------------------------------------------------------#CVuelo en AVuelos##
for i in range(len(AVuelos)):
    temp = []
    for j in range(len(CVuelo)):
        if AVuelos [i][0] == CVuelo[j][0]:
            temp += CVuelo[j][1]
    AVuelos[i] += temp
############################################################################################################################################
#########################################################"""Interfaz de usuario"""##########################################################
############################################################################################################################################

#-----------------------------------------------------------------------------------------------------------------Funciones del funcionario#
def pprincipal():
    choice = input("Digite el numero que corresponde a la acción que desea hacer:""\n"
                  "1. Eliminar Información""\n"
                  "2. Visualizar Información""\n"
                  "3. Asignar vuelos""\n"
                  "4. Cambiar status de un Avion""\n"
                  "5. Manejar la tripulación de un vuelo""\n"
                  "6. Asignar un Avión a una Ruta""\n"
                  "7. Vender tiquetes""\n"
                  "8. Cierra el programa""\n")
    if choice not in ["1","2","3","4","5","6","7","8"]:
        print("El numero que ingresó no se encuentra entre los que se solicitó")
        pprincipal()
        
    elif choice == '1':
        pag1()
        
    elif choice == '2':
        pag2()

    elif choice == '3':
        pag3()

    elif choice == '4':
        pag4()

    elif choice == '5':
        pag5()

    elif choice == '6':
        pag6()

    elif choice == '7':
        pag7()

    elif choice == '8':
        sis.exit()
#---------------------------------------------------------------------------------------------------------------Funciones del funcionario 1#
def pag1():
    jojo = 0
    ch1 = 0
    while jojo == 0:
        ch1 = input("Digite el numero que corresponde a la acción que desea hacer: \n"
                    "1. Eliminar aviones" "\n"
                    "2. Eliminar rutas" "\n"
                    "3. Eliminar vuelos""\n"
                    "4. Eliminar Clientes""\n"
                    "5. Eliminar Asignaciones de vuelos""\n"
                    "6. Volver a la pagina principal""\n"
                    "7. Cerrar programa" "\n")
        if ch1 not in ["1","2","3","4","5","6","7"]:
            print("El numero que ingresó no se encuentra entre los que se solicitó")
        else:
            jojo = 1
#---------------------------------------------------------------------------------------------------------------#
    if ch1 == '1':
        #Elimina avion#
        ea = input("Digite la matricula del avion que desea eliminar: ")
        yn = 0
        #busca#
        for i in range(len(Agencias)): #Cada agencia
            for j in range(len(Agencias[i][2])):
                for k in range(len(Agencias[i][2][j][2])):
                    if ea == Agencias[i][2][j][2][k][0]:
                        del Agencias[i][2][j][2][k]
                        yn = 1
                        break
        if yn != 0:
            print("El avion de matricula", ea, "fué eliminado con éxito")
            print("Además se eliminaron las rutas que estaban inscritas junto con este")
            pag1()
        else:
            print("La matricula", ea, "no está inscrita")
            pag1()
#---------------------------------------------------------------------------------------------------------------#
    elif ch1 == "2":
        #Elimina Rutas#
        er == input("Digite el Id de ruta que desea eliminar: ")
        yn = 0
        for i in range(len(Agencias)):
            for j in range(len(Agencias[i][2])):
                for k in range(len(Agencias[i][2][j][2])):
                    for e in range(len(Agencias[i][2][j][2][k][3])):
                        if er == Agencias[i][2][j][2][k][3][e][0]:
                            del Agencias[i][2][j][2][k][3][e]
                            yn = 1
                            break
        if yn != 0:
            print("La ruta ", er, "fue eliminada con exito""\n")
        else:
            print("El id de ruta ingresado no está registrado""\n")
            pag1()
#---------------------------------------------------------------------------------------------------------------#
    elif ch1 == "3":
        k = 1
        el = 0
        while k != 0:
            print("Actualmente existen los siguentes Vuelos")
            c = 0
            for i in range(len(Vuelos)):
                print(c, Vuelos[i], "\n")
                c += 1
            el = int(input("Inserte el numero del vuelo que desea eliminar y presione enter: "))
            if el > c or el < 0:
                print("Este numero no corresponde a los que se le presentaron""\n")
            else:
                k = 0
                del Vuelos[el-1]
                print("Su Vuelo se elimino con exito""\n")
                pag1()         
#---------------------------------------------------------------------------------------------------------------#           
    elif ch1 == "4":
        yn = 0
        elc = input("Introduzca el Id del cliente que desea eliminar: ")
        for i in range(len(Clientes)):
            if Clientes[i][0] == elc:
                del Clientes[i]
                yn = 1
                break
        if yn != 0:
            print("El Id del cliente que ingreso no corresponde a ninguno registrado")
        else:
            print("El cliente con id", elc,"fue eliminado con exito""\n")
            pag1()
#---------------------------------------------------------------------------------------------------------------#
    elif ch1 == "5":
        k = 1
        el = 0
        while k != 0:
            print("Actualmente existen las siguentes asignaciones de vuelos")
            c = 0
            for i in range(len(AVuelos)):
                print(c, AVuelos[i], "\n")
                c += 1
            el = int(input("Inserte el numero del vuelo que desea eliminar y presione enter: "))
            if el > c or el < 0:
                print("Este numero no corresponde a los que se le presentaron""\n")
            else:
                k = 0
                del AVuelos[el-1]
                print("Su Asignacion de vuelo se elimino con exito""\n")

    elif ch1 == "6":
        pprincipal()

    elif ch1 == "7":
        sys.exit()

#---------------------------------------------------------------------------------------------------------------Funciones del funcionario 2#
def pag2(): #Visualizar info#
    jojo = 0
    ch1 = 0
    while jojo == 0:
        ch1 = input("Digite el numero que corresponde a la acción que desea hacer: \n"
                    "1. Ver aviones" "\n"
                    "2. Ver informacion de vuelos: rutas, aviones por ruta y horas de vuelo" "\n"
                    "3. Ver agencias, aerolineas, aviones y rutas""\n"
                    "4. Ver destinos""\n"
                    "5. Ver tripulacion""\n"
                    "6. Ver Clientes por vuelo""\n"
                    "7. Volver a la pagina principal""\n"
                    "8. Cerrar programa" "\n")
        if ch1 not in ["1","2","3","4","5","6","7","8"]:
            print("El numero que ingresó no se encuentra entre los que se solicitó")
        else:
            jojo = 1
#---------------------------------------------------------------------------------------------------------------#
    if ch1 == "1":
        for i in range(len(Agencias)):
            for j in range(len(Agencias[i][2])):
                for k in range(len(Agencias[i][2][j][2])):
                    print(Agencias[i][2][j][2][k], "\n")
        ch2 = 0
        jojo = 0
        while jojo != 0:
            ch2 = input("Digite" "\n" "1 para volver " "\n" " 2 para regresar a la pagina principal""\n""Luego presione enter: ")
            if ch2 == "1" or ch2 == "2":
                jojo = 1
            else:
                print("Vuelva a digitar su numero""\n")
        if ch2 == "1":
            pag2()
        else:
            pag1()
#---------------------------------------------------------------------------------------------------------------#
    elif ch1 == "2":
        for i in range(len(Agencias)):
            for j in range(len(Agencias[i][2])):
                for k in range(len(Agencias[i][2][j][2])):
                    for e in range(len(Agencias[i][2][j][2][k][3])):
                        print(Agencias[i][2][j][2][k][3][e], "\n")
        ch2 = 0
        jojo = 0
        while jojo != 0:
            ch2 = input("Digite" "\n" "1 para volver " "\n" " 2 para regresar a la pagina principal""\n""Luego presione enter: ")
            if ch2 == "1" or ch2 == "2":
                jojo = 1
            else:
                print("Vuelva a digitar su numero""\n")
        if ch2 == "1":
            pag2()
        else:
            pag1()

#---------------------------------------------------------------------------------------------------------------#
    elif ch1 == "3":
        for i in range(len(Agencias)):
            print(Agencias[i])
        ch2 = 0
        jojo = 0
        while jojo != 0:
            ch2 = input("Digite" "\n" "1 para volver " "\n" " 2 para regresar a la pagina principal""\n""Luego presione enter: ")
            if ch2 == "1" or ch2 == "2":
                jojo = 1
            else:
                print("Vuelva a digitar su numero")
        if ch2 == "1":
            pag2()
        else:
            pag1()
#---------------------------------------------------------------------------------------------------------------#
    elif ch1 == "4":
        for i in range(len(Destinos)):
            print(Destinos[i], "\n")
        ch2 = 0
        jojo = 0
        while jojo != 0:
            ch2 = input("Digite" "\n" "1 para volver " "\n" " 2 para regresar a la pagina principal""\n""Luego presione enter: ")
            if ch2 == "1" or ch2 == "2":
                jojo = 1
            else:
                print("Vuelva a digitar su numero")
        if ch2 == "1":
            pag2()
        else:
            pag1()
#---------------------------------------------------------------------------------------------------------------#
    elif ch1 == "5":
        print("Los miembros de las tripulaciones son:")
        for i in range(len(Tripulacion)):
            print(Tripulacion[i], "\n")
        ch2 = 0
        jojo = 0
        while jojo != 0:
            ch2 = input("Digite" "\n" "1 para volver " "\n" " 2 para regresar a la pagina principal""\n""Luego presione enter: ")
            if ch2 == "1" or ch2 == "2":
                jojo = 1
            else:
                print("Vuelva a digitar su numero")
        if ch2 == "1":
            pag2()
        else:
            pag1()
#---------------------------------------------------------------------------------------------------------------#
    elif ch1 == "6":
        for i in range(len(AVuelos)):
            print("Para el vuelo ", AVuelos[i], "Estan registrados")
            for j in range(len(AVuelos[i][6])):
                print(AVuelos[i][6][j], "\n")
        ch2 = 0
        jojo = 0
        while jojo != 0:
            ch2 = input("Digite" "\n" "1 para volver " "\n" " 2 para regresar a la pagina principal""\n""Luego presione enter: ")
            if ch2 == "1" or ch2 == "2":
                jojo = 1
            else:
                print("Vuelva a digitar su numero")
        if ch2 == "1":
            pag2()
        else:
            pag1()
#---------------------------------------------------------------------------------------------------------------#
    elif ch1 == "7":
        pprincipal()

    elif ch1 == "8":
        sys.exit()
#---------------------------------------------------------------------------------------------------------------Funciones del funcionario 3#
def pag3(): #Asignar Vuelos#
    nuevo = []
    jojo = 0
    n = 0
    while jojo != 1:
        n = input("Digite la matricula del avion y presione enter: ")
        for i in range(len(Agencias)): #Cada agencia
            for j in range(len(Agencias[i][2])):
                for k in range(len(Agencias[i][2][j][2])):
                    if n == Agencias[i][2][j][2][k][0]:
                        jojo = 1
                    if Agencias[i][2][j][2][k][2] == "No-Aeronavegable":
                        jojo = 2
                    if Agencias[i][2][j][2][k][1] < 0:
                        jojo = 3
        if jojo == 0:
            print("Esta matricula no se encuentra registrada a ningun avion""\n")
        elif jojo == 2:
            print("Este avion no es Aeronavegable en este momento""\n")
        elif jojo == 3:
            print("Este avion se encuentra sin combustible""\n")
    nuevo += [n]
    #Id agencia#
    jojo = 0
    while jojo== 0:
        n = input("Digite la Identificacion de la agencia y presione enter: ")
        for i in range(len(Agencias)): #Cada agencia
            if Agencias[i][0] == n:
                jojo = 1
        if jojo == 0:
            print("Esta Identificacion no corresponde a ninguna agencia")
    nuevo += [n]
    #Id Aerolinea#
    jojo = 0
    while jojo== 0:
        n = input("Digite la Identificacion de la aerolinea y presione enter: ")
        for i in range(len(Agencias)):
            for j in range(len(Agencias[i][2])):
                if n == Agencias[i][2][j]:
                    jojo = 1
        if jojo == 0:
            print("Esta Identificacion no corresponde a ninguna aerolinea")
    nuevo += [n]
    #Id Origen#
    jojo = 0
    while jojo== 0:
        n = input("Digite la Identificacion del origen y presione enter: ")
        for i in range(len(Destinos)): 
            if Destinos[i][0] == n:
                jojo = 1
        if jojo == 0:
            print("Esta Identificacion no corresponde a ninguna destino")
    nuevo += [n]
    #Id LLegada#
    jojo = 0
    while jojo== 0:
        n = input("Digite la Identificacion de la llegada y presione enter: ")
        for i in range(len(Destinos)): 
            if Destinos[i][0] == n:
                jojo = 1
        if jojo == 0:
            print("Esta Identificacion no corresponde a ninguna destino")
    nuevo += [n]
    #TVuela#
    jojo = 0
    while jojo== 0:
        n = input("Digite la Identificacion de la Tripulacion y presione enter: ")
        for i in range(len(Trip)): 
            if Trip[i][0] == n:
                jojo = 1
        if jojo == 0:
            print("Esta Identificacion no corresponde a ninguna destino""\n")
    nuevo += [n]
    #CVuelo#
    n = input("Cuantos clientes quiere ingresar? Digite su respuesta y presione enter: ")
    nps = []
    while n > 0:
        jojo = 0
        while jojo == 0:
            np = input("Digite el primer Id de pasajero""\n")
            for i in range(len(Clientes)):
                if Clientes[i][0] == np:
                    jojo = 1
                    nps += [np]
                    print("El usuario ha sido añadido a la lista")
            if jojo == 0:
                print("Este id de cliente no se encuentra registrado")
    nuevo += [np]
    AVuelos += [nuevo]
    
    ch2 = 0
    jojo = 0
    while jojo != 0:
        ch2 = input("Digite" "\n" "1 para volver " "\n" " 2 para regresar a la pagina principal""\n""Luego presione enter: ")
        if ch2 == "1" or ch2 == "2":
            jojo = 1
        else:
            print("Vuelva a digitar su numero")
    if ch2 == "1":
        pag3()
    else:
        pag1()
#---------------------------------------------------------------------------------------------------------------Funciones del funcionario 4#
def pag4(): #Cambiar estatus de un avion#
    jojo = 0
    while jojo == 0:
        stat = input("Digite la matricula del avion al que le quere cambiar el status: ")
        for i in range(len(Agencias)): #Cada agencia
            for j in range(len(Agencias[i][2])):
                for k in range(len(Agencias[i][2][j][2])):
                    if n == Agencias[i][2][j][2][k][0]:
                        jojo = 1
                        print("El avion actualmente esta en estado ", Agencias[i][2][j][2][k][2])
                        if Agencias[i][2][j][2][k][2] == "No-Aeronavegable":
                            Agencias[i][2][j][2][k][2] =  "Aeronavegable"
                        else:
                            Agencias[i][2][j][2][k][2] = "No-Aeronavegable"
                        print("El estado del avion ha sido cambiado a ", Agencias[i][2][j][2][k][2])                    
        if jojo == 0:
            print("El avion de la matricula mencionada no existe")
    ch2 = 0
    jojo = 0
    while jojo != 0:
        ch2 = input("Digite" "\n" "1 para volver " "\n" " 2 para regresar a la pagina principal""\n""Luego presione enter: ")
        if ch2 == "1" or ch2 == "2":
            jojo = 1
        else:
            print("Vuelva a digitar su numero")
    if ch2 == "1":
        pag4()
    else:
        pag1()
#---------------------------------------------------------------------------------------------------------------Funciones del funcionario 5#
def pag5(): #Manejar la tripulacion #
    ch1 = 0
    jojo = 0
    while jojo == 0:
        ch1 = int(input("Inserte \n 1. Para agregar un miembro a una tripulacion \n 2. Para eliminar un miembro de la misma"))
        if ch1 != 1 and ch1 != 2:
            print("El valor ingresado debe ser uno o dos")
        else:
            jojo = 1
            nuevo = []
    if ch1 == 1:
        while jojo == 1:
            ch2 = input("Digite el Id de la aerolinea a la que se va a unir: ")
            for i in range(len(Agencias)):
                for j in range(len(Agencias[i][2])):
                    if Agencias[i][2][j][0] == ch2:
                        jojo = 0
                        nuevo += [Agencias[i][2][j][0]]
            if jojo == 1:
                print("Este id no pertenece a ninguna aerolinea")
        while jojo == 0:
            ch2 = input("Digite el Id de trip en el que se añadirá: ")
            for i in range(len(Trip)):
                if Trip[i][0] == ch2:
                    jojo = 1
                    nuevo += [Trip[i][0]]
            if jojo == 0:
                print("Este id no pertenece a ningun Trip")
        while jojo == 1:
            ch2 = input("Digite el nombre del funcionario que desea agregar: ")
            for i in range(len(Func)):
                if Func[i][1] == ch2:
                    jojo = 0
                    nuevo += [Func[i][1]]
            if jojo == 1:
                print("Este nombre no pertenece a ningun funcionario")
        Func += [nuevo]
    else:
        while jojo == 1:
            print("Los actuales miembros de la tripulacion son: ")
            m = 0
            for i in range(len(Tripulacion)):
                print(m, "=",Tripulacion[i], '\n')
                m += 1
            m = int(input("Escriba el numero que corresponde al miembro que desea eliminar: "))
            if m < 0 and m > (len(Tripulacion)):
                print("El numero ingresado no es correcto")
            else:
                jojo = 0
                del Tripulacion[i]
                print("El miembro fue eliminado con exito")
    ch2 = 0
    jojo = 0
    while jojo != 0:
        ch2 = input("Digite" "\n" "1 para volver " "\n" " 2 para regresar a la pagina principal""\n""Luego presione enter: ")
        if ch2 == "1" or ch2 == "2":
            jojo = 1
        else:
            print("Vuelva a digitar su numero")
    if ch2 == "1":
        pag5()
    else:
        pag1()
#---------------------------------------------------------------------------------------------------------------Funciones del funcionario 6#
def pag6():
    jojo = 0
    avr = 0
    while jojo == 0:
        avr = input("Introduzca el avion y presione enter: ")
        for i in range(len(Agencias)): #Cada agencia
            for j in range(len(Agencias[i][2])):
                for k in range(len(Agencias[i][2][j][2])):
                    if avr == Agencias[i][2][j][2][k][0]:
                        jojo = 1
                        avr = Agencias[i][2][j][2][k][1] ##Combustible
                    if Agencias[i][2][j][2][k][2] == "No-Aeronavegable":
                        jojo = 2
                    if Agencias[i][2][j][2][k][1] < 0:
                        jojo = 3
        if jojo == 0:
            print("Esta matricula no se encuentra registrada a ningun avion")
        elif jojo == 2:
            print("Este avion no es Aeronavegable en este momento")
        elif jojo == 3:
            print("Este avion se encuentra sin combustible")
    rut = 0
    while jojo == 1:
        rut = input("Digite el id de la ruta que va a asignar al avion: ")
        for i in range(len(Agencias)):
            for j in range(len(Agencias[i][2])):
                for k in range(len(Agencias[i][2][j][2])):
                    for e in range(len(Agencias[i][2][j][2][k][3])):
                        if rut == Agencias[i][2][j][2][k][3][e][0]:
                            jojo = 0
                            rut = Agencias[i][2][j][2][k][3][e][3] ##Horas
        if jojo == 1:
            print("Este Id no corresponde a niguna ruta")
    if avr < rut:
        print("Este avion no se puede asignar")
    else:
        print("El avion ha sido asignado correctamente")
    ch2 = 0
    jojo = 0
    while jojo != 0:
        ch2 = input("Digite" "\n" "1 para volver " "\n" " 2 para regresar a la pagina principal""\n""Luego presione enter: ")
        if ch2 == "1" or ch2 == "2":
            jojo = 1
        else:
            print("Vuelva a digitar su numero")
    if ch2 == "1":
        pag6()
    else:
        pag1()
#---------------------------------------------------------------------------------------------------------------Funciones del funcionario 7#
def pag7():#venta de tiquetes#
    print("Los tiquetes que hay disponibles son los siguentes")
    ch1 = 0
    for i in range(len(Vuelos)):
        if Vuelos[i][4] > 0:
            print(ch1,Vuelos[i], "\n")
        ch1 += 1
    jojo = 0
    while jojo == 0:
        ch1 = int(input("Introduzca el numero de vuelo en el que desea reservar"))
        if ch1>0 and ch1<(len(Vuelos)):
            jojo = 1
        else:
            print("Debe insertar uno de los numeros que coresponden a Vuelos")
    num = 0
    while jojo == 1:
        num = int(input("Intriduzca el numero de boletos a comprar"))
        if num > Vuelos[ch1][4]:
            print("Este vuelo no cuenta con esa cantidad de espacios disponibles")
            pag7()
        else:
            Vuelos[ch1][4] = Vuelos[ch1][4] - num
    ch2 = 0
    jojo = 0
    while jojo != 0:
        ch2 = input("Digite" "\n" "1 para volver " "\n" " 2 para regresar a la pagina principal""\n""Luego presione enter: ")
        if ch2 == "1" or ch2 == "2":
            jojo = 1
        else:
            print("Vuelva a digitar su numero")
    if ch2 == "1":
        pag7()
    else:
        pag1()
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#######################################################Funciones Usuario Principal###########################################################
def fpricipal():
    choice = input("Digite el numero que corresponde a la acción que desea hacer:""\n"
                  "1. Visualizar vuelos disponiles""\n"
                  "2. Comprar boletos para un vuelo""\n"
                  "3. Cierra el programa""\n")
    if choice not in ["1","2","3"]:
        print("El numero que ingresó no se encuentra entre los que se solicitó")
        fprincipal()
        
    elif choice == '1':
        pusu1()
        
    elif choice == '2':
        pusu2()

    elif choice == '3':
        sis.exit()
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------Funciones del usuario 1#
def pusu1():
    for i in range(len(Vuelos)):
        if Vuelos[i][4] >= 1:
            print("En el vuelo de la agencia", Vuelos[i][0], "aerolinea ", Vuelos[i][1],"en el avion ", Vuelos[i][2], "quedan", Vuelos[i][4], "campos libres")
    ch2 = 0
    jojo = 0
    while jojo != 0:
        ch2 = input("Digite" "\n" "1 para volver " "\n" " 2 para salir del programa""\n""Luego presione enter: ")
        if ch2 == "1" or ch2 == "2":
            jojo = 1
        else:
            print("Vuelva a digitar su numero")
    if ch2 == "1":
        fprincipal()
    else:
        sys.exit()
#---------------------------------------------------------------------------------------------------------------Funciones del usuario 2#
def pusu2():
    av = 0       
    jojo = 0
    while jojo == 0:
        av = input("Digite la matricula del avion en el que desea volar y presione enter: ")
        for i in range(len(Vuelos)):
            if Vuelos[i][2] == av:
                i = av
                jojo = 1
            else:
                print("Matricula Incorrecta \n") 
    jojo = 0      
    while jojo == 0:
        ch1 = int(input("Digite la cantidad de boletos que desea comprar y presione enter: "))
        if ch1 > Vuelos[av][4]:
            print("Esta cantidad de boletos no la puede comprar")
        else:
            jojo = 1
            Vuelos[av][4] -= ch1
            k = input("Digite su ID y presione enter: ")
            AVuelos[i][6] += k

    print("Felicidades")

    ch2 = 0
    jojo = 0
    while jojo != 0:
        ch2 = input("Digite" "\n" "1 para volver " "\n" " 2 para salir del programa""\n""Luego presione enter: ")
        if ch2 == "1" or ch2 == "2":
            jojo = 1
        else:
            print("Vuelva a digitar su numero")
    if ch2 == "1":
        fprincipal()
    else:
        sys.exit()
#----------------------------------------------------------------------------------------------------------------------------------------------#
####################################################################################################################################################
print("Reportes")
print("Agencias")
for i in range(len(Agencias)):
    print(Agencias[i][0:2])
print("Aerolineas por agencia")
for i in range(len(Agencias)):
    print(Agencias[i][1:3])
print("Asignacion")
for i in range(len(AVuelos)):
    print(AVuelos[i])
print("Puestos de funcionarios")
for i in range(len(Func)):
    print(Func[i])
####################################################################################################################################################
p = 0
while p != 'f' and p != 'c':
    k = input("Digite su Identificación y presione enter: ")
    for i in range(len(Func)):
        if Func[i][0] == k:
            pprincipal()
            p = 'f'
    for i in range(len(Clientes)):
        if Clientes[i][0] == k:
            p = 'c'
            
    if p != 'f' and p != 'c':
        print("La identificación ingresada no está registrada")
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------#

