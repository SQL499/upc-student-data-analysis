# scripts/data_cleaning.py

def normalizar_texto(texto):
    """
    Limpia y formatea nombres propios: quita espacios y aplica formato título.
    """
    if isinstance(texto, str):
        return texto.strip().title()
    return ""

def extraer_dominio(correo):
    """
    Extrae el dominio de un correo electrónico. Si no es válido, retorna 'desconocido'.
    """
    if isinstance(correo, str) and "@" in correo:
        return correo.split("@")[1].lower()
    return "desconocido"

def validar_correo(correo):
    """
    Verifica si un correo es válido según un patrón simple.
    """
    import re
    if isinstance(correo, str):
        return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo))
    return False

def validar_telefono(numero):
    """
    Verifica si un número es un celular válido peruano (9 dígitos, empieza con 9).
    """
    if isinstance(numero, str):
        numero = numero.strip()
        return numero.startswith("9") and len(numero) == 9 and numero.isdigit()
    return False

def longitud_texto(texto):
    """
    Devuelve la longitud del texto, o 0 si no es válido.
    """
    if isinstance(texto, str):
        return len(texto.strip())
    return 0
