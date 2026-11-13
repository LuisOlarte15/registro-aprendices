# Registro de Aprendices — Flask + MySQL + Railway

## Ejecutar localmente
1. Instala Python 3.10+ y MySQL.
2. Crea una base de datos local llamada `institucion`.
3. Ejecuta `database.sql` en esa base de datos.
4. En terminal, dentro de la carpeta:
   ```bash
   python -m venv .venv
   .venv\\Scripts\\activate
   pip install -r requirements.txt
   python app.py
   ```
5. Abre http://127.0.0.1:5000

## Variables de entorno
La app lee `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` y `DB_PORT`.
En Railway, configura estas variables en el servicio Flask con referencias al servicio MySQL.

## Despliegue
Sube el contenido a un repositorio GitHub y en Railway crea un proyecto desde ese repositorio.
Añade un servicio MySQL, crea la tabla ejecutando `database.sql` en la base de datos de Railway,
configura las variables de entorno del servicio Flask y genera un dominio público.
No publiques contraseñas ni archivos `.env`.
