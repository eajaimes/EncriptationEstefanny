from flask import Flask, Blueprint, render_template, request, jsonify, redirect, url_for
blueprint = Blueprint("main", __name__, template_folder="../../templates")
import numpy as np
import json
import sys
sys.path.append("src")  # Ajustar la ruta para que pueda encontrar src
from Encryption.EncryptionLogic import hill_cipher, hill_decipher, hill_genkey
from Database.Models.User import User
import Database.Controllers.UserController as UserController


@blueprint.route('/')
def index():
    return redirect(url_for('main.login'))

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.json.get('usuario')
        password = request.json.get('contrasena')
        try:
            if UserController.VerifyUserExistance(username):
                user = UserController.GetUserByUsername(username)
                if password == user.password:
                    return jsonify({'status': 'success', 'message': 'Inicio de sesión exitoso'})
                else:
                    return jsonify({'status': 'error', 'message': 'Contraseña incorrecta'})
            else:
                return jsonify({'status': 'error', 'message': 'Usuario no encontrado'})
        except UserController.ErrorNotFound:
            return jsonify({'status': 'error', 'message': 'Usuario no encontrado'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})
    return render_template('login.html')

@blueprint.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.json.get('usuario')
        password = request.json.get('contrasena')
        try:
            if not UserController.VerifyUserExistance(username):
                user = User(username, password, "")
                UserController.InsertIntoTable(user)
                return jsonify({'status': 'success', 'message': 'Usuario registrado exitosamente'})
            else:
                return jsonify({'status': 'error', 'message': 'El usuario ya existe'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})
    return jsonify({'status': 'error', 'message': 'Método de solicitud no válido'})

@blueprint.route('/generate_key', methods=['GET'])
def generate_key():
    try:
        size = int(request.args.get('size', 2))
        key = hill_genkey(size)
        key = key.tolist()
        return jsonify({'key': str(key)})
    except Exception as e:
        return jsonify({'error': str(e)})

@blueprint.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        input_text = request.json.get('texto')
        key_str = request.json.get('key')
        key = eval(key_str)
        if input_text and key:
            try:
                encrypted_text = hill_cipher(input_text, key)
                return jsonify({'texto_encriptado': encrypted_text})
            except Exception as e:
                return jsonify({'error': str(e)})
        else:
            return jsonify({'error': 'No se recibió el texto o la clave'})
    return render_template('index.html')

@blueprint.route('/decrypt', methods=['POST'])
def decrypt():
    if request.method == 'POST':
        input_text = request.json.get('texto')
        key = request.json.get('key')
        if input_text and key:
            try:
                key = eval(key)
                decrypted_text = hill_decipher(input_text, key)
                return jsonify({'texto_desencriptado': decrypted_text})
            except Exception as e:
                return jsonify({'error': str(e)})
        else:
            return jsonify({'error': 'No se recibió el texto o la clave'})
    return jsonify({'error': 'Método de solicitud no válido'})
