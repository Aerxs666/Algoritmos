
#login

loginuser = input("Ponga su nombre de usuario que desea crear: ")
loginpassword = input("Introduzca su password con el que va crear la cuenta: ")
print("Su cuenta se ha creado correctamente, inicie sesion:")


login = input("Introduzca su usuario: ")
if login == loginuser:
    passwordlogin = input("Ahora introduzca su password: ")
    if passwordlogin == loginpassword:
        print(f"Ha iniciado sesión correctamente {loginuser}")
        

        while True:
            print("\nMenu:")
            print("1. Cambiar usuario")
            print("2. Cambiar contraseña")
            print("3. Salir")
            menu = input("Seleccione una opción: ")

            if menu == "1":
                loginuser = input("Introduzca su nuevo nombre de usuario: ")
                print("Su usuario ha cambiado a:", loginuser)
            elif menu == "2":
                loginpassword = input("Introduzca su nueva contraseña: ")
                print("Su contraseña ha cambiado a:", loginpassword)
            elif menu == "3":
                print("Sesión finalizada. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario no encontrado, introduzca el usuario con el que creó la cuenta")