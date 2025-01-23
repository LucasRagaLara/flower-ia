
# Averigua tu tipo de flor con mi IA de flores

Es una página web realizada con Flask y una plantilla básica de HTML y JavaScript.

Tienes 4 campos a rellenar, tras rellenarlos y pulsar en el botón, la ia detectará a través de esos campos de que flor se trata.

## Installation

Para instalar el proyecto, revisad el fichero requirements.txt e instalar con pip. 
Es necesario contar con una versión reciente de Python y tener pip instalado.

```bash
    pip install -r requirements.txt
```

Si lo preferís, también puedes instalar las librerias de forma individual:

```bash
    pip install tensorflow
    pip install numpy
    pip install scikit-learn
    pip install flask
```

## Deployment

Para desplegar el proyecto una vez descargado, tan solo tienes ejecutar el siguiente comando desde la carpeta principal:

```bash
  python app.py
```

Se desplegará en: http://127.0.0.1:3000

## Documentation

Para los estilos se ha utilizado Tailwind, a través de su cdn.

Podéis obtener más información de cómo usarla en su página oficial.

https://tailwindcss.com/docs/installation/play-cdn

## Running Training model

Si deseas entrenar la IA o generar un nuevo modelo, asegúrate de instalar las siguientes librerías:

```bash
  pip install tensorflow
  pip install scikit-learn
  pip install matplotlib
  pip install numpy
```

## Recomendation

Se recomienda crear un entorno virtual antes de instalar las dependencias:

```bash
python -m venv venv

source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate     # En Windows
```

## Authors

- [@Lucas Raga](https://github.com/LucasRagaLara/flower-ia)
