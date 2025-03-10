# Proyecto MOST VoIP en Python 2

Esta solución implementa una aplicación SIP usando la Most VoIP Library en Python 2.7, integrada en una aplicación Flask. La solución permite:
- Iniciar una llamada SIP (simulada en este ejemplo) mediante un formulario web.
- Reproducir audio local (lógica simulada o a implementar).
- Detectar la tecla "s" para generar un tono de 1 kHz (esta funcionalidad se omite en Docker debido a restricciones de acceso a dispositivos).

## Estructura del Proyecto

proyecto_most_voip/ ├── Dockerfile ├── requirements.txt ├── app.py ├── call_functions.py ├── most_voip/ <-- Código clonado de la Most VoIP Library (si se usa) ├── templates/ │ ├── index.html │ └── call_status.html └── README.md

markdown
Copiar

## Requisitos Previos

- **Docker** instalado en tu máquina.
- Una instancia EC2 configurada con Docker y un grupo de seguridad que permita el puerto 5000.

## Construcción y Ejecución

### En Local

1. Construir la imagen:
   ```bash
   sudo docker build -t proyecto_py2 .
Ejecutar el contenedor (publicando el puerto 5000):
bash
Copiar
sudo docker run --rm -it -p 5000:5000 proyecto_py2
Despliegue en EC2
Opción A: Usar Docker Hub
Subir la imagen a Docker Hub:

bash
Copiar
sudo docker tag proyecto_py2 tu_usuario/proyecto_py2:latest
sudo docker push tu_usuario/proyecto_py2:latest
En EC2, tirar la imagen y correr el contenedor:

bash
Copiar
sudo docker pull tu_usuario/proyecto_py2:latest
sudo docker run --rm -d -p 5000:5000 tu_usuario/proyecto_py2:latest
Opción B: Transferir la Imagen Directamente
Exportar la imagen:

bash
Copiar
sudo docker save proyecto_py2 > proyecto_py2.tar
Transferir a EC2:

bash
Copiar
scp -i /ruta/a/tu-llave.pem proyecto_py2.tar ubuntu@<IP-EC2>:/home/ubuntu/
En EC2, cargar y correr la imagen:

bash
Copiar
sudo docker load < proyecto_py2.tar
sudo docker run --rm -d -p 5000:5000 proyecto_py2
Funcionalidades Implementadas
Interfaz Web:
La aplicación Flask muestra un formulario para ingresar la IP del servidor SIP, usuario, contraseña y destino.

Llamada SIP:
La función make_call simula la realización de una llamada SIP (puedes reemplazarla con la integración real de la Most VoIP Library).

Reproducción de Audio:
La función play_audio_local simula la reproducción de un archivo de audio.
(Implementación real pendiente, en función de las necesidades y entorno de audio)

Detección de Tecla "s":
Se intenta configurar la librería keyboard para generar un tono de 1 kHz. En entornos Docker, esta funcionalidad se deshabilita (se imprime un mensaje de error) debido a restricciones en el acceso a dispositivos de teclado.

Limitaciones y Próximos Pasos
Funcionalidad de Hotkey:
Debido a restricciones del entorno Docker, la detección de teclas no funciona. En un entorno con acceso a dispositivos de entrada, esta funcionalidad se implementaría correctamente.

Integración SIP Real:
La función make_call está simulada. La integración completa usando la Most VoIP Library requerirá inicializar la librería, registrar la cuenta SIP y realizar la llamada real.

Producción:
La aplicación usa el servidor de desarrollo de Flask, lo que no es recomendable para producción. Se sugiere usar un WSGI server (por ejemplo, gunicorn) para entornos productivos.

Conclusión
Esta solución demuestra el flujo principal:

Interfaz web para iniciar una llamada SIP.
Lógica para reproducir audio y detectar la tecla "s" (con limitaciones en Docker).
Documentación de las dificultades encontradas y pasos a seguir para una versión completa.