[[TOC]]

# odoo-docker-postgres

Crearemos un repositorio donde guardar la configuracion de un dockerfile y docker-compose para levantar contenedores de docker que corran de manera local para usarlos de entorno de desarrollo. 

- odoo 
- postgres
- nginx
- pgadmin

El objetivo es levantar varias instancias en la nube con docker, una en **producción**, otra en **testing**, otra solo de postgres y una última con todos los backups.  Tener el mínimo off line posible.

- [ ] nvim en servidor remoto

---

# Pasos en PC local

- [ ] Primer paso, crear carpetas para configuracion odoo y para los addons.
- [ ] Segundo paso, crear el archivo `docker-compose.yml` 
- [ ] Correr `systemctl start docker` para levantar el sistema
- [ ] Guardar el `odoo.conf` en la ruta del volumen del contenedor
- [ ] Guardar el archivo `nginx.conf` idem
- [x] Persistir los datos en los volúmenes
- [x] Recovery disaster de bases en producción

> Crear un usuario `odoo` con permisos para postgres en el container  **odoo-db-data**

|Accion|Comando|
|--|--:|
|**Arrancar los contenedores** | Correr esto en el mismo directorio donde está el archivo docker-compose.yml `docker-compose up -d` (para que corra en segundo plano)|
| **Detener los contenedores** | `docker-compose down` |
| **Restart** | `docker-compose restart` |
| **Entrar a la linea de comandos del contenedor** | `docker exec -it u roo odoo-db-data /bin/bash` | 
| **Listar las imágenes** | `docker image ls` |
| **Ver los contenedores corriendo** | `docker stats` |
| **Ver los contenedores activos** | `docker ps` |

---

# Modulos Odoo para Agencias de Viajes 

Retail Mayorista y Minorista

- Passenger_data -Agrega a res.partner la lógica por pasajeros-
- Copia TST
- Presupuestador 
- Pasar presupuesto a file
  - Item por producto en el file. (wizzard con la lógica del producto)
  - Vencimiento por producto / proveedor.  Campo fecha a ver en la vista calendario.
  - Manejo de costos.
- Crear plantillas de presupuestos que van a iniciar el flujo correcto.  ¿Etiquetas para esto?
- Reporteador.  Esto se resuelve del lado del usuario.  Se crea un "tablero" propio con las vistas. 
- Alertas por email y SMS (configuración de servicios de email)
- Lógica del file costos vs. ventas
- Calendario de salidas, vto de pasaporte, cumpleaños, etc.  En una vista calendario.

---
## File.  Diseñar como armar el file.  (80 hs desarrollo / realizadas 0)

Crear un notebook en la línea en que están los detalles del presupuesto / venta y agregar al final una etiqueta **Costos del File**.

| Líneas del pedido | Productos opcionales | Otra Información | Firma del Cliente | *Costos del file*. |

- Proveedor.
- Costo.  Gastos.  
- Vencimiento pagos.
- Inicio de servicios.

## Módulo passenger_data (40 hs. desarrollo / Realizadas 16)

- [ ] Armar flujo de proyecto en TH consultora y seguir esto.
- [x] Datos Adicionales al pasajero en res.partner **(OK)**.
- [x] Agregar imágenes y verlas en la vista **(OK)**.
- [ ] Mejorar vista datos.
- [ ] ABM pasajeros. **(OK)**.
- [ ] Captura datos del pasajero **Odoo2Amadeus** / **Amadeus2Odoo** 
- [ ] Automatiza tareas repetitivas evita errores de tipeo.  reduce costos por **ADM'S**
- [ ] Genera un Renglón para pegar en Amadeus con los campos para el PNR con los campos `NM, AP, TK, SRDOCS, OS, SR FQTV y RM{nrocliente}` (En desarrollo)
- [ ] Ciclo for que enumera los pasajeros y pega ese valor en `/p{valor}`
- [x] Alertas de **Vencimientos** de pasaporte o Visas **(OK)** como TIME LIMIT en el `Formulario` y en el `Calendario` 
- [ ] Agregar vista calendario `Salidas` y `vencimiento de señas`
- [ ] Módulo disparador de alertas al usuario, a los seguidores del file y al pasajero, para vencimientos de pasaportes, de señas al proveedor, de salida, etc.
- [ ] Segmentador de público -por etiquetas-
- [x] Genera **RM** con datos para el backoffice y automatizar la facturación.
- [x] Vinculación `Many2one` a un contacto en `res.partner`.
- [x] Agrega calidad al proceso de generación de un PNR al incluir `FrequentFlyer FFR`, `SRFOID`. Contacto automatizado en el PNR con `OSICTC` servicios especiales `SSR`, Documentación obligatoria para ciertas cias/destinos `SRDOCS`, etc. Al no omitir detalles que hacen a la *agencia boutique* 
- [x] Este beneficio está disponible en **Profiles** del lado del GDS, pero los datos quedan en una fuente externa.  
- [x] Teniendo este módulo la agy se independiza del proveedor.
- [x] **MultiGds** le da independencia a la agy incluso del GDS.

---

## Módulo CopiarTst (30 hs. desarrollo / realizadas 5)

- [x] Copia el texto plano de un TST **(OK)** que están en el ejemplo: `/Static/tst.txt`
- [x] Arma la ruta con los segmentos de vuelos.
- [ ] Armar script en amadeus que haga todo.
- [ ] Presupuestador en Pesos y Dolares.
- [ ] Agrear el título que indique al usuario que debe pegar todo el TST completo, las dos o tres páginas para que no se rompa.  Tooltip.
- [x] Parsear TST es otro título.   Ver tst guardados.
- [x] Error al traer el Q1 cuando cambia de renglón.
- [ ] Lógica separada para cabotaje e internacional.
- [ ] Lógica separada para emisiones en USD o ARS.
- [x] Recorta los Datos con REGEX **(OK)**
- [x] Cía. 
- [x] Tarifa ARS.
- [x] Tarifa USD.
- [x] LTD (fecha y hora del último momento para emitir el tkt).
- [x] Tipo de cambio (validar contra el GDS).
- [x] Origen.
- [x] Destinos.
- [x] Fechas.
- [x] Franqujicia de equipaje.
- [x] Resaltar retención AFIP.
- [ ] Notas de la tarifa.
- [ ] Proyecto en TH Consultora con los gantt de tiempos de cada módulo.

## Pegarle en el renglon del presupuesto el contenido del TST desmenuzado.

- [ ] Define dictionary to add order_line
`order_line_dict = { 'order_id' : 9, 'product_id': 2003, 'price_unit': 3000.0, 'product_uom_qty': 2.0, 'name': '' }`

- [ ] Search the order line for the sale order
`sale_order_line = self.env['sale.order.line'].browse(9)`

- [ ] Create a new order line
`sale_order_line.create(order_line_dict)`

- [ ] Print sale order lines
`sale_order_line`

- [ ] Note
If you are doing/testing this on the Odoo Shell, then make sure to run the following after the changes to reflect on database:
`self.env.cr.commit()`

---

### Nota importante

- [ ] Este módulo aún tiene los modelos como flotantes, debemos `Corregir Monedas del tst para que podamos aplicarles tipos de cambio`
- [ ] Posibilidad de ver en el presupuesto las dos monedas y el tipo de cambio.
- [ ] Boton para que cambie el presupuesto de USD a ARS y viceversa. en este caso USD será el `USD Turista.` 
- [ ] Aclarar tipos de financiaciones en un modelo para empujar ventas hacia cierta financiación, estimar esfuerzo.

---

- [ ] Arma cotización con varios 'TST', varias veces se corre el proceso, varios botones dependiendo si la cotización es en ARS o en USD.

- [ ] Cambia a dolar Turista.  Agregar 2 dolares distintos.
- [ ] Quedan todos los parámetros guardados por defecto con un trazado de usuario / hora.
- [ ] **HELP** al usuario que agregue `/SBF-1` en be odoo con un *tooltip*, para que si el presupuesto salió sin equipaje, invitándolo a gue genere otro con equipaje.
- [ ] Armar Diccionario con grupos de Ciudades / Aeropuertos segmentados por región, a subir vía archivo `.csv`
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
	
## Sale.order  

(Mejoras al presupuesto para adaptarlo a agencia de viajes retail)

### Aéreos (30 hs / hechas 10)

### Terrestre (40 hs / hechas 0)

Dividir presupuestos por tipos de viajes indexando categorías, para mejorar el ***Revenue Management*** haciendo reglas de MU puntuales y para poder mostrar estadísticas periódicas (no puede mejorarse lo que no puede medirse) y poder enfocarse en lo rentable.  Se establece una plantilla por tipo de viaje y esta acomoda la información a utilizar.

Ejemplo:

> Plantilla Aéreo **Internacional** Leisure.

> Plantilla Aéreo **Internacional** Migrante.

> Aéreo Cabotaje. 

---

## Módulo hereda de SaleOrder (30 hs)

- [ ] Armar método, botón en el **MENU PRESUPUESTO** que automatice la carga de los datos de un TST previamente generado en **Amadeus**.  

- [ ] Seleccionar pasajeros de una lista, para generar ese renglón.

- [ ] Copiar **MiniRules** o Notas más importantes al presupuesto, también por clipboard (dependemos que el OID de la agy tenga habilitado minirules)

- [ ] Idem **Masterpricer**

---

## Gantt / Linea del tiempo Presupuesto (20 hs)

- Cambio de color cuando se carta el TST automatizado al Presupuesto

Inicio > Cargar TST > Cargar nota > Revisar MU > OK > Enviar por email

```plantuml
@startmindmap
title Flujo Presupuesto 
!theme amiga
* Motor Mu  
 ** Plantilla Condiciones\nGenerales
  *** Enviar email\nal pax
  *** Graba actividad CRM 
   **** ToDo

left side
** Cargar Nota tarifaria
** Copiar TST
*** FXD
**** Aéreo
** Copiar
*** Scrapear\nWeb
**** Terrestre

legend: Switch Botón\nAéreo - Terrestre 
@endmindmap
```

---

## Motor markup por destinos (10 hs)

Segmentar productos / categorías para aplicar reglas de MU.

- [ ] Hacer un tablero de los destinos, con su markup puntual.
- [ ] Ver rentabilidad por destinos.
- [ ] Idem por tipo de viajes a partir del modelo de presupuesto.

---

## Tableros de comando comercial (10 hs)

Armar las vistar de productos, rentabilidad, etc.

- [ ] Rentabilidad promedio por destino, presupuestos por destino
- [ ] Rentabilidad por Segmento
- [ ] Ratio conversión 

---

## Configurar correo viral y plantillas para publicidades masivas (20 hs)

- [ ] Conectarla a odoo
- [ ] Diseñar plantillas / Buscar hechas

---

### Checklist implementación Odoo

|Orden|Tarea|
|--|--:|
|1  |Decidir Nube  
|2  |Instalar Odoo  
|3  |Instalar localización  
|4  |Configurar Email  
|5  |Configurar Compañia  
|6  |Cargar Plan de Cuentas  
|7  |Cargar Productos  
|8  |Cargar Clientes  
|9  |Cargar Proveedores  
|10  |Cargar Tarifas  
|11  |Asiento de Apertura  
|12  |Configurar Moneda  
|13  |Certificar la empresa  
|14  |Crear Bodegas  
|15  |Crear Ubicaciones  
|16  |Crear Puntos de Ventas  
|17  |Categorias de Productos  
|18  |Configurar Asientos  
|19  |Crear Cuentas Analiticas 

---

## Gabriela Rivero

- Buscar el modulo de PMS desarrollado en odoo 10.
- Actualizarlo a odoo 14 CE.
- Agregar lógicas faltantes con Belen.

