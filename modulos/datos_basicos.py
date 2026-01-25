def pedir_nombre():
    name = input("Ingrese su nombre: ")
    return name

def pedir_edad():
    #Creamos un while para manejar errores de ingreso edad
    while True:
        try:
            age = int(input("Ingrese su edad: "))
            if age > 0:
                return age
            else:
                print("La edad debe ser mayor a 0")
        
        except:
            print("Debe ingresar un dato valido")

def pedir_tipo_usuario():
    while True:
        try:
            user_type = int(input("""
[1] Invitado
[2] Usuario
[3] Admin
                      
Seleccione la opción: 
"""))
            match user_type:
                case 1:
                    user_type = "Invitado"
                case 2:
                    user_type = "Usuario"
                case 3:
                    user_type = "Admin"
                case _:
                    print("Elija una opción valida")
                    continue

            return user_type
        except:
            print("La opción es 1,2 o 3")
            continue

def registrar_usuario(user):
    user = {
        "name": user[0],
        "age": user[1],
        "user_type": user[2]
    }

    return user