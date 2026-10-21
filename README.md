# Automatizacion de Redes
# Mi estación de automatización de redes

## 1. Datos del equipo

Integrantes:
- Edson López Jiménez
- [Elizabeth Maldonado Sanchez]
- [Daniel Alejandro Venegas Vargas]
- [Daniel Pedro Cortes Zuñiga]

Asignatura: Automatización de Infraestructura Digital I

## 2. Propósito de la práctica

El propósito de esta práctica fue preparar una estación de trabajo para realizar actividades de automatización de redes. Para ello se instalaron y configuraron diferentes herramientas de programación, control de versiones, pruebas, virtualización y simulación de redes.

## 3. Herramientas instaladas

Durante la práctica se instalaron y configuraron las siguientes herramientas:

- Python
- Visual Studio Code
- Git
- GitHub
- Postman
- OpenConnect
- Docker Desktop
- GNS3
- GNS3 VM
- VMware Workstation Pro

## 4. Configuración realizada

Se configuró Python para trabajar desde Visual Studio Code, se creó un entorno virtual y se comprobó la ejecución de un programa de prueba.

También se configuró la identidad de Git con nombre y correo electrónico, se creó un repositorio en GitHub y se conectó con el repositorio local.

Finalmente se configuraron Docker, GNS3, VMware Workstation y la GNS3 VM para contar con un entorno de virtualización y simulación de redes.

## 5. Verificación del entorno

Se realizaron diferentes pruebas para comprobar el funcionamiento de las herramientas instaladas.

Python y Git fueron verificados mediante comandos de versión. Docker se comprobó ejecutando el contenedor hello-world. GNS3 se abrió correctamente y se integró con la GNS3 VM mediante VMware Workstation.

## 6. Estructura del proyecto

automatizacion-redes/
├── README.md
├── requirements.txt
├── src/
├── tests/
├── data/
└── docs/
    └── practica-01/
        ├── evidencias/
        ├── instalacion.md
        ├── configuracion.md
        └── verificacion.md

## 7. Problemas encontrados y soluciones

Durante la práctica se presentaron algunos problemas de configuración. Docker inicialmente no podía ejecutar contenedores debido a que el equipo no tenía conexión a Internet. Después de restablecer la conexión, se logró ejecutar correctamente el contenedor hello-world.

También se presentó un problema al integrar GNS3 con VMware porque GNS3 no encontraba el archivo vmrun. El problema se solucionó configurando correctamente la ruta de VMware dentro de las preferencias de GNS3.

## 8. Conclusiones

Esta práctica permitió preparar un entorno completo para trabajar con automatización y simulación de redes. Durante el proceso se instalaron diferentes herramientas y se resolvieron algunos problemas de configuración. Al finalizar se logró contar con un entorno funcional para continuar con las siguientes prácticas del proyecto.

## Avance del proyecto integrador

### Práctica 1
Preparación de la estación de automatización de redes.  
Estado: Completada.

### Práctica 2
Construcción de la red simulada en GNS3.  
Estado: Completada.

Infraestructura construida:
- Topología básica PC-Switch-PC.
- Topología con dos routers y un switch multicapa.
- Direccionamiento IP.
- Conectividad entre dispositivos.
- Protocolo OSPF.
- Verificación de tablas de enrutamiento.

Próximo paso:
Desarrollo de scripts y herramientas para automatizar tareas sobre la infraestructura de red.



## Avance del proyecto integrador

El proyecto integrador tiene como objetivo aplicar conocimientos de redes y programación para desarrollar herramientas que faciliten la organización y administración de dispositivos de red.

### Práctica 01: Organización del proyecto
**Estado:** Completada.

Se estableció la estructura inicial del repositorio, organizando las carpetas y archivos necesarios para documentar las actividades y almacenar los programas del proyecto.

### Práctica 02: Infraestructura de red
**Estado:** Completada.

Se trabajó en la representación y documentación de la infraestructura de red, identificando los dispositivos y sus características principales para utilizarlos como referencia en las siguientes prácticas.

### Práctica 03: Representación de dispositivos con Python
**Estado:** Completada.

Se desarrolló un programa en Python que permite representar routers y switches mediante diccionarios y listas, consultar su información, verificar sus estados, modificar datos y guardar los resultados en un archivo JSON.

### Siguiente paso

Continuar con el desarrollo del proyecto integrador, incorporando nuevas funciones que permitan mejorar la consulta y administración de dispositivos de red mediante Python.



### Práctica 4

**Exploración de comunidades, documentación y recursos de colaboración.**

**Estado:** Completada.

Se identificaron y analizaron recursos de documentación y comunidades relacionados con Python, GNS3 y la automatización de redes.

Se organizó una base de conocimiento técnica con recursos de Python, documentación de redes, comunidades de colaboración, evaluación de confiabilidad y una estrategia de investigación de problemas.

**Próximo paso:**

Continuar el desarrollo de programas en Python y utilizar los recursos técnicos investigados para resolver problemas durante las siguientes etapas del proyecto integrador.