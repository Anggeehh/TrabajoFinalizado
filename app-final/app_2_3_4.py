# Importamos la función para manejar plantillas
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/coleccion")
def ver_coleccion():
    # Creamos una lista de diccionarios con datos de prueba
    mis_favoritos = [
        {"nombre": "Eladio Carrion", "categoria": "Musica"},
        {"nombre": "Futbol", "categoria": "Deportes"},
        {"nombre": "Rocket League", "categoria": "Videojuegos"},
    ]
    # Enviamos la lista completa a la plantilla con el nombre 'favoritos'
    return render_template("galeria.html", favoritos=mis_favoritos)

if __name__ == "__main__":
   
    app.run(debug=True) 