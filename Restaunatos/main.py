
#Proyecto 2 Algoritmos
print("Bienvenido a nuestra aplicacion RESTAUNATOS\n")
menu = input("Que desea hacer?\n\n"
             "1. Comer Ya!\n"
             "2. Iniciar Sesion\n"
             "3. Restaurante del dia\n"
             "4. Salir\n\n")
menu = str(menu)
while (menu!="4"):
    if menu =="1":
         a = input("Su restaurante sirve solo un tipo de comida?/n"
                   "1. Si\n"
                   "2. Quiza\n"
                   "3. No se\n"
                   "4. Casi no\n"
                   "5. No\n\n")
    if menu =="2":
        b = input("1. Iniciar Sesion\n"
                  "2. Registrarse\n\n")
        b = str(b)
        if b=="1":
            usuario = input("Ingrese Usuario: ")
            contrasena = input("Ingrese contrasena: ")
            usuario =str(usuario)
            contrasena = str(contrasena)
        if b=="2":
            usuarion = input("Ingrese Usuario: ")
            contrasena1 = input("Ingrese contrasena: ")
            contrasena2 = input("Ingrese contrasena nuevamente: ")
            usuarion =str(usuarion)
            contrasena1 = str(contrasena1)
            contrasena1 = str(contrasena1)
    if menu =="3":
        print("RESTAUNATOS te recomienta: \n")
print("Buen provecho!!!!")
        
    
