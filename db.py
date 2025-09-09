import psycopg2
from psycopg2 import OperationalError

conn_str = "postgresql://neondb_owner:npg_i3WyNPMKJzn7@ep-proud-rice-ac2xu92h-pooler.sa-east-1.aws.neon.tech/banco_pystock?sslmode=require&channel_binding=require"


def get_connection():
    try:
        conn = psycopg2.connect(conn_str)
        return conn
    except OperationalError as e:
        print(f"Erro de conexão: {e}")
        return None
