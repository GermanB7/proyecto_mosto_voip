# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, session, redirect, jsonify
from call_functions import make_call, setup_tone_hotkey

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia por una clave segura

# Variables globales para configuración SIP (se completarán en el formulario)
sip_user = ""
sip_pass = ""
sip_address = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/make_call', methods=['POST'])
def make_call_route():
    global sip_user, sip_pass, sip_address
    sip_address = request.form.get('ip_address')
    sip_user = request.form.get('username')
    sip_pass = request.form.get('password')
    destination = request.form.get('destination')
    
    try:
        call_status = make_call(sip_address, sip_user, sip_pass, destination)
        if call_status:
            session['call_status'] = "Call initiated"
            return redirect('/call_status')
        else:
            return jsonify({'error': 'Call failed'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/call_status')
def call_status():
    status = session.get('call_status', "No status available")
    return render_template('call_status.html', call_status=status)

if __name__ == '__main__':
    # Configura la detección de tecla 's' para generar el tono.
    # Si no se encuentran dispositivos de teclado (lo cual es común en un contenedor),
    # se captura la excepción y se imprime un mensaje.
    try:
        setup_tone_hotkey()
    except Exception as ex:
        print "No se pudo configurar hotkey:", ex
    app.run(host="0.0.0.0", debug=True)
