import os
from langchain_community.utilities import SQLDatabase
from dotenv import load_dotenv
from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_openai import ChatOpenAI
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain.tools import tool
load_dotenv()


@tool("Search in DB")
def generate_and_execute_sql_query():
    # Cargar variables de entorno
    """
    Esta herramienta genera una consulta SQL basada en un prompt proporcionado y la ejecuta en la base de datos.
    Retorna el resultado de la consulta.
    """



    # Definir credenciales de la base de datos
    db_user = "root"
    db_password = "admin"
    db_host = "127.0.0.1"
    db_name = "clientesdb"

    # Crear la conexión a la base de datos SQL
    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", sample_rows_in_table_info=5)
    
    # Imprimir información de la base de datos
    print('1111111111111111111111111111111111111111111111111111111111', db.dialect)
    print('22222222222222222222222222222222222222222222222222222222222', db.get_usable_table_names())
    print('333333333333333333333333333333333333333333333333333333333333', db.table_info)

    # Crear el LLM y generar la consulta SQL
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    generate_query = create_sql_query_chain(llm, db)
    

    #template
    #Genera una consulta SQL que recupere todos los campos de las tablas `calls`, `customers`, `agents`, `campaigns`, `transcripts`, `analysis_results`, `buyer_personas`, `reports` y `agent_personas`, uniendo adecuadamente las tablas según sus relaciones para preparar los datos para análisis y generación de reportes.

    query = generate_query.invoke({"question": "dame toda la informacion de maria"})
    
    # Imprimir la consulta generada
    print('444444444444444444444444444444444444444444444444444444444444', query)

    # Eliminar las comillas invertidas (```) del final de la consulta si existen
    query = query.replace('SQLQuery: ', '').strip('`')

    # Ejecutar la consulta SQL
    execute_query = QuerySQLDataBaseTool(db=db)
    result = execute_query.invoke(query)
    
    # Imprimir el resultado de la consulta
    print(result)
    
    return result