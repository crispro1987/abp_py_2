# Función recursiva para contar usuarios
def contar_usuarios(users):
    if users == []:
        return 0
    else:
        return 1 + contar_usuarios(users[1:])

# Procedimiento para reutilizar este print de error
def error_msg():
    print("========= [XXX] =========")

# Procedimiento para reutilizar mostrar usuario
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