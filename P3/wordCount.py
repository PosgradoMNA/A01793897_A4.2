"""
Programa que cuenta la frecuencia con las que aparece una
palabra en un archivo de texto
"""
import sys
import os
import time

def count_words(filename):
    """
    Cuenta la frecuencia de palabras distintas en un archivo.

    Args:
        filename (str): Nombre del arcchivo que contiene las palabras.

    Returns:
        None
    """
    try:
        # Extraemos el nombre del archivo sin la extensión
        filename_column_name = os.path.splitext(filename)[0]

        with open(filename, 'r') as file:
            words = file.read().split()

        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        sorted_word_count = sorted(word_count.items(), key=lambda x: x[0])

        with open('WordCountResults.txt', 'w') as result_file:
            result_file.write(f"Row\tLabels\tCount of {filename_column_name}\n")
            for i, (word, count) in enumerate(sorted_word_count, start=1):
                result_file.write(f"{i}\t{word}\t{count}\n")

        total_count = sum(count for _, count in sorted_word_count)
        with open('WordCountResults.txt', 'a') as result_file:
            result_file.write(f"Grand Total\t\t{total_count}\n")

        print("wordCount se ha ejecutado correctamente. \n"
              "Se guardaron los resultados en WordCountResults.txt")

    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except ValueError:
        print("Error: Datos inválidos en el archivo.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Ejemplo de Uso: python wordCount.py fileWithData.txt")
    else:
        start_time = time.time()
        count_words(sys.argv[1])
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Tiempo transcurrido: {elapsed_time} segundos")
