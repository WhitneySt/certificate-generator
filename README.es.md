# Generador de Certificados

*Lea esto en otros idiomas: [English](README.md)*

Una herramienta automatizada en Python para generar certificados personalizados a partir de datos en Excel utilizando plantillas personalizables.

## 🌟 Características

- Generación masiva de certificados desde hojas de Excel
- Plantillas de certificados personalizables
- Formato de salida en PDF
- Estilos y posicionamiento de texto configurables
- Personalización de fuentes con soporte para variantes de Roboto Mono
- Sistema detallado de registro de eventos
- Manejo y validación de errores

## 📋 Prerequisitos

- Python 3.x
- pip (Instalador de paquetes de Python)

## 🔧 Instalación

1. Clona el repositorio:
```bash
git clone https://your-repository-url/certificate-generator.git
cd certificate-generator
```

2. Crea un entorno virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias requeridas:
```bash
pip install -r requirements.txt
```

## 📁 Estructura del Proyecto

```
certificate-generator/
├── certificados_generados/     # Directorio de salida para certificados generados
├── datos/
│   └── estudiantes.xlsx        # Archivo Excel con datos de estudiantes
├── fonts/
│   └── static/                 # Archivos de fuentes estáticas
│   └── *.ttf                   # Archivos de fuentes para el texto del certificado
├── plantillas/
│   └── plantilla.png           # Imagen de plantilla del certificado
├── generador_certificados.py   # Script principal
├── generador_certificados.log  # Archivo de registro
└── .gitignore
```

## ⚙️ Configuración

El generador de certificados puede configurarse a través de los siguientes ajustes en el script:

```python
self.estilos = {
    'nombre': {
        'fuente': 'RobotoMono-Bold.ttf',
        'tamanno': 50,
        'color': '#280384',
        'posicion_y': 250,
        'espaciado': -3
    },
    'identificacion': {
        'fuente': 'RobotoMono-Bold.ttf',
        'tamanno': 39,
        'color': '#280384',
        'posicion_y': 342,
        'posicion_x': 610,
        'espaciado': -3
    }
}
```

## 📝 Uso

1. Prepara tu archivo Excel (`estudiantes.xlsx`) con las siguientes columnas:
   - `nombre_completo`: Nombre completo del estudiante
   - `identificacion`: Número de identificación del estudiante

2. Coloca tu imagen de plantilla de certificado en la carpeta `plantillas`.

3. Ejecuta el script:
```bash
python generador_certificados.py
```

4. Los certificados generados se guardarán en la carpeta `certificados_generados`.

## 📊 Formato del Archivo Excel

Ejemplo de estructura para `estudiantes.xlsx`:

| nombre_completo | identificacion |
|----------------|----------------|
| Juan Pérez     | 12345678       |
| María García   | 87654321       |

## 🔍 Registro de Eventos

El script genera registros detallados en `generador_certificados.log`, incluyendo:
- Estado de generación de certificados
- Mensajes de error
- Información de finalización del proceso

## ⚠️ Manejo de Errores

El script incluye un manejo integral de errores para:
- Archivos o directorios faltantes
- Datos inválidos en Excel
- Problemas de carga de fuentes
- Errores en el procesamiento de imágenes

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! No dudes en enviar un Pull Request.

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

## 📫 Contacto

Para soporte o consultas, por favor abre un issue en el repositorio.

## 🙏 Agradecimientos

- Familia de fuentes Roboto Mono por Google Fonts
- PIL (Python Imaging Library) para el procesamiento de imágenes
- pandas para el manejo de datos Excel
- ReportLab para la generación de PDFs