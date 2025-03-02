# UDI Tracker

Una herramienta de línea de comandos para consultar el valor de las Unidades de Inversión (UDIs) y realizar conversiones de UDIs a pesos mexicanos utilizando la API oficial provista por el Banco de México (SIE API).

## Descripción

Este proyecto proporciona dos utilidades:

1. `get_udi.py` - Consulta el valor de la UDI para una fecha específica o para la fecha actual.
2. `udi2pesos.py` - Convierte un monto en UDIs a pesos mexicanos basado en el valor de la UDI en una fecha específica o en la fecha actual.


## Requisitos

- Python 3.6 o superior

## Instalación

```bash
# Clonar el repositorio (si aplica)
git clone https://github.com/aamayam/udi_tracker.git
cd udi_tracker
```

## Uso

### Consultar el valor de la UDI

```bash
# Consultar el valor de la UDI en la fecha actual
python get_udi.py

# Consultar el valor de la UDI en una fecha específica
python get_udi.py -f 2023-04-15
# o
python get_udi.py --fecha 2023-04-15
```

### Convertir UDIs a pesos

```bash
# Convertir un monto en UDIs a pesos usando el valor de la UDI actual
python udi2pesos.py 100

# Convertir un monto en UDIs a pesos usando el valor de la UDI en una fecha específica
python udi2pesos.py 100 -f 2023-04-15
# o
python udi2pesos.py 100 --fecha 2023-04-15
```

## Ejemplos

```bash
# Obtener el valor de la UDI hoy
$ python get_udi.py
El valor de la UDI en la fecha 2023-06-15 es: 7.963123

# Obtener el valor de la UDI en una fecha específica
$ python get_udi.py -f 2022-12-31
El valor de la UDI en la fecha 2022-12-31 es: 7.651165

# Convertir 150 UDIs a pesos con el valor actual
$ python udi2pesos.py 150
El valor de la UDI el dia 2023-06-15 es: 7.963123
El total a pagar por 150.0 UDIs es de: $1194.47

# Convertir 150 UDIs a pesos con el valor en una fecha específica
$ python udi2pesos.py 150 -f 2022-12-31
El valor de la UDI el dia 2022-12-31 es: 7.651165
El total a pagar por 150.0 UDI's es de: $1147.67
```

## Configuración

**BANXICO_TOKEN:** El token de consulta es un requisito necesario para poder utilizar el API de series de tiempo. Consta de 64 caracteres alfanuméricos y debe ser enviado cada vez que se interactúe con los servicios provistos.

Se puede obtener en el siguiente enlace: 
```
https://www.banxico.org.mx/SieAPIRest/service/v1/token
```

Es necesario configurar la variable de entorno ```BANXICO_TOKEN``` en un archivo ```.env``` para que se pueda utilizar el servicio de consulta del Banco de México.

## Troubleshooting 
Revisar que todas las dependencias estén instaladas, de lo contrario, hacer:
```python
pip install [lib-name]
```

para cada dependencia faltante (```os```, ```dotenv```, etc.).

Revisar que el archivo ```.env``` exista y contenga la variable ```BANXICO_TOKEN = '[actual_token]'```.

## Licencia

MIT LICENSE