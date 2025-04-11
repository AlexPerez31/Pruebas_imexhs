'''
Quise crear este archivo de prueba para inicializar el procesador como tal,
probar todo lo que pertenece a la clase, ajustar los parametros del
path, logger y diversos archivos a utilizar.
'''
from file_processor import FileProcessor

processor = FileProcessor(base_path="data", log_file="logs.txt")

# Esta es la funcion que hice para la prueba de lectura de archivos, carpetas y sus caracteristicas
print()
processor.list_folder_contents(folder_name="test_folder", details=True)

# Esta funcion lee el archivo csv proporcionado
print()
processor.read_csv(filename="sample-02-csv.csv", report_path="./reports", summary=True)

# Esta funcion lee alguno de los archivos DICOM proporcionado
print()
processor.read_dicom(
    filename="sample-02-dicom.dcm",
    tags=[(0x0010, 0x0010), (0x0008, 0x0060)],
    extract_image=True
)

# Una prueba para leer el segundo DICOM que si contiene un formato de imagen valido
print()
processor.read_dicom(
    filename="sample-02-dicom-2.dcm",
    tags=[(0x0010, 0x0010), (0x0008, 0x0060)],
    extract_image=True
)
