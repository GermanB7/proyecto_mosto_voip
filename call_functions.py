# -*- coding: utf-8 -*-

import sys
# Agrega la ruta donde se encuentra la librería Most VoIP.
# La carpeta que contiene "most" es: most_voip/python/src
sys.path.append("most_voip/python/src")

import threading
import pyaudio
import numpy as np

try:
    import keyboard
except Exception as ex:
    print "Keyboard library not available:", ex
    keyboard = None

def play_audio_local(file_path):
    """Simula la reproducción de un archivo de audio local."""
    print "Reproduciendo audio local:", file_path
    pass

def play_tone():
    """Genera y reproduce un tono de 1 kHz durante 1 segundo."""
    sample_rate = 44100
    duration = 1.0
    freq = 1000
    p = pyaudio.PyAudio()
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(2 * np.pi * freq * t)
    tone = (tone * 32767).astype(np.int16)
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, output=True)
    stream.write(tone.tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()

def setup_tone_hotkey():
    """Configura la tecla 's' para generar un tono en un hilo separado."""
    if keyboard is None:
        print "Keyboard hotkey no configurado, ya que no se pudo importar keyboard."
        return
    try:
        keyboard.on_press_key('s', lambda e: threading.Thread(target=play_tone, daemon=True).start())
    except Exception as e:
        print "Error al configurar hotkey:", e

def make_call(ip_address, username, password, destination):
    print "Realizando llamada SIP:"
    print "  Servidor SIP:", ip_address
    print "  Usuario:", username
    print "  Destino:", destination

    from most.voip.api import VoipLib
    import pjsua as pj

    # Aseguramos que exista la instancia de la librería pjsua,
    # y configuramos los dispositivos de audio a -1 para deshabilitarlos.
    try:
        # Si no existe una instancia, la creamos.
        if not pj.Lib.instance():
            pj.Lib()
        pj.Lib.instance().set_snd_dev(-1, -1)
    except Exception as e:
        print "No se pudo desactivar el dispositivo de audio:", e

    voip_params = {
        u'username': username,
        u'sip_server_address': ip_address,
        u'sip_server_user': username,
        u'sip_server_pwd': password,
        u'sip_server_transport': u'udp',
        u'log_level': 5,
        u'debug': True
    }

    voip_lib = VoipLib()

    def notify_events(voip_event_type, voip_event, params):
        print "MOST VOIP EVENT: %s -> %s, Params: %s" % (voip_event_type, voip_event, params)

    init_ok = voip_lib.init_lib(voip_params, notify_events)
    if not init_ok:
        print "Error al inicializar la librería VoIP"
        return False

    reg_ok = voip_lib.register_account()
    if not reg_ok:
        print "Error al registrar la cuenta SIP"
        return False

    call_ok = voip_lib.make_call(destination)
    if not call_ok:
        print "Error al realizar la llamada"
        return False

    return True

