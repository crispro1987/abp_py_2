def add_user(users):
    print("""
====== REGISTRAR USUARIO ======
""")
    rut = input("Ingrese rut: ")
    name = input("Ingrese nombre: ")
    mail = input("Ingrese email: ")
    phone = input("Ingrese teléfono: ")

    users[rut] = {
        "name": name,
        "mail": mail,
        "phone": phone
    }

    return users

def list_user(users):
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

    for rut, datos in users.items():
        if(counter == 1):
            print("===============================================")
        print(f"""
== Rut: {rut}
== Nombre: {datos.get('name', 'n/a')}
== Mail: {datos.get('mail', 'n/a')}
== Teléfono: {datos.get('phone', 'n/a')}
""")
        if(counter == total_user):
            print("===============================================")
        counter += counter

    input("Presiona una tecla para volver al menú...")

def search_user():
    pass

def delete_user():
    pass
