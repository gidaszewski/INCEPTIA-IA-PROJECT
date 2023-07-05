_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021",
"Navidad2x1", "heladoFrozen"]

def validate_discount_code(discount_code: str) -> bool:
    """Verifica si el código de descuento ingresado por el usuario es válido.

    Args:
        discount_code (str): Código de descuento a verificar ingresado por el usuario.

    Returns:
        bool: Devuelve True si el código de descuento ingresado es válido y cumple
              con el criterio de diferencia menor a tres caracteres en al menos uno
              de los casos. Devuelve False en caso contrario.
    """
    global _AVAILABLE_DISCOUNT_CODES
    # Bloque if que verifica si 'discount_code' coincide exactamente con uno
    # de los códigos vigentes. Si es así entonces la función devuelve True.
    if discount_code in _AVAILABLE_DISCOUNT_CODES:
        return True
    
    # Si 'discount_code' no coincide exactamente con ningún código vigente, entonces
    # se recorre cada código vigente de la lista '_AVAILABLE_DISCOUNT_CODES'.
    # Luego dentro de la variable 'differences' se guardan la cantidad de diferencias 
    # que se encuentran entre 'discount_code' y el/los códigos vigentes.
    # Además se aplica el método lower() para convertir a minúsculas tanto el código
    # ingresado por el usuario, como los código vigentes para que la comparación sea
    # insensible a mayúsculas y minúsculas como lo pide el enunciado del ejercicio 3.
    
    for code in _AVAILABLE_DISCOUNT_CODES:
        differences = sum(1 for char in discount_code.lower() if char not in code.lower()) + sum(1 for char in code.lower() if char not in discount_code.lower())
        
        if differences <= 3:
            return True
    
    return False