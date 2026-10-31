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

**Pendiente:** agregar la conclusión individual de cada integrante del equipo.

