# odoo-docker-postgres

Crearemos un repositorio donde guardar la configuracion de un dockerfile y docker-compose para levantar contenedores de docker que corran 

- odoo 
- postgres
- nginx
- pgadmin

El objetivo es levantar varias instancias en la nube con docker, una en **producción**, otra en **testing**, otra solo de postgres y una última con todos los backups.  Tener el mínimo off line posible.

*Revisar SublimeText para editar en la nube!*

---

## Pasos en PC local

- [ ] Correr `systemctl start docker`
- [ ] Primer paso, crear el archivo `docker-compose.yml`
- [ ] Guardar el `odoo.conf` en la ruta del volumen del contenedor
- [ ] Guardar el archivo `nginx.conf` iden
- [ ] Persistir los datos en los volúmenes

> Crear un usuario `odoo` con permisos para postgres en el container  **odoo-db-data**

|Accion|Comando|
|--|--:|
|**Arrancar los contenedores** | Correr esto en el mismo directorio donde está el archivo docker-compose.yml docker-compose up -d (para que corra en segundo plano)|
| **Detener los contenedores** | docker-compose down |
| **Restart** | docker-compose restart |
| **Entrar a la linea de comandos del contenedor** | docker exec -it u roo odoo-db-data bash | 
| **Listar las imágenes** | docker image ls |
| **Ver los contenedores corriendo** | docker stats |
| **Ver los contenedores activos** | docker ps |

---

# Modulos Odoo para Agencias de Viajes / Retail Mayorista y Minorista

### DatosPax
### Copia TST
### Presupuestador
### Reporteador

---

## Módulo DatosPax (40 hs. desarrollo / Realizadas 10)

- [x] Agrega Menú / Sub menú **(OK)**.

![Menú datospax](/Static/datospax1.jpg "Menu DatosPax")

- [x] ABM pasajeros. **(OK)**

- ![ABM datospax](/Static/datospax2.jpg "Form datos pax")

- [x] Captura datos del pasajero **Odoo2Amadeus** / **Amadeus2Odoo** 
- ![copiar datospax para el PNR](/Static/datospax3.jpg "Datos pax al pnr")

- Automatiza tareas repetitivas evita errores de tipeo.  reduce costos por **ADM'S**
- [ ] Genera un Renglón para pegar en Amadeus con los campos para el PNR con los campos `NM, AP, TK, SRDOCS, OS, SR FQTV y RM{nrocliente}` (En desarrollo)
- [ ] Ciclo for que enumera los pasajeros y pega ese valor en `/p{valor}`
- [x] Alertas de **Vencimientos** de pasaporte o Visas **(OK)** como TIME LIMIT en el `Formulario` y en el `Calendario`
![Vto Pasaporte y Visa USA](/Static/datospax4.jpg "Formulario de Carga")


![Vista Calendario VTO Pass ](/Static/datospax5.jpg "Calendario Vencimientos")

- [ ] Segmentador de público.
- [x] Genera **RM** con datos para el backoffice y automatizar la facturación.
- [x] Vinculación `Many2one` a un contacto en `res.partner`.
- [x] Agrega calidad al proceso de generación de un PNR al incluir `FrequentFlyer FFR`, `SRFOID`. Contacto automatizado en el PNR con `OSICTC` servicios especiales `SSR`, Documentación obligatoria para ciertas cias/destinos `SRDOCS`, etc. Al no omitir detalles que hacen a la *agencia boutique* 
- [x] Este beneficio está disponible en **Profiles** del lado del GDS, pero los datos quedan en una fuente externa.  
- [x] Teniendo este módulo la agy se independiza del proveedor.
- [x] **MultiGds** le da independencia a la agy incluso del GDS.

---

## Módulo CopiarTst (30 hs. desarrollo / realizadas 5)

- [x] Copia el texto plano de un TST **(OK)** que están en el ejemplo: /Static/tst.txt
- [ ] Agrear el título que indique al usuario que debe pegar todo el TST completo, las dos o tres páginas para que no se rompa.  Tooltip.
- [ ] Parsear TST es otro título.   Ver tst guardados.
- [ ] Error al traer el Q1 cuando cambia de renglón.

![Imagen del capturador del tst](/Static/tst2.jpg "Capturador")

- [x] Recorta los Datos con REGEX **(OK)**

- [x] Cía. 
- [x] Tarifa ARS
- [x] Tarifa USD
- [x] LTD (fecha y hora del último momento para emitir el tkt)
- [x] Tipo de cambio (validar contra el GDS)
- [x] Ruta 
- [x] Fechas
- [x] Franqujicia de equipaje
- [x] Resaltar retención AFIP

- ![Tst recortado y datos persistidos ](/Static/tst3.jpg "scrap de datos del tst de amadeus")

---

### Nota importante

- [ ] Este módulo aún tiene los modelos como flotantes, debemos `Corregir Monedas del tst para que podamos aplicarles tipos de cambio`
- [ ] Posibilidad de ver en el presupuesto las dos monedas y el tipo de cambio.
- [ ] Aclarar tipos de financiaciones en un modelo para empujar ventas hacia cierta financiación, estimar esfuerzo.

---

![Imagen TST Copiado](/Static/tst1.jpg "TST Copiado")

- [ ] Arma cotización con varios 'TST', varias veces se corre el proceso, varios botones dependiendo si la cotización es en ARS o en USD.

![Agregar botones que faltan COT USD / COT ARS / AGREGAR SEGURO XX / ETC](/Static/tst5.jpg "Botones para cotizaciones distintas")

- [ ] Cambia a dolar Turista.  Agregar 2 dolares distintos.
- [ ] Quedan todos los parámetros guardados por defecto con un trazado de usuario / hora.
- [ ] **HELP** al usuario que agregue `/SBF-1` en be odoo con un *tooltip*, para que si el presupuesto salió sin equipaje, invitándolo a gue genere otro con equipaje.
- [ ] Armar Diccionario con grupos de Ciudades / Aeropuertos segmentados por región, a subir vía archivo `.csv`
- [ ] Markups automatizados para las regiones.
- [ ] Securización CRUD de este módulo para administradores solamente.

![Securización de los módulos por grupos](/Static/tst4.jpg "Ventana permisos de módulos")

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

- Dividir presupuestos por tipos de viajes indexando categorías, para mejorar el ***Revenue Management*** haciendo reglas de MU puntuales y para poder mostrar estadísticas periódicas (no puede mejorarse lo que no puede medirse) y poder enfocarse en lo rentable.  
- Ejemplo:

> Plantilla Aéreo **Internacional** Leisure.

> Plantilla Aéreo **Internacional** Migrante.
> 

![Aletas y recomendaciones por defecto, pegar variables puntuales como tipo de cambio](/Static/presupuesto1.jpg "Plantilla presupuesto")


---

## Módulo hereda de SaleOrder (30 hs)

- [ ] Armar método, botón en el **MENU PRESUPUESTO** que automatice la carga de los datos de un TST previamente generado en **Amadeus**.  

- [ ] Seleccionar pasajeros de una lista, para generar ese renglón.

- [ ] Copiar **MiniRules** o Notas más importantes al presupuesto, también por clipboard (dependemos que el OID de la agy tenga habilitado minirules)

- [ ] Idem **Masterpricer**

---

## Gantt / Linea del tiempo Presupuesto (20 hs)

Cambio de color cuando se carta el TST automatizado al Presupuesto

### Inicio > Cargar TST > Cargar nota > Revisar MU > OK > Enviar por email

---


## Tablero Destinos (10 hs)

- [ ] Hacer un tablero de los destinos, con su markup puntual.
- [ ] Ver rentabilidad por destinos.
- [ ] Idem por tipo de viajes a partir del modelo de presupuesto.

---

## Tableros de comando comercial (10 hs)

- [ ] Rentabilidad promedio por destino, presupuestos por destino
- [ ] Rentabilidad por Segmento
- [ ] Ratio conversión 


---

## Configurar correo viral y plantillas para publicidades masivas (20 hs)
- [ ] Cuenta en Mailchimp
- [ ] Conectarla a odoo
- [ ] Diseñar plantillas / Buscar hechas




