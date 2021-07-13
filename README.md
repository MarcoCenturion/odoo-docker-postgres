# odoo-docker-postgres

Crearemos un repositorio donde guardar la configuracion de un dockerfile y docker-compose para levantar contenedores de docker que corran odoo y postgres

el objetivo es levantar en producción en poco tiempo un backup

## pasos
1- correr systemctl start docker
2- Primer paso, crear el archivo docker-compose.yml
3- guardar el odoo.conf en la ruta del volumen del contenedor
4- persistir los datos en los volúmenes

**Arrancar los contenedores**
Correr esto en el mismo directorio donde está el archivo docker-compose.yml
docker-compose up -u

**Detener los contenedores**
docker-compose down 

**Restart**
docker 

## Restorear la base

Crear un usuario odoo con permisos para postgres en el container  
**odoo-db-data**

## Entrar a la linea de comandos del contenedor

**docker exec -it u roo odoo-db-data bash** 

o 

**docker exec -it u roo odoo-web-data bash** 

## Listar las imágenes

docker image ls

## Ver los contenedores corriendo

docker stats

## Modulo DatosPax
- Captura datos del pasajero.
- Automatiza tareas repetitivas.
- Evita errores de tipeo.
- Genera un Renglón para pegar en amadeus con los campos para el PNR.
- Alertas de Vencimientos de pasaporte o Visas.
- Genera campo SR DOCS al pnr
- Genera RM con datos para el backoffice y automatizar la facturación

## Módulo CopiarTst
- Copia el texto plano de un TST
- Recorta los Datos con REGEX
    + Cía. 
    + Tarifa ARS
    + Tarifa USD
    + LTD (fecha y hora)
    + Tipo de cambio
    + Ruta 
    + Fecha
    + Franqujicia de equipaje
    + Resaltar retención AFIP
- Arma cotización con varios TST
- Quedan todos los parámetros guardados por defecto con un trazado de usuario / hora.

## Nice to Have
Escribir una función que tome de Odoo la ruta / Fecha / Cía para pegar un renglón en Amadeus y cotizar.



