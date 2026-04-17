# 📊 Limpieza y Análisis de Datos: Gastos Hormiga

Este proyecto enfocado en la gestión de finanzas personales utiliza **Python** y **Pandas** para automatizar la limpieza y estandarización de registros de "gastos hormiga". El sistema procesa datos provenientes de múltiples fuentes (CSV y JSON) que presentan inconsistencias, errores de formato o valores nulos, transformándolos en información estructurada y útil para el análisis.

## 🎯 Objetivo del Proyecto
Desarrollar un flujo de trabajo (pipeline) de datos que permita:
* Cargar datos "crudos" con errores desde la carpeta `raw`.
* Limpiar inconsistencias (duplicados, fechas mal formateadas, valores vacíos).
* Exportar un dataset unificado y limpio para generar reportes financieros precisos.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.10+
* **Librerías principales:** * [Pandas](https://pandas.pydata.org/): Manipulación y análisis de estructuras de datos.
    * [JSON](https://docs.python.org/3/library/json.html): Manejo de formatos de intercambio de datos.

## 📁 Estructura del Repositorio
Siguiendo las convenciones de proyectos de ciencia de datos:

```text
├── data/
│   ├── raw/          # Archivos originales (CSV/JSON) con errores.
│   └── processed/    # Archivos finales limpios y listos para análisis.
├── src/              # Scripts de Python (.py) con la lógica de limpieza.
├── requirements.txt  # Lista de dependencias del proyecto.
└── README.md         # Documentación del proyecto.
🚀 Instalación y Configuración
Clonar el repositorio:

Bash
git clone https://github.com/camilaortiz07/ZentPandas.git
cd ZentPandas
Crear un entorno virtual (Recomendado):

Bash
python -m venv venv
# En Windows:
.\venv\Scripts\activate
Instalar las dependencias:

Bash
pip install -r requirements.txt
💻 Uso
Para ejecutar el proceso de limpieza, corre el script principal desde la terminal:

Bash
python src/main.py
📝 Notas de Implementación
El proyecto maneja errores de propiedad de directorio en entornos locales mediante configuraciones seguras de Git.

Se utiliza una arquitectura de separación de datos (Raw vs Processed) para garantizar la integridad de la fuente original.

Desarrollado como parte del aprendizaje en desarrollo de software y análisis de datos.
