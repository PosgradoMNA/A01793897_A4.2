"""
Programa que convierte los números de un archivo a de binario y hexadecimal.
"""
import sys
import time
import os

def convert_numbers(filename):
    """
    Convierte los números de un archivo a su representación en binario y hexadecimal.

    Args:
        filename (str): Nombre del archivo que contiene los datos.

    Returns:
        None
    """
    try:
        # Extraemos el nombre del archivo sin la extensión
        filename_column_name = os.path.splitext(filename)[0]

        with open(filename, 'r') as file:
            data = [int(line.strip()) for line in file.readlines()]

        if len(data) == 0:
            print("Error: El archivo está vacío.")
            return

        binary_data = [bin(num)[2:] for num in data]
        hexadecimal_data = [hex(num)[2:].upper() for num in data]

        with open('ConvertionResults.txt', 'w') as result_file:

            result_file.write(f"NUMBER\t{filename_column_name}\tBIN\tHEX\n")
            for i, num in enumerate(data, start=1):
                result_file.write(f"{i}\t{num}\t{binary_data[i-1]}\t{hexadecimal_data[i-1]}\n")

        print("convertNumbers se ha ejecutado correctamente. \n"
              "Se guardaron los resultados en ConvertionResults.txt")

    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except ValueError:
        print("Error: Datos inválidos en el archivo.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Ejemplo de Uso: python convertNumbers.py fileWithData.txt")
    else:
        start_time = time.time()
        convert_numbers(sys.argv[1])
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Tiempo transcurrido: {elapsed_time} segundos")
