from modulos.datos_basicos import (pedir_nombre,pedir_edad,pedir_tipo_usuario,registrar_usuario)
from modulos.validaciones import (categoria_edad,login)

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