# Certificate Generator

*Read this in other languages: [Español](README.es.md)*


An automated Python tool for generating personalized certificates from Excel data using customizable templates.

## 🌟 Features

- Bulk certificate generation from Excel spreadsheets
- Customizable certificate templates
- PDF output format
- Configurable text styles and positioning
- Font customization with support for Roboto Mono variants
- Detailed logging system
- Error handling and validation

## 📋 Prerequisites

- Python 3.x
- pip (Python package installer)

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://your-repository-url/certificate-generator.git
cd certificate-generator
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 📁 Project Structure

```
certificate-generator/
├── certificados_generados/     # Output directory for generated certificates
├── datos/
│   └── estudiantes.xlsx        # Input Excel file with student data
├── fonts/
│   └── static/                 # Static font files
│   └── *.ttf                   # Font files for certificate text
├── plantillas/
│   └── plantilla.png           # Certificate template image
├── generador_certificados.py   # Main script
├── generador_certificados.log  # Log file
└── .gitignore
```

## ⚙️ Configuration

The certificate generator can be configured through the following settings in the script:

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

## 📝 Usage

1. Prepare your Excel file (`estudiantes.xlsx`) with the following columns:
   - `nombre_completo`: Full name of the student
   - `identificacion`: Student ID or identification number

2. Place your certificate template image in the `plantillas` folder.

3. Run the script:
```bash
python generador_certificados.py
```

4. Generated certificates will be saved in the `certificados_generados` folder.

## 📊 Excel File Format

Example structure for `estudiantes.xlsx`:

| nombre_completo | identificacion |
|----------------|----------------|
| John Doe       | 12345678       |
| Jane Smith     | 87654321       |

## 🔍 Logging

The script generates detailed logs in `generador_certificados.log`, including:
- Certificate generation status
- Error messages
- Process completion information

## ⚠️ Error Handling

The script includes comprehensive error handling for:
- Missing files or directories
- Invalid Excel data
- Font loading issues
- Image processing errors

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📫 Contact

For support or queries, please open an issue in the repository.

## 🙏 Acknowledgments

- Roboto Mono font family by Google Fonts
- PIL (Python Imaging Library) for image processing
- pandas for Excel data handling
- ReportLab for PDF generation