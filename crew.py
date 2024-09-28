# crew.py
from crewai import Agent, Task, Crew
from tool import generate_and_execute_sql_query

# Definir el agente encargado de la extracción de datos
data_extractor_agent = Agent(
    role='Agente Extractor de Datos',
    goal='Extraer datos relevantes de la base de datos SQL para su posterior análisis.',
    backstory="""Eres un agente especializado en la extracción de datos.
    Tu función es obtener información de la base de datos que será utilizada para análisis y generación de reportes.""",
    tools=[generate_and_execute_sql_query],
    verbose=True
)

# Definir la tarea de extracción de datos
data_extraction_task = Task(
    description='Extraer datos de la base de datos SQL necesarios para análisis.',
    expected_output='Datos extraídos de las tablas relevantes, listos para ser limpiados y analizados.',
    agent=data_extractor_agent
)

# Crear el equipo (Crew)
crew = Crew(
    agents=[data_extractor_agent],
    tasks=[data_extraction_task],
    verbose=True
)

# Iniciar el proceso
result = crew.kickoff()
print(result)
