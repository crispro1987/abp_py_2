def contar_usuarios(users):
    if users == []:
        return 0
    else:
        return 1 + contar_usuarios(users[1:])
    
def error_msg():
    print("========= [XXX] =========")

def mostrar_usuario(user):
    print(f"""
[RUT] : {user.get('rut')}
[NOMBRE] : {user.get('name') or 'NN'}
[MAIL] : {user.get('mail')}
[TELÉFONO] : {user.get('phone') or 'Sin teléfono'}
[ROL] : {user.get('rol')}
""")