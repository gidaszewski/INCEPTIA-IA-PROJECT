import requests, logging

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    MAX_TEMP = 28

    # Configuración de registro utilizando la biblioteca logging para un mejor control y manejo de los mensajes.
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Método 1
    @classmethod
    def get_weather_data(cls):
        """Realiza una solicitud para obtener datos del clima en Pehuajo de la API de Open Weather.

        Returns:
            dict or None: Un diccionario con los datos del clima si la solicitud es válida,
                          None si ocurre un error durante la solicitud o extracción de datos del JSON.
        """
        try:
            # Extracción de datos de la API con los atributos de la clase GeoAPI. URL obtenida de la documentación de la API.
            api_response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}')
            # Extraer el contenido JSON
            data = api_response.json()
            return data
    
        except requests.RequestException as e:
            cls.logger.error("Error al realizar la solicitud: %s", e)
            return None
        
        except ValueError as e:
            cls.logger.error('No fue posible convertir los datos recibidos: %s', e)
            return None

    # Método 2
    @classmethod
    def is_hot_in_pehuajo(cls):
        """Verifica si la temperatura en Pehuajo es mayor a la temperatura máxima deseada.
           Dentro del bloque try-except se llama a la función get_weather_data() la cúal
           brinda los datos del clima. Si los datos ingresan éxitosamente entonces
           se realiza la conversión de los datos para luego verificar la temperatura.

        Returns:
            bool: True si la temperatura es mayor, False en caso contrario o si hay errores.
        """
        try:
            data = cls.get_weather_data()
            if data is not None:
                temperatura_actual = data['main']['temp']
                temp_kelvin = float(temperatura_actual)
                # Conversión de grados Kelvin a grados Celsius utilizando la formula: K − 273,15 = °C
                celsius = temp_kelvin - 273.15
                
                # Prueba si la temperatura en Pehuajo es mayor a 28 grados celsius.
                if celsius > cls.MAX_TEMP:
                    return True
    
        except KeyError as e:
            cls.logger.error("Error al extraer los datos: %s", e)
            return None

        except ValueError as e:
            cls.logger.error("Valor incorrecto para convertir a tipo float: %s", e)
            return None
        
        return False