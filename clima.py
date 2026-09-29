import requests

def buscar_ciudad(nombre):
    """Busca una ciudad y regresa su nombre, país, latitud y longitud."""
    url = "https://geocoding-api.open-meteo.com/v1/search"
    parametros = {"name": nombre, "count": 1, "language": "es"}


    respuesta = requests.get(url, params=parametros, timeout=10)
    respuesta.raise_for_status()
    datos = respuesta.json()

    if "results" not in datos:
        return None

    ciudad = datos["results"][0]
    return {
        "nombre": ciudad["name"],
        "pais": ciudad["country"],
        "lat": ciudad["latitude"],
        "lon": ciudad["longitude"],
    }

def obtener_clima(lat, lon):
    """Pide el clima actual para unas coordenadas."""
    url = "https://api.open-meteo.com/v1/forecast"
    parametros = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m,relative_humidity_2m",
        "timezone": "auto",
    }

    respuesta = requests.get(url, params=parametros, timeout=10)
    respuesta.raise_for_status()
    datos = respuesta.json()
    actual = datos["current"]

    return {
        "temperatura": actual["temperature_2m"],
        "viento": actual["wind_speed_10m"],
        "humedad": actual["relative_humidity_2m"],
    }

def main():
    print("=== App del Clima ===")
    nombre = input("Escribe una ciudad: ").strip()

    if not nombre:
        print("No escribiste nada.")
        return

    try:
        ciudad = buscar_ciudad(nombre)

        if ciudad is None:
            print(f"No encontré la ciudad '{nombre}'. Revisa cómo la escribiste.")
            return

        clima = obtener_clima(ciudad["lat"], ciudad["lon"])

    except requests.exceptions.ConnectionError:
        print("No hay conexión a internet.")
        return
    except requests.exceptions.Timeout:
        print("El servicio tardó demasiado en responder. Intenta de nuevo.")
        return
    except requests.exceptions.RequestException:
        print("Ocurrió un error al consultar el servicio del clima.")
        return

    print(f"\nClima en {ciudad['nombre']}, {ciudad['pais']}")
    print(f"Temperatura: {clima['temperatura']} °C")
    print(f"Viento:      {clima['viento']} km/h")
    print(f"Humedad:     {clima['humedad']} %")


if __name__ == "__main__":
    main()