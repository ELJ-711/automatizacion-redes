
import json

router1 = {
    "nombre": "R1",
    "tipo": "Router Cisco IOSv",
    "ip": "10.1.1.1",
    "interfaz": "GigabitEthernet0/0",
    "estado": "Activo",
    "mascara": "255.255.255.0",
    "loopback": "1.1.1.1"
}

router2 = {
    "nombre": "R2",
    "tipo": "Router Cisco IOSv",
    "ip": "10.1.1.2",
    "interfaz": "GigabitEthernet0/0",
    "estado": "Activo",
    "mascara": "255.255.255.0",
    "loopback": "2.2.2.2"

}

switch1 = {
    "nombre": "SW1",
    "tipo": "Switch Cisco IOSvL2",
    "ip": "Sin asignar",
    "interfaz": "GigabitEthernet0/0",
    "estado": "Activo",
    "mascara": "Sin asignar",
    "loopback": "No aplica"     
}

dispositivos = [router1, router2, switch1]



def mostrar_dispositivos(lista):
    for dispositivo in lista:
        print("-------------------------")
        print("Nombre:", dispositivo["nombre"])
        print("Tipo:", dispositivo["tipo"])
        print("Dirección IP:", dispositivo["ip"])
        print("Interfaz:", dispositivo["interfaz"])

        if dispositivo["estado"] == "Activo":
            print("Estado: Dispositivo activo")
        else:
            print("Estado: Dispositivo inactivo")

        print("Máscara:", dispositivo["mascara"])
        print("Loopback:", dispositivo["loopback"])

mostrar_dispositivos(dispositivos)


print("-------------------------")
print("Total de dispositivos:", len(dispositivos))


activos = 0
inactivos = 0

for dispositivo in dispositivos:
    if dispositivo["estado"] == "Activo":
        activos += 1
    else:
        inactivos += 1

print("Dispositivos activos:", activos)
print("Dispositivos inactivos:", inactivos)



def buscar_dispositivo(lista, nombre):
    for dispositivo in lista:
        if dispositivo["nombre"] == nombre:
            print("-------------------------")
            print("Dispositivo encontrado")
            print("Nombre:", dispositivo["nombre"])
            print("Dirección IP:", dispositivo["ip"])
            print("Estado:", dispositivo["estado"])
            return

    print("Dispositivo no encontrado")


buscar_dispositivo(dispositivos, "R1")



def cambiar_estado(lista, nombre, nuevo_estado):
    for dispositivo in lista:
        if dispositivo["nombre"] == nombre:
            dispositivo["estado"] = nuevo_estado
            print("-------------------------")
            print("Estado actualizado correctamente")
            print("Dispositivo:", dispositivo["nombre"])
            print("Nuevo estado:", dispositivo["estado"])
            return

    print("Dispositivo no encontrado")


cambiar_estado(dispositivos, "R2", "Inactivo")



print("-------------------------")
print("Verificación después del cambio de estado")

mostrar_dispositivos(dispositivos)



with open("data/dispositivos.json", "w", encoding="utf-8") as archivo:
    json.dump(dispositivos, archivo, indent=4, ensure_ascii=False)

print("-------------------------")
print("Información guardada correctamente en JSON")


with open("data/dispositivos.json", "r", encoding="utf-8") as archivo:
    dispositivos_guardados = json.load(archivo)

print("-------------------------")
print("Información recuperada desde JSON")
mostrar_dispositivos(dispositivos_guardados)


print("-------------------------")
print("Total de dispositivos recuperados:", len(dispositivos_guardados))


activos_json = 0
inactivos_json = 0

for dispositivo in dispositivos_guardados:
    if dispositivo["estado"] == "Activo":
        activos_json += 1
    else:
        inactivos_json += 1

print("-------------------------")
print("Resumen de dispositivos desde JSON")
print("Dispositivos activos:", activos_json)
print("Dispositivos inactivos:", inactivos_json)    





