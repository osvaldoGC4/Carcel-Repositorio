class Utiles:

    def mostrar_resultados_dinamico(self, respuesta):
        if respuesta:  # Verificar si 'respuesta' tiene datos
            # Obtener las columnas de la primera fila de la respuesta
            columnas = respuesta[0].keys()

            # Mostrar encabezados dinámicos
            encabezado = " | ".join([f"{col:<20}" for col in columnas])
            print(encabezado)
            print("-" * len(encabezado))  # Línea separadora con longitud dinámica

            # Mostrar los valores de cada fila
            for row in respuesta:
                valores = " | ".join([f"{str(row[col]):<20}" for col in columnas])
                print(valores)
        else:
            print("No se encontraron datos.")