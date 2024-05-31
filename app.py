from flask import Flask, request, jsonify, url_for
from flask import render_template
import sys
sys.path.append("src")
from src.Gui.view_web import vista_usuarios

app = Flask(__name__)
app.register_blueprint(vista_usuarios.blueprint)

app.static_folder = 'static'

if __name__ == '__main__':
    app.run(debug=True)
