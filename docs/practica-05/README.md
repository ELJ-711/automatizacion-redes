# Práctica 5: Mi primer script en Python para la automatización de redes

## 1. Objetivo
Configurar y ejecutar un script de Python que permita automatizar la configuración de un router Cisco mediante Telnet en un entorno de laboratorio GNS3.

## 2. Relación con las prácticas anteriores
En las prácticas anteriores se preparó el entorno de trabajo, se construyó una infraestructura simulada en GNS3, se representaron dispositivos mediante Python y se investigaron recursos técnicos. En esta práctica se aplicaron estos conocimientos para realizar configuraciones automáticas en un router.

## 3. Topología y direccionamiento
La topología se desarrolló en GNS3 utilizando:

- Network Automation Container (NAC).
- Ethernet Switch.
- NAT Cloud.
- Switch Cisco IOSvL2.
- Router Cisco IOSv (R1).

**Direcciones IP utilizadas:**

- NAC: 192.168.185.130
- Router R1: 192.168.185.70
- Loopback 0: 1.1.1.1
- Loopback 1: 2.2.2.2

## 4. Versión de Python
Se utilizó Python 3.8.5 en el Network Automation
Container (NAC) de GNS3 para desarrollar y
ejecutar el script de automatización mediante Telnet.

## 5. Explicación del script
Se desarrolló un script en Python utilizando la biblioteca `telnetlib` para establecer una conexión Telnet con R1. El programa solicita credenciales de acceso, ingresa al modo privilegiado y envía comandos para configurar dos interfaces Loopback y el protocolo OSPF en el área 0.

## 6. Tabla de pruebas

| Prueba | Resultado |
|---|---|
| Asignación de IP mediante DHCP al NAC | Exitosa |
| Conectividad entre NAC y R1 | Exitosa |
| Acceso al router mediante Telnet | Exitoso |
| Ejecución del script Python | Exitosa |
| Creación de Loopback 0 | Exitosa |
| Creación de Loopback 1 | Exitosa |
| Configuración de OSPF | Exitosa |

## 7. Problemas y soluciones
Durante el desarrollo se presentaron problemas de conectividad porque el router y el NAC tenían direcciones IP de diferentes subredes. Se solucionó modificando la dirección IP de R1.

También se presentaron errores en el código Python, que se corrigieron revisando la sintaxis y las instrucciones de conexión Telnet.


## 8. Conclusiones individuales

### Elizabeth
Esta práctica me permitió comprender mejor la relación que existe entre la programación y el funcionamiento de una red. Considero que una de las partes más importantes fue trabajar con GNS3, ya que pudimos observar cómo interactúan los diferentes dispositivos dentro de una topología. También aprendí que es necesario llevar un orden durante las configuraciones para evitar errores que afecten la comunicación. La creación de las interfaces Loopback y la configuración de OSPF me ayudaron a conocer otras funciones de los routers. Finalmente, esta actividad me permitió reconocer la importancia de documentar los procedimientos y conservar evidencias para comprobar los resultados obtenidos.

### Edson 
Durante esta práctica aprendí cómo utilizar Python para automatizar la configuración de dispositivos de red mediante Telnet. Al principio tuvimos algunos problemas con las direcciones IP y errores en el código, pero logramos solucionarlos mediante diferentes pruebas. Lo que más me llamó la atención fue comprobar que un script puede ejecutar varios comandos en un router sin necesidad de introducirlos manualmente. También comprendí la importancia de verificar la conectividad antes de realizar cualquier configuración. Esta actividad me permitió mejorar mis conocimientos de programación y administración de redes, además de entender cómo estas herramientas pueden facilitar el trabajo de un administrador de infraestructura.

### Pedro
Con esta actividad pude identificar la importancia de establecer correctamente los parámetros de comunicación entre los dispositivos de una red. La asignación de direcciones IP, la comprobación mediante ping y el acceso remoto fueron elementos fundamentales para conseguir que la automatización funcionara. Además, comprendí que los comandos enviados desde Python deben tener una estructura adecuada para que el router pueda interpretarlos correctamente. La práctica también permitió observar cómo se pueden realizar configuraciones de manera remota y verificar posteriormente sus resultados. Estos conocimientos son útiles para administrar infraestructuras de red de forma más organizada y eficiente.

### Alejandro
Al realizar esta práctica comprendí que la automatización puede ayudar a reducir el tiempo necesario para configurar equipos de red, especialmente cuando se deben aplicar varias instrucciones. Una parte interesante fue utilizar un programa de Python para establecer una sesión Telnet y modificar la configuración de un router Cisco. También observé que los errores pueden presentarse tanto en el código como en la comunicación entre los dispositivos, por lo que es importante revisar cada resultado antes de continuar. Considero que esta experiencia fue útil para conocer una aplicación práctica de la programación dentro del área de redes y entender por qué es importante desarrollar procedimientos que puedan repetirse de manera controlada.
