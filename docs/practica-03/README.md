# Práctica 03: Representación de dispositivos de red

## 1. Propósito

El propósito de esta práctica fue desarrollar un programa en Python para representar y administrar información básica de dispositivos de red, como routers y switches. Se utilizaron variables, diccionarios, listas, ciclos, condicionales y funciones para organizar los datos, consultar dispositivos, modificar sus estados y guardar la información en un archivo JSON.

Esta actividad permite establecer las bases para desarrollar herramientas de automatización de redes en futuras prácticas.

## 2. Conceptos utilizados

- **Variables:** Permiten almacenar información como nombres, direcciones IP y estados de los dispositivos.
- **Tipos de datos:** Se utilizaron cadenas de texto para representar información y números enteros para realizar conteos.
- **Función print():** Permite mostrar en la terminal los datos y resultados del programa.
- **Diccionarios:** Se utilizaron para organizar las características de cada router y switch mediante claves y valores.
- **Listas:** Permiten agrupar varios dispositivos en una sola estructura.
- **Ciclo for:** Se utilizó para recorrer los dispositivos y mostrar o analizar su información.
- **Condicional if:** Permite verificar condiciones, como identificar si un dispositivo está activo o inactivo.
- **Funciones:** Permiten organizar el código en bloques reutilizables para mostrar, buscar y modificar información de los dispositivos.

## 3. Dispositivos representados

En esta práctica se utilizaron tres dispositivos de la infraestructura de red simulada: dos routers Cisco IOSv y un switch Cisco IOSvL2. Cada dispositivo fue representado mediante un diccionario de Python que contiene sus características principales.

| Dispositivo | Tipo | Dirección IP | Estado final | Función |
|---|---|---|---|---|
| R1 | Router Cisco IOSv | 10.1.1.1 | Activo | Enrutamiento |
| R2 | Router Cisco IOSv | 10.1.1.2 | Inactivo | Enrutamiento |
| SW1 | Switch Cisco IOSvL2 | Sin asignar | Activo | Conectividad |

El programa permitió mostrar la información de los tres dispositivos, consultar sus características y modificar el estado de R2 de activo a inactivo. Finalmente, los datos fueron almacenados y recuperados mediante un archivo JSON.


## 4. Evidencias

Durante el desarrollo de la Práctica 03 se realizaron capturas de pantalla para documentar la creación y ejecución del programa en Python.

Las evidencias muestran la estructura del repositorio, la representación de dispositivos de red, el uso de diccionarios y listas, los ciclos y condicionales, la implementación de funciones y las pruebas realizadas.

Las capturas se encuentran organizadas en la carpeta `docs/practica-03/Evidencias/`.

### Evidencias del reto final

Se realizaron pruebas de búsqueda interactiva utilizando la función `input()` de Python.

El programa permitió ingresar el nombre de un dispositivo y consultar su nombre, tipo, dirección IP y estado.

Las pruebas realizadas fueron:

- Búsqueda de R1: dispositivo encontrado correctamente.
- Búsqueda de R2: dispositivo encontrado correctamente.
- Búsqueda de R5: dispositivo no encontrado.
- Búsqueda de SW1: dispositivo encontrado correctamente.

Los resultados demuestran que el programa permite consultar distintos dispositivos y detectar cuando un nombre no está registrado.



## 5. Problemas y soluciones

Durante el desarrollo de la práctica se realizaron diferentes pruebas para comprobar el funcionamiento del programa y verificar que la información de los dispositivos se mostrara correctamente.

| Problema o dificultad | Causa | Solución |
|---|---|---|
| Organizar la información de varios dispositivos. | Cada dispositivo contiene diferentes características que deben almacenarse de manera ordenada. | Se utilizaron diccionarios para representar cada dispositivo y una lista para agruparlos. |
| Identificar los dispositivos activos e inactivos. | Era necesario revisar el estado de cada dispositivo. | Se implementaron condicionales `if` para verificar y mostrar su estado. |
| Modificar la información de un dispositivo. | Se necesitaba actualizar los datos sin cambiar manualmente todas las partes del programa. | Se utilizaron funciones para buscar dispositivos y modificar sus estados. |
| Comprobar los cambios en la dirección IP. | Era necesario verificar que el programa mostrara correctamente la información modificada. | Se cambió temporalmente la IP de R1 a `10.1.1.10`, se ejecutó el programa y posteriormente se restauró a `10.1.1.1`. |
| Conservar la información de los dispositivos. | Los datos necesitaban almacenarse en un archivo para poder recuperarlos. | Se utilizó el módulo `json` para guardar y cargar la información desde `data/dispositivos.json`. |



## 6. Conclusión

En esta práctica se desarrolló un programa en Python para representar y administrar información básica de dispositivos de red, utilizando routers y switches como ejemplos.

Durante su elaboración se aplicaron conceptos de programación como variables, diccionarios, listas, ciclos, condicionales y funciones. Estos elementos permitieron organizar los datos de los dispositivos, consultar sus características, verificar sus estados y realizar modificaciones.

También se aprendió a guardar y recuperar información mediante archivos JSON, lo que facilita conservar los datos para utilizarlos posteriormente.

Finalmente, esta práctica permitió comprender cómo la programación puede ayudar a organizar y gestionar información de una red, estableciendo las bases para desarrollar herramientas de automatización más avanzadas en futuras actividades.


## 7. Preguntas de análisis

### 1. ¿Por qué es útil representar la información de los dispositivos mediante un programa?

Es útil porque permite organizar y consultar la información de los dispositivos de red de manera más rápida y sencilla. Con Python podemos visualizar sus nombres, tipos, direcciones IP y estados, además de realizar modificaciones sin tener que revisar manualmente cada dispositivo. Esto facilita la administración de una red.

### 2. ¿Qué ventaja ofrece utilizar un diccionario para representar un dispositivo?

Un diccionario permite almacenar diferentes características de un dispositivo utilizando claves y valores. Por ejemplo, podemos guardar su nombre, tipo, dirección IP y estado en una misma estructura. Esto ayuda a mantener la información organizada y facilita su consulta o modificación dentro del programa.

### 3. ¿Qué ventaja ofrece utilizar una lista para representar varios dispositivos?

Una lista permite agrupar varios dispositivos dentro de una sola estructura. En nuestra práctica utilizamos una lista que contiene los routers R1 y R2 y el switch SW1. Esto facilita recorrerlos, mostrar su información y realizar operaciones sin tener que escribir instrucciones individuales para cada uno.

### 4. ¿Qué tarea permite realizar el ciclo for?

El ciclo `for` permite recorrer los elementos de una lista y ejecutar instrucciones para cada uno. En nuestro programa lo utilizamos para mostrar la información de los dispositivos, verificar sus estados y contar cuántos se encuentran activos o inactivos.

### 5. ¿Para qué se utilizó la estructura if?

La estructura `if` se utilizó para evaluar condiciones dentro del programa. Por ejemplo, permitió identificar si un dispositivo estaba activo o inactivo y comparar nombres durante las búsquedas. De esta manera, el programa puede realizar diferentes acciones dependiendo de la información de cada dispositivo.

### 6. ¿Qué ventaja tiene utilizar una función?

Una función permite organizar el programa en bloques de código que realizan tareas específicas y pueden reutilizarse. En nuestra práctica creamos funciones para mostrar, buscar y modificar información de los dispositivos. Esto evita repetir instrucciones y facilita la comprensión y el mantenimiento del código.

### 7. ¿Qué información de los dispositivos podría obtener automáticamente un programa en una etapa posterior?

En una etapa posterior, el programa podría obtener automáticamente las direcciones IP, nombres de los dispositivos, estados de las interfaces, versiones del sistema operativo y configuraciones de red. También podría consultar información sobre conectividad y funcionamiento de los equipos mediante herramientas y protocolos de administración de redes.

### 8. ¿Qué diferencia existe entre representar información de un dispositivo y obtener esa información directamente desde el dispositivo?

Representar información consiste en almacenar manualmente los datos de un dispositivo dentro del programa, como hicimos utilizando diccionarios en Python. En cambio, obtener información directamente del dispositivo implica establecer comunicación con el equipo para consultar sus datos reales. La segunda opción permite trabajar con información actualizada de la red.

### 9. ¿Cómo podría evolucionar este programa para convertirse en una herramienta de automatización de redes?

El programa podría evolucionar incorporando funciones para conectarse automáticamente a routers y switches, consultar sus configuraciones, verificar su estado y detectar problemas de conectividad. También podría generar reportes, realizar respaldos de configuraciones y ejecutar tareas administrativas en varios dispositivos, reduciendo el trabajo manual.

### 10. ¿Qué relación existe entre esta práctica, la Práctica 2 y las siguientes prácticas del proyecto integrador?

La Práctica 2 permitió construir y configurar una infraestructura de red en GNS3, utilizando dispositivos como routers y switches. En la Práctica 3 utilizamos Python para representar y administrar información de esos dispositivos mediante estructuras de datos y funciones. Ambas prácticas establecen las bases para que, en las siguientes actividades, podamos desarrollar programas capaces de interactuar con la infraestructura de red y automatizar tareas de administración.
