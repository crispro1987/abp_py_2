from modulos.funciones_utiles import (contar_usuarios,error_msg,mostrar_usuario)

users = []

mails = set()

ruts = set()

ROLES = ('Admin', 'Invitado', 'Usuario')

def add_user():
    print("""
====== REGISTRAR USUARIO ======
""")
    while True:
        rut = input("Ingrese rut: ")
        if rut in ruts:
            error_msg()
            print(f"El rut {rut} ya está registrado")
            input("Presiona una tecla para volver a intentar...")
            continue
        else:
            break

    name = input("Ingrese nombre: ")
    age = input("Ingrese edad: ")

    while True:
        mail = input("Ingrese email: ")
        if mail in mails:
            error_msg()
            print(f"El mail {mail} ya está registrado")
            input("Presiona una tecla para volver a intentar...")
            continue
        else:
            break

    phone = input("Ingrese teléfono: ")

    

    print("========= ROL =========")
    while True:
        for i, rol in enumerate(ROLES):
            print(f"[{i+1}] - {rol}")

        try:
            option = int(input("Ingrese ROL: "))

            if option == 1:
                role = ROLES[0]
                break
            elif option == 2:
                role = ROLES[1]
                break
            elif option == 3:
                role = ROLES[2]
                break
            else:
                error_msg()
                print("Ingrese una opción valida")
                error_msg()
                continue
        except:
            error_msg()
            print('Ingrese una opción valida')
            error_msg()
            continue

    user = {
        "rut": rut,
        "name": name,
        "age": age,
        "mail": mail,
        "phone": phone,
        "rol": role
    }

    users.append(user)
    mails.add(mail)
    ruts.add(rut)
    return

def list_user():
    qty = contar_usuarios(users)
    
    print(f"""

===============================
===    LISTA DE USUARIOS    ===
===============================
=== Hay {qty} usuarios          ===
""")
    if not users:
        print("No hay usuarios registrados.")
        print("")
        input("Presiona una tecla para volver al menú...")
        return
    
    total_user = len(users)
    counter = 1

    for user in users:
        if(counter == 1):
            print("===============================================")
        
        mostrar_usuario(user)

        if(counter == total_user):
            print("===============================================")
        counter += 1

    input("Presiona una tecla para volver al menú...")

def search_user():
    option = int(input("""
=======================
[1] Buscar por rut
[2] Buscar por mail
                       
Seleccione una opción: 
"""))
    if option == 1:
        search1 = input("Ingrese rut a buscar: ")
        opt_search = "rut"
    elif option == 2:
        search1 = input("Ingrese mail a buscar: ")
        opt_search = "mail"
    else:
        error_msg()
        print("Opción no valida")
        return
    
    counter = 1
    total_user = len(users)

    for user in users:
        if user.get(opt_search) == search1:
            print("=======[ USUARIO ENCONTRADO ]=======")
            mostrar_usuario(user)
            input("Presiona una tecla para volver al menú...")
            return
        else:
            if(counter >= total_user):
                error_msg()
                print("Usuario no encontrado")
                input("Presiona una tecla para volver al menú...")

        counter += 1

def delete_user():
    mail = input("Ingrese mail de usuario a eliminar: ")

    counter = 1
    total_user = len(users)

    for user in users:
        if user["mail"] == mail:
            name_user = user["name"]
            users.remove(user)
            print("=======[ USUARIO ELIMINADO ]=======")
            print("USUARIO: ",name_user)
            input("Presiona una tecla para volver a intentar...")
            return
        else:
            if(counter >= total_user):
                print("=======[ USUARIO NO EXISTE ]=======")
                input("Presiona una tecla para volver al menú...")

        counter += 1

def category_user():

    category = {}
 
    for user in users:
        age = int(user['age'])

        if age < 18:
            category['menor'] = category.get('menor', 0) + 1
        elif age <= 60:
            category['adulto'] = category.get('adulto', 0) + 1
        else:
            category['adulto_mayor'] = category.get('adulto_mayor', 0) + 1

    
    for key, value in category.items():
        if value > 1:
            ese = 's'
        else:
            ese = ''
        print(f"{key}: {value} usuario{ese}")
        print("------------------------------")