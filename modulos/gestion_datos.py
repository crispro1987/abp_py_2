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
            print("========= [XXX] =========")
            print(f"El rut {rut} ya está registrado")
            input("Presiona una tecla para volver a intentar...")
            continue
        else:
            break

    name = input("Ingrese nombre: ")
    
    while True:
        mail = input("Ingrese email: ")
        if mail in mails:
            print("========= [XXX] =========")
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
                print("========= [XXX] =========")
                print("Ingrese una opción valida")
                print("========= [XXX] =========")
                continue
        except:
            print("========= [XXX] =========")
            print('Ingrese una opción valida')
            print("========= [XXX] =========")
            continue

    user = {
        "rut": rut,
        "name": name,
        "mail": mail,
        "phone": phone,
        "rol": role
    }

    users.append(user)
    mails.add(mail)
    ruts.add(rut)
    return

def list_user():
    print("""

===============================
===    LISTA DE USUARIOS    ===
===============================
          
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
        print(f"""
== Rut: {user["rut"]}
== Nombre: {user.get('name','NN')}
== Mail: {user['mail']}
== Teléfono: {user.get('phone','Sin teléfono')}
== ROL: {user['rol']}
""")
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
        print("========= [XXX] =========")
        print("Opción no valida")
        return
    
    for user in users:
        if user.get(opt_search) == search1:
            print("=======[ USUARIO ENCONTRADO ]=======")
            print(f"""
[RUT] : {user.get('rut')}
[NOMBRE] : {user.get('name','NN')}
[MAIL] : {user.get('mail')}
[TELÉFONO] : {user.get('phone','Sin teléfono')}
[ROL] : {user.get('rol')}
""")
            input("Presiona una tecla para volver al menú...")
            return
        else:
            print("========= [XXX] =========")
            print("Usuario no encontrado")
    

def delete_user():
    pass
