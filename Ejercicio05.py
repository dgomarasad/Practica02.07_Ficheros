#Escribir un programa que abra el fichero con información sobre el PIB per 
#cápita de los países de la Unión Europea( https://ec.europa.eu/eurostat/
#estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.
#gz&unzip=true ), pregunte por las iniciales de un país y muestre el PIB
#per cápita de ese país de todos los años disponibles.
import urllib.request

def obtener_pib_pais():
    url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"
    archivo_local = "pib_europa.tsv"
    
    try:
        # Descargar el archivo y guardarlo localmente
        urllib.request.urlretrieve(url, archivo_local)
        
        # Leer el archivo descargado
        with open(archivo_local, "r", encoding="utf-8") as fichero:
            lineas = fichero.readlines()
        
        # Preguntar por las iniciales del país
        iniciales_pais = input("Introduce las iniciales del país (por ejemplo, 'DE' para Alemania): ").upper()
        
        # Buscar el país en el archivo
        encontrado = False
        for linea in lineas:
            if linea.startswith(iniciales_pais + "\t"):
                encontrado = True
                datos = linea.strip().split("\t")
                print(f"PIB per cápita de {iniciales_pais}:")
                print("\n".join(datos[1:]))
        
        if not encontrado:
            print(f"No se encontró información para el país con iniciales '{iniciales_pais}'.")
    
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

obtener_pib_pais()

