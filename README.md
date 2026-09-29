# App del Clima

Aplicación de consola en Python que muestra el clima actual de cualquier ciudad del mundo.

## Características
- Búsqueda de ciudades por nombre (geocodificación)
- Temperatura, viento y humedad en tiempo real
- Manejo de errores: ciudad inexistente, sin internet y servicio caído

## Tecnologías
- Python 3
- Librería `requests`
- APIs gratuitas de [Open-Meteo](https://open-meteo.com/) (no requieren llave)

## Cómo usarla
```bash
git clone https://github.com/juan-ML22/clima-app.git
cd clima-app
pip install -r requirements.txt
python clima.py
```

## Ejemplo
```
=== App del Clima ===
Escribe una ciudad: Guadalajara

Clima en Guadalajara, México
Temperatura: 25.7 °C
Viento:      11.0 km/h
Humedad:     54 %
```

## Próximos pasos
- [ ] Pronóstico de varios días
- [ ] Interfaz web con HTML y CSS

## Autor
Juan Luis Medina Leal, estudiante de ITC en el Tecnológico de Monterrey.