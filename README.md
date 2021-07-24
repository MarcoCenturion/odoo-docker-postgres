# odoo-docker-postgres

Crearemos un repositorio donde guardar la configuracion de un dockerfile y docker-compose para levantar contenedores de docker que corran 

- odoo 
- postgres
- nginx
- pgadmin

El objetivo es levantar varias instancias en la nube con docker, una en producción, otra en testing, otra solo de postgres y una última con todos los backups.  Tener el mínimo off line posible.

*Revisar SublimeText para editar en la nube!*

---

## Pasos
-1 [ ] Correr systemctl start docker
-2 [ ] Primer paso, crear el archivo docker-compose.yml
-3 [ ] Guardar el odoo.conf en la ruta del volumen del contenedor
-4 [ ] Persistir los datos en los volúmenes

> Crear un usuario odoo con permisos para postgres en el container  
**odoo-db-data**

|Accion|Comando|
|--|--|
|**Arrancar los contenedores** | Correr esto en el mismo directorio donde está el archivo docker-compose.yml docker-compose up -d (para que corra en segundo plano)|
| **Detener los contenedores** | docker-compose down |
| **Restart** | docker-compose restart |
| **Entrar a la linea de comandos del contenedor** | docker exec -it u roo odoo-db-data bash | 
| **Listar las imágenes** | docker image ls |
| **Ver los contenedores corriendo** | docker stats |
| **Ver los contenedores activos** | docker ps |

---

# Modulos Odoo para Agencias de Viajes / Retail Mayorista y Minorista
---
    
## Módulo DatosPax (40 hs. desarrollo / Realizadas 10)

- [x] Agrega Menú / Sub menú **(OK)**.

![Menú datospax](/Static/datospax1.jpg "Menu DatosPax")

- [x] ABM pasajeros. **(OK)**

- ![ABM datospax](/Static/datospax2.jpg "Form datos pax")

- [x] Captura datos del pasajero **Odoo2Amadeus** / **Amadeus2Odoo** 
- ![copiar datospax para el PNR](/Static/datospax3.jpg "Datos pax al pnr")

- Automatiza tareas repetitivas evita errores de tipeo.  reduce costos por **ADM'S**
- [ ] Genera un Renglón para pegar en Amadeus con los campos para el PNR con los campos `NM, AP, TK, SRDOCS, OS, SR FQTV y RM{nrocliente}`
- [ ] Ciclo for que enumera los pasajeros y pega ese valor en `/p{valor}`
- [ ] Alertas de **Vencimientos** de pasaporte o Visas **(OK)**.
- [ ] Genera **RM** con datos para el backoffice y automatizar la facturación.
- [ ] Agrega calidad al proceso de generación de un PNR al incluir FrequentFlyer, servicios especiales, SRDOCS, etc.
- [ ] Este beneficio está disponible en **Profiles** del lado del GDS, pero los datos quedan en una fuente externa.  
- [ ] Teniendo este módulo la agy se independiza del proveedor.
- [ ] **MultiGds** le da independencia a la agy incluso del GDS.

---

## Módulo CopiarTst (30 hs. desarrollo / realizadas 5)

- [x] Copia el texto plano de un TST **(OK)** que están en el ejemplo: /Static/tst.txt

![Imagen del capturador del tst](/Static/tst2.jpg "Capturador")

- [x] Recorta los Datos con REGEX **(OK)**

    + Cía. 
    + Tarifa ARS
    + Tarifa USD
    + LTD (fecha y hora)
    + Tipo de cambio
    + Ruta 
    + Fecha
    + Franqujicia de equipaje
    + Resaltar retención AFIP

---

Este módulo aún tiene los modelos como flotantes, debemos `'corregir Monedas del tst para que podamos aplicarles tipos de cambio'`

---

![Imagen TST Copiado](/Static/tst1.jpg "TST Copiado")

- [ ] Arma cotización con varios 'TST', varias veces se corre el proceso.
- [ ] Cambia a dolar Turista.  Agregar 2 dolares distintos.
- [ ] Quedan todos los parámetros guardados por defecto con un trazado de usuario / hora.
- [ ] **HELP** al usuario que agregue `/SBF-1` en be odoo con un *tooltip*, para que si el presupuesto salió sin equipaje, invitándolo a gue genere otro con equipaje.
- [ ] Diccionario con grupos de Ciudades / aeropuertos segmentados por región, a subir vía archivo `.csv`.
- [ ] Markups automatizados para las regiones.
- [ ] Securización CRUD de este módulo para administradores solamente.

---

## Módulo importador de TKTS (20 hs. desarrollo / hecho 0)
- [ ] Capturar los .AIR (Amadeus) o .SPL (Sabre) de los tkts emitidos, parcear toda la info contable, y buscar el renglón `RM{NROCLIENTE}` para armar la factura automatizada. 
- [ ] Todo un capítulo aparte para poder captar agencias que emitan y quieran salirse del esquema de los proveedores oficiales de **ERP's** globales.

---

# N2H
- [ ] Escribir una función que tome de Odoo la ruta / Fecha / Cía para pegar un renglón en Amadeus y cotizar.
- [ ] Cambiar en JS letras ingresadas por el usuario por las aceptadas en Amadeus. Ñ por N, vocales acentuadas por vocales sin acento.
- [ ] Editar en la nube.

---

## Sale.order  (Mejoras al presupuesto para adaptarlo a agencia de viajes retail)
### Aéreos (30 hs / hechas 10)
### Terrestre (40 hs / hechas 0)

- Dividir presupuestos por tipos de viajes indexando categorías, para mejorar el Revenue Management haciendo reglas de MU puntuales y para poder mostrar estadísticas periódicas (no puede mejorarse lo que no puede medirse).  
- Ejemplo:

> Aéreo Internacional Leisure.

> Aéreo Internacional Migrante.

> Aéreo Internacional Congreso.

> Aéreo Internacional a Cliente tiempo compartido.

> Aéreo Cabotaje corporativo.

> Aéreo Cabotaje Leisure.

> Terrestre Argentina Vacaciones.

> Terrestre noches sueltas internacional.


## Módulo hereda de SaleOrder (30 hs)

- [ ] Armar método, botón en el **MENU PRESUPUESTO** que automatice la carga de los datos de un TST previamente generado en **Amadeus**.  

- [ ] Seleccionar pasajeros de una lista, para generar ese renglón.

- [ ] Copiar **MiniRules** o Notas más importantes al presupuesto, también por clipboard (dependemos que el OID de la agy tenga habilitado minirules)

- [ ] Idem **Masterpricer**

## Gantt / Linea del tiempo Presupuesto (20 hs)

Cambio de color cuando se carta el TST automatizado al Presupuesto

### Inicio > Cargar TST > Cargar nota > Revisar MU > OK > Enviar por email


## Tablero Destinos (10 hs)

- [ ] Hacer un tablero de los destinos, con su markup puntual.
- [ ] Ver rentabilidad por destinos.
- [ ] Idem por tipo de viajes a partir del modelo de presupuesto.

## Tableros de comando comercial (10 hs)

- [ ] Rentabilidad promedio por destino, presupuestos por destino
- [ ] Rentabilidad por Segmento
- [ ] Ratio conversión




