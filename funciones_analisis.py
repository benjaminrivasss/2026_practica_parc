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