import pandas as pd
import logging

# Configuración de registro utilizando la biblioteca logging para un mejor control y manejo de los mensajes.
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Diccionario con las claves y valores dados en el ejercicio 2.1
data = {"product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"], "quantity": [3,10,0,5]}

# Creción del DataFrame utilizando la biblioteca Pandas
_PRODUCT_DF = pd.DataFrame(data)

def is_product_available(product_name: str, quantity: int):
    """Verifica si existe stock.

    Args:
        product_name (str): Nombre del producto a consultar stock
        quantity (int): Cantidad del producto a consultar stock

    Returns:
        bool: Devuelve un True si existe stock del producto y cantidad consultado.
              Devuelve False si no existe stock, se produce una excepción o el usuario cancela el proceso.
    """
    global _PRODUCT_DF
    try:
        # Utilizando 'loc' se filtran las filas del DF donde el nombre del producto coincide
        # con el argumento 'product_name' proporcionado.
        product_row = _PRODUCT_DF.loc[_PRODUCT_DF['product_name'] == product_name]
        if product_row.empty:
            logger.info(f"No se encontró el producto {product_name}.")
            return False
        
        # Accede al valor de stock 'quantity' para el producto seleccionado 'product_row'.
        product_stock = product_row['quantity'].values[0]

        # A través de un bucle if se compara la cantidad de stock que hay del producto seleccionado 'product_stock' 
        # con la cantidad 'quantity' ingresada en la función.
        if product_stock >= quantity:
            return True
        else:
            logger.info(f"No hay suficiente stock de {product_name}. Stock disponible: {product_stock}")
            return False
    
    except KeyboardInterrupt:
        logger.error("Proceso de pedido cancelado.")
        return False

    except Exception as e:
        logger.error(f"Error: {str(e)}.")
        return False
    
# En la función is_product_available() se maneja la lógica de verificación de stock dentro
# del bloque try-except. Si el producto no se encuentra en el DataFrame _PRODUCT_DF se
# muestra un mensaje informativo y la función devuelve False, y si no hay suficiente stock
# se muestra un mensaje informativo y la función devuelve False.
# Esto resuelve el potencial bucle infinito que se menciona en el ejercicio 2.2.