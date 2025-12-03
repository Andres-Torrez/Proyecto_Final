from datetime import datetime
from logger import log_error, log_info, log_warning
from validadores import validar_indice,  validar_texto


# ===========================
# CREACIÓN DE NOTAS
# ===========================


def crear_nota(texto, etiqueta):
    """
    Crea una nota con texto, etiqueta y fecha.

    Args:
        texto (str): Contenido de la nota.
        etiqueta (str) : Categoria o etiqueta de la nota.

    Returns:
    dict | None : Diccionario con la nota creada o None si falla la validacion
    """
    
    if not validar_texto(texto):
        print("❌Error: La nota no puede estar vacia.")
        return None

    etiqueta = etiqueta.strip().lower() or "general"
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    return {
        "texto":texto,
        "etiqueta":etiqueta,
        "fecha": fecha
    }

# ===========================
# CRUD DE NOTAS
# ===========================


#CODIGO COMENTADO
# def agregar_nota(notas, texto, etiqueta):
#     """
#     Agrega una nuva nota a la lista.
    
#     Args:
#         notas (list): Lista actual de notas.
#         texto (str): Texto de la nota.
#         etiqueta (str): Etiqueta de la nota
        
#     Returns:
#         bool:  True si la nota fue agregada , False en caso contrario"""
#     nota =  crear_nota(texto,etiqueta)

#     if nota is None:
#         return False
    
#     notas.append(nota)
#     log_info("Nota agregada correctamente")
#     return True

def editar_nota(notas, indice, nuevo_texto, nueva_etiqueta):
    """
    Edita una nota existente cambiando texo y/o etiqueta.
    
    Args:
        notas(list): Lista de notas.
        inidice (int): Posicion de la nota a editar.
        nuevo_texto (str): texto actualizado.
        nueva_etiqueta (str): Etqueta actualiaza"""
    if not validar_indice(notas, indice):
        return False
    
    if not validar_texto(nuevo_texto):
        print("El texto no puede estar vacio.")
        return False
    
    notas[indice]["texto"] = nuevo_texto.strip()

    if nueva_etiqueta.strip():
        notas[indice]["etiqueta"] = nueva_etiqueta.strip().lower()

    log_info(f"Nota editada en posicion {indice}: {nuevo_texto} [{nueva_etiqueta}]")
    print("Nota editada correctamente")


    return True


# ===========================
# MOSTRAR NOTAS
# ===========================


def mostrar_notas(notas):
    """
    Mustra todas las notas almacenadas.
    
    Args:
    notas (list): Lista de notas
    """
    if not notas:
        print("No hay notas.")
        log_warning("Intento de mostrar notas vacias.")
        return
    
    log_info(f"Mostrando {len(notas)} notas.")

    for i, n in enumerate(notas, start=1):
        print(f"{i}. [{n['etiqueta']} | {n['fecha']}] {n['texto']}")

def mostrar_resultados(resultados):
    """
    Filtrar notas por etiqueta exacta.
    
    Args:
         notas(list): Lista de notas.
         etiqueta (str): Etiqueta a filtrar.
        
    Returns:
         list: Lista de notas con esa etiqueta"""
    if not resultados:
        log_warning("Intento de mostrar resultado, pero la lsiata esta vacia.")
        return
    
    for i, n in enumerate(resultados, start=1):
        print(f"{i}. [{n['etiqueta']} | {n['fecha']}] {n['texto']}")


# ===========================
# BÚSQUEDA Y FILTROS
# ===========================


def buscar_notas(notas, texto):
    """
    Busca notas cuyo texto contenga una cedena dada.
    
    Args:
        notas (list): Lista de notas.
        texto (str): Texto para buscar
    
    Returns:
        list: Lista de notas que coinciden con la busqueda.
    """
    texto = texto.strip().lower()

    if not validar_texto(texto):
        print("Busqueda vacia.")
        return[]
    
    resultados = [ n for n in notas if texto in n["texto"].lower()]

    log_info(f"Busqueda '{texto}' ->  {len(resultados)} resultados")
    
    if not resultados:
        print("No se encontraron notas.")
    
    return resultados


def filtrar_por_etiqueta(notas, etiqueta):
    """
    Filtra notas por etiqueta exacta.
    
    Args:
        notas (list): Lista de notas.
        etiqueta(str): Etiqueta a filtrar.
    
    Returns:
        list: Lista de notas con esa etiqueta.
    """
    etiqueta = etiqueta.strip().lower()

    resultados = [n for n in notas if n["etiqueta"] == etiqueta]

    log_info(f"Filtro por etiqueta '{etiqueta}' -> {len(resultados)} resultados.")


    if not resultados:
        print("No hay notas con esa etiqueta.")
    
    return resultados

    
def filtrar_por_fecha(notas, fecha_parcial):
    """
    Filtrar notas cuyo campo de fecha empieza con la cedena dad(ej: 2025- 12
    
    Args:
         notas (list): Lista de notas.
         fecha_parcial (str): Cadena para filtrar por fecha.
         
    Returns:
        list: Lista de notas con fechas coninciente')"""
    fecha_parcial = fecha_parcial.strip()

    resultado = [n for n in notas if n["fecha"].startswith(fecha_parcial)]

    log_info(f"Filtro por fecha '{fecha_parcial}' -> {len(resultado)} resultados")

    if not resultado:
        print("No se encontraron notas en esa fecha.")
    
    return resultado
