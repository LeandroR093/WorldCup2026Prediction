import pandas as pd
import logging
import os

# Configuramos el registro de eventos (logs)
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def download_historical_matches():
    """
    Descarga el dataset de resultados internacionales históricos,
    filtra desde el año 2000 y lo guarda en la carpeta local 'data/raw'.
    """
    url = "https://raw.githubusercontent.com/martj42/international_results/master/results.csv"
    output_path = "data/raw/historical_results.csv"
    
    try:
        logging.info("Conectando a la fuente de datos...")
        df = pd.read_csv(url)
        logging.info(f"Dataset original descargado: {len(df)} partidos encontrados.")
        
        # Filtramos para quedarnos con datos modernos (año 2000 en adelante)
        df['date'] = pd.to_datetime(df['date'])
        df_filtered = df[df['date'].dt.year >= 2000]
        
        # Guardamos el archivo
        df_filtered.to_csv(output_path, index=False)
        logging.info(f"Éxito: {len(df_filtered)} partidos guardados en '{output_path}'.")
        
    except Exception as e:
        logging.error(f"Error al descargar los datos: {e}")

if __name__ == "__main__":
    download_historical_matches()