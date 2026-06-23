# Goalscorers Dashboard

Aplicacion web creada con Streamlit para explorar un conjunto de datos historico de goles en partidos internacionales.

## Funcionalidades

- Vista previa del dataset.
- Metricas generales de goles, goleadores y selecciones.
- Histograma interactivo de goles por minuto.
- Grafico de barras con los goleadores mas frecuentes.

## Como ejecutar el proyecto localmente

1. Crea y activa un entorno virtual.
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicacion:

```bash
streamlit run app.py
```

## Despliegue en Render

Usa el siguiente comando de inicio:

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```
