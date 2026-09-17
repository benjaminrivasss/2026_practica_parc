def separar_viento(campo_viento: str) -> tuple:
        """
    Interpreta el campo de viento 'Norte 3' como (dirección, velocidad) y maneja el caso especial 'Calma', sin velocidad numérica.
    """
        texto_limpio = campo_viento.strip()
        if texto_limpio.lower() == "calma":
            return ("Calma", 0.0)
    
        partes = texto_limpio.split()
    
        if len(partes) < 2:
            return (texto_limpio, 0.0)
    
        direccion = " ".join(partes[:-1])
        velocidad = float(partes[-1])
        return (direccion, velocidad)
#cambiar y rearmar para seguir la naturaleza de la consigna, se debe utilizar el parametro observaciones en cantidad_ciudades, para que quede consistente
def leer_observaciones(ruta: str) -> dict:
    """Lee el archivo de observaciones del SMN y devuelve un diccionario
    {ciudad: datos}, con los nombres de ciudad limpios y el campo de viento
    ya separado en dirección y velocidad."""
    with open(ruta, "r", encoding="UTF-8") as archivo:
        observaciones = {}
        ciudades_incompletas = 0
        for linea in archivo:
            linea_limpia = linea.strip()

            if not linea_limpia:
                continue

            campos = linea_limpia.split(";")

            if len(campos) != 10:
                ciudades_incompletas += 1
                continue

            ciudad = campos[0].strip()

            dir_viento, vel_viento = separar_viento(campos[8])

            st = campos[6].strip()
            if st.lower() != "no se calcula":
                st = float(st)

            observaciones[ciudad] = {
                "fecha": campos[1].strip(),
                "hora": campos[2].strip(),
                "condicion": campos[3].strip(),
                "visibilidad": campos[4].strip(),
                "temperatura": float(campos[5]),
                "sensacion_termica": st,
                "humedad": int(campos[7]),
                "direccion_viento": dir_viento,
                "velocidad_viento": vel_viento,
                "presion": float(campos[9].replace("/", "").strip())
            }
    return observaciones,ciudades_incompletas



def cantidad_ciudades(ruta: str) -> int:
    """Devuelve la cantidad total de ciudades leídas."""
    observaciones, ciudades_incompletas = leer_observaciones(ruta)
    
    cantidad = len(observaciones) + ciudades_incompletas
    print(cantidad)
    return cantidad
    

def cantidad_ciudades_completas(observaciones: dict) -> int:
    """Devuelve la cantidad de ciudades sin ningún dato faltante."""
    cantidad = len(observaciones) 
    print(cantidad)
    return cantidad
