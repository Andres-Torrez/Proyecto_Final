from logger import log_error, log_warning

# ===========================
# VALIDAR TEXTO
# ===========================

def validar_texto(texto):
    """
    Valida que el texto sea un string no vacio.
    """
    if not isinstance(texto, str):
        log_error("texto invalido: no es string.")
        return False
    
    texto.strip()
    if texto == "":
        log_warning("Intento de ingresar texto vacio.")
        return False
    return True

# ===========================
# VALIDAR TEXTO
# ===========================

def validar_inidce(lista, indice):
    """
    Valida que el indice sea:
    -un numero entero
    -no negativo
    -dentro del rango ded la lista
    """

    if not isinstance(indice, int):
        log_error("indice invalido: no es entero.")
        return False
    
    if indice < 0:
        log_warning(f"Indice negativo detectado: {indice}.")
        return False
    
    if indice >= len(lista):
        log_warning(
            f"Indice fuera de rango: {indice}."
            f"Maximo permitido: {len(lista) - 1}"
        )

        return False
    
    return True