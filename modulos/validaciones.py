def categoria_edad(age):
    if age < 0:
        return "Edad invalida"
    elif age < 18:
        return "Menor de edad"
    elif age <= 60:
        return "Adulto"
    else:
        return "Adulto mayor"
    
def login(user_type):
    user = user_type.lower()
    if user == "invitado":
        return "acceso limitado"
    elif user == "usuario":
        return "acceso medio"
    elif user == "admin":
        return "acceso ilimitado"
    else:
        return "acceso denegado"