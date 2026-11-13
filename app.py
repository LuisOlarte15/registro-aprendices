import os
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "clave-local-de-prueba")

def conectar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "institucion"),
        port=int(os.getenv("DB_PORT", "3306"))
    )

@app.route("/")
def inicio():
    try:
        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre, correo FROM aprendices ORDER BY id DESC")
        aprendices = cursor.fetchall()
        cursor.close()
        conexion.close()
        return render_template("index.html", aprendices=aprendices)
    except Error as error:
        return render_template("index.html", aprendices=[], error_db=str(error)), 500

@app.route("/registrar", methods=["POST"])
def registrar():
    nombre = request.form.get("nombre", "").strip()
    correo = request.form.get("correo", "").strip()
    if not nombre or not correo:
        flash("Completa el nombre y el correo.", "error")
        return redirect(url_for("inicio"))
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO aprendices (nombre, correo) VALUES (%s, %s)",
            (nombre, correo)
        )
        conexion.commit()
        cursor.close()
        conexion.close()
        flash("Aprendiz registrado correctamente.", "success")
    except Error as error:
        flash(f"No se pudo registrar: {error}", "error")
    return redirect(url_for("inicio"))

@app.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM aprendices WHERE id = %s", (id,))
        conexion.commit()
        cursor.close()
        conexion.close()
        flash("Registro eliminado.", "success")
    except Error as error:
        flash(f"No se pudo eliminar: {error}", "error")
    return redirect(url_for("inicio"))

if __name__ == "__main__":
    app.run(debug=True)
