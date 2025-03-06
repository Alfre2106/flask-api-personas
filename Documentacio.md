Documentación de la API - Lista de Personas
Descripción
Esta API ha sido desarrollada utilizando el framework Flask en Python. Su propósito es proporcionar un endpoint que devuelve una lista de nombres de personas en formato JSON.
Instalación y Configuración
Requisitos previos:
•	Python 3 instalado en el sistema.
•	Entorno virtual de Python.
•	Flask instalado.
Pasos de instalación:
1.	Clonar el repositorio desde GitHub: 
2.	git clone <URL_DEL_REPOSITORIO>
3.	cd <NOMBRE_DEL_REPOSITORIO>
4.	Crear y activar un entorno virtual (opcional pero recomendado): 
5.	python -m venv venv
6.	venv\Scripts\activate
7.	Instalar las dependencias necesarias: 
8.	pip install flask




Uso de la API
Iniciar el servidor
Ejecuta el siguiente comando para iniciar la aplicación:
python nombre_del_archivo.py
Por defecto, Flask ejecutará el servidor en http://127.0.0.1:5000/.
Endpoints disponibles
GET /personas
Descripción: Retorna una lista de nombres de personas en formato JSON.
Ejemplo de solicitud:
curl http://127.0.0.1:5000/personas
Ejemplo de respuesta:
{
    "personas": [
        "Alfredo",
        "Miguel",
        "Carlos",
        "Daniela",
        "Alberto",
        "Luisa"
    ]
}


Pruebas con Postman
1.	Abre Postman.
2.	Crea una nueva solicitud de tipo GET.
3.	Introduce la URL http://127.0.0.1:5000/personas.
4.	Haz clic en "Enviar" y verifica la respuesta JSON.


Despliegue en GitHub
Una vez completado el desarrollo, sube el proyecto a un repositorio público en GitHub:
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <URL_DEL_REPOSITORIO>
git push -u origin main

Autor
Alfredo Mercado Leal – Alfre2106(GitHub)
http://127.0.0.1:5000/personas  (url del flask)

