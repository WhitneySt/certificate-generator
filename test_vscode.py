def verificar_configuracion():
    """
    Función simple para verificar la configuración de VSCode con Python
    """
    try:
        # Importar bibliotecas necesarias
        import sys
        import PIL
        import pandas as pd
        import reportlab
        
        # Crear un diccionario con la información
        info = {
            "Python Version": sys.version.split()[0],
            "Pillow Version": PIL.__version__,
            "Pandas Version": pd.__version__,
            "ReportLab Version": reportlab.Version
        }
        
        # Imprimir información de configuración
        print("\n=== Configuración de VSCode y Python ===")
        for key, value in info.items():
            print(f"{key}: {value}")
            
        print("\n✅ ¡Todo está configurado correctamente!")
        
    except ImportError as e:
        print("\n❌ Error: Falta instalar algunas bibliotecas.")
        print(f"Error específico: {str(e)}")
        print("\nEjecuta el siguiente comando en la terminal:")
        print("pip install Pillow pandas openpyxl reportlab")

if __name__ == "__main__":
    verificar_configuracion()