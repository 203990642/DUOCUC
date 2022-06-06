flagreg = False
Flag = True
lista_pacientes = [] 
lista_ruts = []
lista_direcciones = []
lista_correos = []
lista_edades = []
lista_sexo = []
#ESTO SIGNIFICA QUE TENDRIA UN MAXIMO DE 300 PACIENTES, NO SE ME OCURRIO OTRA FORMA
lista_registros = [None for _ in range(300)]
lista_ps = []
cantidad_pac = 0
while Flag:
    print("          Centro Medico")
    print("1.  Registrar Paciente")
    print("2.  Atención Paciente")
    print("3.  Consultar Datos Paciente")
    print("4.  Salir")
    menures = int(input())

    if menures == 1:
        
        paciente=input("Ingrese nombre\n")
        lista_pacientes.append(paciente)

        flag2 = True
        while flag2:
            rut=int(input("Ingrese rut\n"))
            if rut > 4999999 and rut < 100000000:
                lista_ruts.append(rut)
                flag2 = False
            else: 
                print("Ingrese un rut válido")

        direccion=input("Ingrese direccion\n")
        lista_direcciones.append(direccion)

        correo=input("Ingrese correo\n")
        lista_correos.append(correo)

        flag2 = True
        while flag2:
            edad=int(input("Ingrese edad\n"))
            if edad > 0 and edad < 111:
                lista_edades.append(edad)
                flag2 = False
            else: 
                print("Ingrese una edad entre 0 a 110 años")
    
        flag2 = True
        while flag2:
            sexo=input("Ingrese sexo (m ó f )\n").lower()
            if sexo == "m" or sexo == "f":
                lista_sexo.append(sexo)
                flag2 = False
            else: 
                print("Ingrese un caracter valido")

        flag2 = True
        while flag2:
            ps=input("Ingrese PS (ISAPRE ó FONASA)\n").lower()
            if ps == "isapre" or ps == "fonasa":
                lista_ps.append(ps)
                flag2 = False
            else: 
                print("Ingrese una opcion valida")
        
        cantidad_pac = cantidad_pac + 1

    if menures == 2:
        flagaa = True
        while flagaa:
            res=int(input("Ingrese rut"))
            if res in lista_ruts:
                indice = lista_ruts.index(res)
                registro = input("Ingrese Fecha y observacion de visita")
                lista_registros[indice] = registro
                flagaa = False
            else:
                print("Ingrese un rut válido")
        
    if menures == 3:
        flagaa = True
        while flagaa:
            res=int(input("Ingrese rut"))
            if res in lista_ruts:
                flagaa = False
                indice = lista_ruts.index(res)
                if lista_registros[indice] != None:
                    print("Nombre : ",lista_pacientes[indice])
                    print("Rut : ", lista_ruts[indice])
                    print("Direccion : ", lista_direcciones[indice])
                    print("Correo : ", lista_correos[indice])
                    print("Edad : ", lista_edades[indice])
                    print("Sexo : ",lista_sexo[indice])
                    print("Registros : ",lista_registros[indice])
                    print("PS : ",lista_ps[indice])

                else:
                    print("Nombre : ",lista_pacientes[indice])
                    print("Rut : ", lista_ruts[indice])
                    print("Direccion : ", lista_direcciones[indice])
                    print("Correo : ", lista_correos[indice])
                    print("Edad : ", lista_edades[indice])
                    print("Sexo : ",lista_sexo[indice])
                    print("Registros : No hay registros")
                    print("PS : ",lista_ps[indice])
            else:  
                print("Ingrese rut válido")
    if menures == 4:
        print("Salir del sistema")
        Flag = False
