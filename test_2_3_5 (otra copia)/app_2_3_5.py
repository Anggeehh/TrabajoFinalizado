# Importamos la función para manejar plantillas
import sqlite3
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def ver_coleccion():
    # 1. Conectamos con el archivo de la base de datos
    conexion = sqlite3.connect("productos.db")
    
    # 2. Configuramos la conexión para que devuelva diccionarios (más fácil para Jinja2)
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    
    # 3. Ejecutamos la consulta SQL
    cursor.execute("SELECT * FROM productos")
    
    # 4. Guardamos todos los resultados en una variable
    datos = cursor.fetchall()
    
    # 5. Cerramos la conexión
    conexion.close()
    
    # 6. Enviamos los datos reales a la plantilla
    return render_template("indexgrupal.HTML", items=datos)

if __name__ == "__main__":
   
    app.run(debug=True) 