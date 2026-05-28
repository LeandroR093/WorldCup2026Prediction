import boto3
import os
import logging
from botocore.exceptions import NoCredentialsError, ClientError
from dotenv import load_dotenv

# Cargamos las credenciales de forma segura desde el archivo .env
load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def upload_raw_to_s3(local_file: str, s3_file: str):
    """
    Sube un archivo local a un bucket de AWS S3 utilizando credenciales seguras.
    """
    bucket_name = os.getenv('S3_BUCKET_NAME')
    
    # Inicializamos el cliente de S3
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION')
    )

    try:
        logging.info(f"Iniciando subida de '{local_file}' a S3 (Bucket: {bucket_name})...")
        s3_client.upload_file(local_file, bucket_name, s3_file)
        logging.info(f"Éxito: Archivo subido correctamente a s3://{bucket_name}/{s3_file}")
        return True
        
    except FileNotFoundError:
        logging.error(f"Error: El archivo local '{local_file}' no existe.")
        return False
    except NoCredentialsError:
        logging.error("Error: No se encontraron las credenciales de AWS.")
        return False
    except ClientError as e:
        logging.error(f"Error de AWS: {e}")
        return False

if __name__ == "__main__":
    # Ruta de nuestro archivo local descargado en el paso anterior
    ARCHIVO_LOCAL = "data/raw/historical_results.csv"
    
    # Cómo queremos que se llame dentro de la carpeta raw/ en nuestro bucket
    ARCHIVO_DESTINO_S3 = "raw/historical_results.csv"
    
    upload_raw_to_s3(ARCHIVO_LOCAL, ARCHIVO_DESTINO_S3)