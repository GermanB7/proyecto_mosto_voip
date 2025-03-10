# -*- coding: utf-8 -*-
import threading
import pyaudio
import numpy as np

# Intentamos importar keyboard; si falla (por ejemplo, por falta de dispositivos), lo capturamos.
try:
    import keyboard
except Exception as ex:
    print "Keyboard library not available:", ex

def play_audio_local(file_path):
    """Simula la reproducción de un archivo de audio local."""
    print "Reproduciendo audio local:", file_path
    # Aquí podrías implementar la reproducción real usando PyAudio y wave.
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
    try:
        keyboard.on_press_key('s', lambda e: threading.Thread(target=play_tone, daemon=True).start())
    except Exception as e:
        print "Error al configurar hotkey:", e

def make_call(ip_address, username, password, destination):
    """
    Simula la realización de una llamada SIP.
    En una implementación real, aquí se inicializaría la Most VoIP Library,
    se registraría la cuenta SIP y se invocaría la llamada real.
    """
    print "Realizando llamada SIP:"
    print "  Servidor SIP:", ip_address
    print "  Usuario:", username
    print "  Destino:", destination
    # Aquí integrarías la lógica real utilizando Most VoIP Library.
    # Por ejemplo:
    #   from most.voip.api import VoipLib
    #   voip_params = { ... }
    #   voip_lib = VoipLib()
    #   if voip_lib.init_lib(voip_params, notify_events):
    #       voip_lib.register_account()
    #       return voip_lib.make_call(destination)
    return True
