# manejo_registros.py

def agregar_registro(registros, nombre, cantidad, fecha):
    """
    Agrega un nuevo registro a la lista de registros.
    
    Args:
        registros (list): Lista de registros.
        nombre (str): Nombre del registro.
        cantidad (float): Cantidad asociada al registro.
        fecha (str): Fecha del registro.
        
    Returns:
        list: Lista de registros actualizada.
    """
    registro = {
        'nombre': nombre,
        'cantidad': cantidad,
        'fecha': fecha
    }
    registros.append(registro)
    return registros

def mostrar_registros(registros):
    """
    Muestra todos los registros en la lista.
    
    Args:
        registros (list): Lista de registros.
        
    Returns:
        None
    """
    for registro in registros:
        print(f"Nombre: {registro['nombre']}, Cantidad: {registro['cantidad']}, Fecha: {registro['fecha']}")

def calcular_balance(registros):
    """
    Calcula el balance total de todos los registros.
    
    Args:
        registros (list): Lista de registros.
        
    Returns:
        float: Balance total.
    """
    balance_total = sum(registro['cantidad'] for registro in registros)
    return balance_total

