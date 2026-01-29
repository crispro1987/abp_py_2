# Procedimiento para validar edad
def categoria_edad(age):
    if age < 0:
        return "Edad invalida"
    elif age < 18:
        return "Menor de edad"
    elif age <= 60:
        return "Adulto"
    else:
        return "Adulto mayor"