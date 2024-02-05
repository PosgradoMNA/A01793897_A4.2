"""
El programa permite calcular las estadísticas descriptivas a partir de un archivo que
contiene una lista de números.
"""
import sys
import time
import statistics

# Creamos la función que nos permitirá calcular las estadísticas descriptivas de un archivo
def compute_statistics(filename):
    """
    Calcula estadísticas descriptivas a partir de un archivo que contiene una lista de números.

    Args:
        filename (str): Nombre del archivo que contiene los datos.

    Returns:
        None
    """
    try:
        with open(filename, 'r') as file:
            data = [float(line.strip()) for line in file.readlines()]

        if len(data) == 0:
            print("Error: El archivo está vacío.")
            return

        # Calculamos las estadísticas descriptivas
        count = len(data)
        mean = sum(data) / count
        median = statistics.median(data)
        mode = statistics.mode(data)
        stdev = statistics.stdev(data)
        variance = statistics.variance(data)

        with open('StatisticsResults.txt', 'w') as result_file:
            result_file.write(f"COUNT: {count}\n")
            result_file.write(f"MEAN: {mean}\n")
            result_file.write(f"MEDIAN: {median}\n")
            result_file.write(f"MODE: {mode}\n")
            result_file.write(f"SD: {stdev}\n")
            result_file.write(f"VARIANCE: {variance}\n")

        print("computeStatistics se ha ejecutado correctamente. \n "
              "Se guardaron los resultados en StatisticsResults.txt")

    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except ValueError:
        print("Error: Datos inválidos en el archivo.")
    #except Exception as e:
    #    print(f"Error inesperado: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Ejemplo de Uso: python computeStatistics.py fileWithData.txt")
    else:
        start_time = time.time()
        compute_statistics(sys.argv[1])
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Tiempo transcurrido: {elapsed_time} segundos")
