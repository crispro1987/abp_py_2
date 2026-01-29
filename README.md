# Sistema Usuario Python | Proyecto Módulo #3 | ABP

Sistema de registro de usuarios desarrollado en __Python__. implementando estructuras de control, diferentes tipos de funciones y tipos de datos.

este sistema esta modularizado para la reutilización de tareas repetitivas haciendo el código más legible y limpio

## Tecnologías utilizadas

- Python 3.14
- Github

## Estructura del proyecto

```
abp3/
│
├── modulos/
│   ├── __init_.py
│   ├── funciones_utiles.py
│   ├── gestion_datos.py
│   ├── menu.py
|   └── validaciones.py
├── main.py
└── README.md
```

## Funcionamiento de sistema

### Tipos de datos

#### Tupla

Tupla con roles de usuario
```
ROLES = ('Admin', 'Invitado', 'Usuario') 
```

#### Lista

Lista que recibe los diccionarios con los datos del usuario

```
users = []
```

#### Diccionario y diccionario anidado 

Se utiliza un diccionario para agregar un usuario a lista users y este contiene un diccionario anidado data que contiene datos extra.

```
user = {
    "rut": rut,
    "name": name,
    "age": age,
    "mail": mail,
    "phone": phone,
    "rol": role,
    "data": {
        "is_adult": catgry,
        "verified": False
    }
}

users.append(user)
```

#### Set

Implementación de Set para no permitir duplicidad de datos como mail o rut y sean unicos.


```
mails = set()

ruts = set()

....

mails.add(mail)
ruts.add(rut)
```


### Menú Principal

El menú lo iteramos con un __while__. Hasta que el usuario decida salir


```
======================
===      MENU      ===
======================
          
[1] Agregar usuario
[2] Listar usuarios
[3] Buscar usuarios
[4] Eliminar usuario
[5] Categorías de usuarios
[6] Salir
```

### Condicional de opciones

Para las opciones del menu usamos como condicional __if__ para enviarnos a las funciones de cada item del menu. usamos __try__ y __except__ para capturar el error

```
try:
    menu()
    option = int(input("Ingrese una opcion: "))

    if(option == 1):
        add_user()
        print("***Usuario registrado***")
    elif(option == 2):
        list_user()
    elif(option == 3):
        search_user()
    elif(option == 4):
        delete_user()
    elif(option == 5):
        category_user()
    elif(option == 6):
        print("Hasta pronto")
        break
    else:
        print("Opción invalida")
        continue
except:
    print("Ingresar opción valida")
    continue
```

### Función recursiva

Creación de una función recursiva para contar usuarios que trae en el __argumento__ users. En el sistema lo utilizamos para saber cuantos usuarios estan registrados

```
def contar_usuarios(users):
    if users == []:
        return 0
    else:
        return 1 + contar_usuarios(users[1:])
```

### Procedimiento

Se utiliza un procedimiento para imprimir en pantalla los datos del usuario que trae como argumento. También contiene logica anidada
 
```
def mostrar_usuario(user):
    if user['data']['is_adult']:
        cat = "ADULTO"
    else:
        cat = "MENOR DE EDAD"

    if user['data']['verified']:
        verified = "-SI-"
    else:
        verified = "-NO-"

    print(f"""
[RUT] : {user.get('rut')}
[NOMBRE] : {user.get('name') or 'NN'}
[EDAD] : {user.get('age')}
[CATEGORÍA] : {cat}
[MAIL] : {user.get('mail')}
[TELÉFONO] : {user.get('phone') or 'Sin teléfono'}
[ROL] : {user.get('rol')}
[VERIFICADO] : {verified}
""")
```

