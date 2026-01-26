from modulos.datos_basicos import (pedir_nombre,pedir_edad,pedir_tipo_usuario,registrar_usuario)
from modulos.validaciones import (categoria_edad,login)
from modulos.menu import (menu)
from modulos.gestion_datos import (add_user,list_user,search_user,delete_user)


name = pedir_nombre()
age = pedir_edad()
user_type = pedir_tipo_usuario()

user = name,age,user_type

registrar_usuario(user)

category = categoria_edad(age)
access = login(user_type)

print(f"""
Bienvenido {name} 
--------------------------
Categoría: {category}
Nivel acceso: {access}
""")

users = {}

while True:
    try:
        menu()
        option = int(input("Ingrese una opcion: "))

        if(option == 1):
            new_user = add_user(users)
            users = new_user
            print(users)
            print("""
***
                  
Usuario registrado

***
""")
            continue
        elif(option == 2):
            list_user(users)
            continue
        elif(option == 3):
            search_user()
        elif(option == 4):
            delete_user()
        elif(option == 5):
            print(f"Hasta pronto {name}")
            break
        else:
            print("Opción invalida")
            continue
    except:
        print("Ingresar opción valida")
        continue

