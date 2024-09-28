# crew_tuto
aprendiendo a usar CrewAI

Instrucciones para Usar el Código
Este proyecto permite extraer datos de una base de datos SQL utilizando agentes de CrewAI y LangChain. Está compuesto por dos archivos principales:

tool.py
crew.py
Requisitos Previos
Python 3.11 o superior.
Acceso a una base de datos MySQL con las credenciales correspondientes.
Claves API necesarias para los modelos de lenguaje (por ejemplo, OpenAI API Key).
Instalación de Dependencias
Las dependencias necesarias están listadas en el archivo requirements.txt. Para instalarlas, sigue estos pasos:

Abre una terminal en el directorio del proyecto.

Ejecuta el siguiente comando:

pip install -r requirements.txt

Archivos y Configuración
tool.py
"CAMBIALE EL PROMPT PARA QUE BUSQUE EN LA BASE LO QUE QUIERAS ESPECIFICAMENTE" COMO KEY DEL QUESTION
Este archivo contiene la función generate_and_execute_sql_query, que genera y ejecuta una consulta SQL basada en un prompt proporcionado. La función realiza lo siguiente:

Carga las variables de entorno (si es necesario).
Establece una conexión con la base de datos SQL.
Utiliza un modelo de lenguaje para generar una consulta SQL basada en una pregunta.
Ejecuta la consulta y devuelve los resultados.
Valores a Modificar en tool.py
Credenciales de la Base de Datos

Actualiza las siguientes variables con tus credenciales:


# Definir credenciales de la base de datos
db_user = "root"        # Cambia esto por tu usuario de la base de datos
db_password = "admin"   # Cambia esto por tu contraseña de la base de datos
db_host = "127.0.0.1"   # Cambia esto si tu base de datos está en otro host
db_name = "clientesdb"  # Cambia esto por el nombre de tu base de datos
Modelo de Lenguaje

Asegúrate de utilizar un modelo al que tengas acceso y que esté disponible en tu cuenta de OpenAI:

python
Copy code
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
Si usas una clave API, asegúrate de que esté configurada correctamente en tus variables de entorno o reemplaza os.getenv("OPENAI_API_KEY") con tu clave API directamente (no recomendado por seguridad).

Claves API y Variables de Entorno

Si utilizas variables de entorno para tus claves API u otras configuraciones, asegúrate de que estén definidas. Puedes crear un archivo .env en el directorio del proyecto:

makefile
Copy code
OPENAI_API_KEY=tu_clave_api_de_openai
crew.py
Este archivo define el agente y la tarea que utilizará la herramienta definida en tool.py. Realiza lo siguiente:

Importa la función generate_and_execute_sql_query desde tool.py.
Define un agente especializado en la extracción de datos.
Crea una tarea que utiliza el agente y la herramienta para extraer datos.
Inicia el proceso y muestra los resultados.
No es Necesario Modificar Valores en crew.py, a menos que quieras personalizar el agente o la tarea.
Cómo Ejecutar el Código
Sigue estos pasos para ejecutar el proyecto:

Configura las Credenciales y Claves API

Asegúrate de haber modificado tool.py con las credenciales de tu base de datos.
Configura tus claves API en un archivo .env o directamente en el código (no recomendado).
Instala las Dependencias

Ya realizado en pasos anteriores, pero si aún no lo has hecho:

pip install -r requirements.txt
Ejecuta el Script

En la terminal, ejecuta:

python crew.py YA QUE ES EL ENTRYPOINT D ELA APLICACION
Verifica los Resultados

El script mostrará en la consola los resultados de la consulta SQL generada y ejecutada.

Notas Importantes
Seguridad

No compartas tus credenciales o claves API en repositorios públicos. Es recomendable utilizar variables de entorno para almacenar información sensible.

Compatibilidad de Modelos

Base de Datos

La base de datos debe estar en funcionamiento y accesible desde tu máquina. Verifica que el puerto y el host sean correctos.

Manejo de Errores

Si encuentras errores al ejecutar el código, revisa los mensajes en la consola. Comúnmente, los errores pueden deberse a:

Credenciales incorrectas.
Base de datos inaccesible.
Claves API faltantes o incorrectas.
Versiones incompatibles de las librerías.
Personalización
Si deseas personalizar el comportamiento del agente o la consulta SQL, puedes:

Modificar el prompt proporcionado al modelo de lenguaje en tool.py.
Cambiar la descripción y los objetivos del agente en crew.py.
Agregar más herramientas o agentes según tus necesidades.
Contacto y Soporte
Si tienes preguntas o necesitas ayuda adicional, por favor contacta al mantenedor del proyecto o revisa la documentación de las librerías utilizadas:

LangChain Documentation
CrewAI Documentation
¡Disfruta explorando y utilizando este proyecto!