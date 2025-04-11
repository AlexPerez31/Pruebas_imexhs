import os
import logging
import datetime
import csv
import statistics
import pydicom
import matplotlib.pyplot as plt

class FileProcessor:
    def __init__(self, base_path: str, log_file: str):

        self.base_path = base_path

        # Aca configurto el logger que vamos a usar en toda la clase
        self.logger = logging.getLogger("FileProcessorLogger")
        self.logger.setLevel(logging.ERROR)

        # Esto es para evita agregar múltiples handlers si ya existen
        if not self.logger.handlers:
            handler = logging.FileHandler(log_file)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)


    def list_folder_contents(self, folder_name: str, details: bool = False) -> None:
        """
        Lista los contenidos de una carpeta dentro de test_folder con sus caracteristicas.
        """
        test_folder = os.path.join(self.base_path, folder_name)

        # Primero verifico si la carpeta existe
        if not os.path.exists(test_folder):
            # En dado caso de no existir registro el error en el log y tambien lo imprimo por consola
            self.logger.error(f"Carpeta no encontrada: {test_folder}") 
            print(f"Folder '{test_folder}' does not exist.")
            return

        files = []
        folders = []

        # Aca recorro todos los elementos dentro de la carpeta
        for item in os.listdir(test_folder):
            item_path = os.path.join(test_folder, item)
            # Si el elemento es un archivo lo agregue a la lista de archivos
            if os.path.isfile(item_path):
                files.append(item_path)
            # Si es una carpeta la agregue a la lista de carpetas
            elif os.path.isdir(item_path):
                folders.append(item_path)

        # Imprimi la ruta completa y número total de elementos encontrados
        print(f"\nFolder: {test_folder}")
        print(f"Number of elements: {len(files) + len(folders)}")

        # Iteré sobre los archivos encontrados
        if files:
            print("Files:")
            for file in files:
                # Obtuve el nombre del archivo
                name = os.path.basename(file)
                # Aca me asegure de que se quieran obtener los detalles
                if details:
                    # Tamaño del archivo en MB
                    size_mb = os.path.getsize(file) / (1024 * 1024)
                    # Fecha de última modificación del archivo
                    mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d %H:%M:%S')
                    print(f"  - {name} ({size_mb:.2f} MB, Last Modified: {mod_time})")
                else:
                    print(f"  - {name}")
        
        # Iteré sobre carpetas encontradas
        if folders:
            print("Folders:")
            for folder in folders:
                name = os.path.basename(folder)

                if details:
                    mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(folder)).strftime('%Y-%m-%d %H:%M:%S')
                    print(f"  - {name} (Last Modified: {mod_time})")
                else:
                    print(f"  - {name}")


    def read_csv(self, filename, report_path=None, summary=False):
        """
        Esta funcion lee el archivo CSV desde base_path, imprime estadísticas numéricas y guarda un reporte.
        """
        csv_path = os.path.join(self.base_path, filename)

        # Primero verifiqué si el archivo existe en esa ruta, de lo contrario se registra el error en el log
        if not os.path.exists(csv_path):
            self.logger.error(f"Archivo CSV no encontrado: {csv_path}")
            print(f"File '{csv_path}' does not exist.")  
            return

        try:
            # Aca abrí el archivo CSV en modo lectura
            with open(csv_path, newline='', encoding='utf-8') as csvfile:
                # Usé csv.DictReader para leer el contenido como una lista de diccionarios
                # y convertí el lector en una lista para poder procesar sus datos
                reader = csv.DictReader(csvfile)
                rows = list(reader)  

            # Verifiqué si el archivo estaba vacío
            if not rows:
                print("The CSV file is empty.")
                self.logger.error(f"El archivo CSV esta vacio: {csv_path}")
                return

            # Obtuve los nombres de todas las columnas desde el encabezado del archivo y conte las filas
            columns = reader.fieldnames
            num_rows = len(rows)
            print("CSV Analysis:")
            print(f"Columns: {columns}")
            print(f"Rows: {num_rows}")

            # Aca guardare las columnas con datos numéricos
            numeric_stats = {} 
            # Aca guardare las columnas de texto, cuando se especica que summary es True
            non_numeric_summary = {}

            for col in columns:
                # Lista donde guardare los valores numéricos
                values = []
                is_numeric = True

                # Aca trato de definir cuales columnas son numericas convirtiendo sus valores a numerico
                for row in rows:
                    value = row[col]
                    try:
                        values.append(float(value))
                    except ValueError:
                        # Cuando no se puede convertir el valor asumo que no es numerica
                        is_numeric = False
                        break

                if is_numeric:
                    # Para las columnas numericas uso funciones que porporciona Python para desarrollar cada punto
                    avg = statistics.mean(values)  # Promedio
                    std = statistics.stdev(values) if len(values) > 1 else 0.0  # Desviación estándar
                    numeric_stats[col] = (round(avg, 2), round(std, 2))
                elif summary:
                    # Si no fue numérica y summary=True, solo conté los valores únicos como se pedia
                    unique_counts = {}
                    for row in rows:
                        val = row[col]
                        unique_counts[val] = unique_counts.get(val, 0) + 1
                    non_numeric_summary[col] = unique_counts

            if numeric_stats:
                print("Numeric Columns:")
                for col, (avg, std) in numeric_stats.items():
                    print(f"  - {col}: Average = {avg}, Std Dev = {std}")

            if summary and non_numeric_summary:
                print("Non-Numeric Summary:")
                for col, value_counts in non_numeric_summary.items():
                    print(f"  - {col}: Unique Values = {len(value_counts)}")

            # Para guardar el reporte cree una carpeta y el archivo a guardar
            if report_path:
                os.makedirs(report_path, exist_ok=True)
                report_file = os.path.join(report_path, f"{os.path.splitext(filename)[0]}_report.txt")

                # Use las funciones de python de lectura para escribir el reporte con todos los resultados en el archivo
                with open(report_file, 'w') as f:
                    f.write("CSV Analysis Report\n")
                    f.write(f"Columns: {columns}\n")
                    f.write(f"Rows: {num_rows}\n\n")
                    f.write("Numeric Columns:\n")
                    for col, (avg, std) in numeric_stats.items():
                        f.write(f"  - {col}: Average = {avg}, Std Dev = {std}\n")
                    if summary and non_numeric_summary:
                        f.write("\nNon-Numeric Summary:\n")
                        for col, value_counts in non_numeric_summary.items():
                            f.write(f"  - {col}: Unique Values = {len(value_counts)}\n")

                print(f"Saved summary report to {report_path}")

        except Exception as e:
            # En caso de errores inesperados los registro en el log
            self.logger.error(f"Error al procesar CSV: {e}")
            print(f"Failed to process CSV file: {e}")


    def read_dicom(self, filename, tags=None, extract_image=False):
        """
        Esta funcion es para leer los archivos DICOM, extraer los metadatos y en dado caso guardar PNG
        """
        dicom_path = os.path.join(self.base_path, filename)

        # Primero verifiqué si el archivo existe
        if not os.path.exists(dicom_path):
            self.logger.error(f"Archivo DICOM no encontrado: {dicom_path}")
            print(f"File '{dicom_path}' does not exist.")
            return

        try:
            # Instale pydicom para poder leer el archivo, de manera sencilla
            dicom = pydicom.dcmread(dicom_path)

            print("DICOM Analysis:")
            # Si existen los campos los imprimo con ayuda de las funciones que proporciona la libreria
            print(f"Patient Name: {getattr(dicom, 'PatientName', 'N/A')}")
            print(f"Study Date: {getattr(dicom, 'StudyDate', '')[:4]}-{getattr(dicom, 'StudyDate', '')[4:6]}-{getattr(dicom, 'StudyDate', '')[6:8]}" if getattr(dicom, 'StudyDate', '') else "Study Date: N/A")
            print(f"Modality: {getattr(dicom, 'Modality', 'N/A')}")

            # Si se pasaron tags personalizados, los imprimí también
            if tags:
                for tag in tags:
                    try:
                        element = dicom[tag]
                        print(f"Tag {hex(tag[0])}, {hex(tag[1])}: {element.value}")
                    except KeyError:
                        print(f"Tag {hex(tag[0])}, {hex(tag[1])}: Not Found")

            # Si se pidió extraer una imagen, lo hago de la sigueinte manera
            if extract_image:
                if 'PixelData' not in dicom:
                    print("No image data found in this DICOM file.")
                    return
                
                # Obtuve la imagen como un arreglo de píxeles y lo guardo en la misma carpeta path
                image = dicom.pixel_array
                '''
                Aca hago una verificacion de cuantas dimensiones tiene la imagen
                porque puede ser una imagen RGB con 3 dimenciones obtenidas o 
                una imagen en escala de grises con menos de 3 diamensiones
                '''
                output_file = os.path.join(self.base_path, f"{os.path.splitext(filename)[0]}.png")
                if image.ndim == 2:
                    # Imagen en escala de grises
                    plt.imsave(output_file, image, cmap='gray')
                elif image.ndim == 3 and image.shape[2] in [3, 4]:
                    # Imagen RGB o RGBA
                    plt.imsave(output_file, image)
                else:
                    print("Unsupported image format for saving.")
                    return
                print(f"Extracted image saved to {output_file}")

        except Exception as e:
            # Si ocurre un error inesperado lo registro en el log
            self.logger.error(f"Error al procesar DICOM: {e}")
            print(f"Failed to process DICOM file: {e}")