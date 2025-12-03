import json
import shutil
from logger import log_error, log_info, log_warning

def guardar_notas(notas,ruta):
    """
    Guarda la lista de notas en un archivo JSON.
    
    Args:
        notas (list): Lista de notas a guardar.
        ruta (str): Ruta de archivo donde se guardaran las notas.
    
    Returns:
        bool: True  si se guardo correctamente, False si hubo un error
    """

    try: 
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(notas, f, ensure_ascii=False, indent=4)
        
        log_info(f"Notas guardadas en '{ruta}'.")
        return True
    
    except Exception as e:
        log_error(f"Error al guardar notas: {e}")
        return False
  
  

def cargar_notas(ruta):
    """
    Cargar las notas desde un archivo JSON.
    
    Arg:
       ruta (str): Ruta del archivo a cargar.
    
    Returns:
       list: Lissta de notas, o lista vacia si ocurre error."""
    try:
        with open(ruta, "r", encoding="utf_8") as f:
            return json.load(f)
        
        log_info(f"Notas cargadas desde '{ruta}'.")
        return notas
    
    except FileNotFoundError:
        log_warning(f"El archivo '{ruta}' no existe. Se creara automticamente.")
        return []
    
    except json.JSONDecodeError:
        log_error(f"Archivo '{ruta}' corrupto. Nose pudo leer JSON.")
        return []
    
    except Exception as e:
        log_error(f"Error inesperado al cargar notas: {e}")
        return []
    
def crear_backup(ruta):
    """
    Crea un resplado .bak del archivo de notas.
    
    Args:
        ruta(str): Ruta del archivo original.
        
    Return:
        bool: True si el backup fue creado, False si hubi error.
    """
    try:
        backp_ruta = ruta + ".bak"
        shutil.copy(ruta, backp_ruta)

        log_info(f"Backup_creado en '{backp_ruta}'.")
        return True
    except Exception as e:
        log_warning(f"No se pudo cerar backup de '{ruta}' : {e}")
        return False
    
# def autoguardar(notas, ruta="notas.json"):
#     """
#     Guarda las notas y crea un backup automaticamente.
    
#     Args:
#         notas (list) : Lista de notas.
#         ruta (str): Ruta del archivo principal.
    
#     Returns:
#         None
#     """

#     if guardar_notas(notas, ruta):
#         crear_backup(ruta)
#         log_info("Auto-guardado completado.")
#     else:
#         log_error("El auto-guardado fallo.")