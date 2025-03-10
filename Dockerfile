# Dockerfile
FROM python:2.7

# Instala dependencias del sistema (incluye portaudio para PyAudio, herramientas de compilación, etc.)
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    python-dev \
    wget \
    subversion

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos
COPY requirements.txt /app/

# Actualiza pip e instala las dependencias de Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# (Si necesitas compilar PJSIP y sus bindings, inserta aquí el proceso correspondiente)

# Si la Most VoIP Library no está en PyPI, se espera que la hayas clonado en el directorio "most_voip"
# Y puedes instalarla en modo editable (opcional) con:
# RUN pip install -e most_voip

# Copia el resto del proyecto en el contenedor
COPY . /app

# Comando por defecto para ejecutar la aplicación Flask
CMD ["python", "app.py"]
