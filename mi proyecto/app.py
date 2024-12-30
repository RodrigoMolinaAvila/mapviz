from flask import Flask, render_template, send_from_directory
import os

# Crea la aplicación Flask
app = Flask(__name__)

# Ruta base del proyecto
BASE_PATH = r"C:\Users\Rodrigo\Desktop\Roxana Files\plots\mi proyecto"

# Ruta principal para renderizar el HTML
@app.route("/")
def index():
    return render_template("index.html")

# Ruta para servir los iconos de las banderas
@app.route("/static/ico/<filename>")
def serve_icons(filename):
    icon_path = os.path.join(BASE_PATH, "static", "ico")
    return send_from_directory(icon_path, filename)

# Ruta para servir el archivo custom.geo.json
@app.route("/static/<filename>")
def serve_geojson(filename):
    static_path = os.path.join(BASE_PATH, "static")
    return send_from_directory(static_path, filename)

if __name__ == "__main__":
    # Configura Flask para que busque las plantillas y archivos estáticos en tu ruta base
    app.template_folder = os.path.join(BASE_PATH, "templates")
    app.static_folder = os.path.join(BASE_PATH, "static")

    # Ejecuta el servidor Flask
    app.run(debug=True)
