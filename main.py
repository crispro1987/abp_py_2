from modulos.menu import (menu)
from modulos.gestion_datos import (add_user,list_user,search_user,delete_user,category_user)

# Creación del menú con un While para iterar mientras quiera el usuario continuar
# y usamos if como condicional para las opciones llamando a sus respectivas funciones
while True:
    try:
        menu()
        option = int(input("Ingrese una opcion: "))

        if(option == 1):
            add_user()
            print("""
***
                  
Usuario registrado

***
""")
        elif(option == 2):
            list_user()
        elif(option == 3):
            search_user()
        elif(option == 4):
            delete_user()
        elif(option == 5):
            category_user()
        elif(option == 6):
            print(f"Hasta pronto")
            break
        else:
            print("Opción invalida")
            continue
    except:
        print("Ingresar opción valida")
        continue

