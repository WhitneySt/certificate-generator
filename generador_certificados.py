import os
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
from reportlab.pdfgen import canvas
import logging
from datetime import datetime

class GeneradorCertificados:
    def __init__(self, ruta_excel, ruta_plantilla, carpeta_salida, carpeta_fuentes='fonts'):
        """
        Inicializa el generador de certificados.
        
        Args:
            ruta_excel (str): Ruta al archivo Excel con los datos
            ruta_plantilla (str): Ruta a la imagen de la plantilla
            carpeta_salida (str): Carpeta donde se guardarán los certificados
            carpeta_fuentes (str): Carpeta donde están las fuentes TTF
        """
        self.ruta_excel = ruta_excel
        self.ruta_plantilla = ruta_plantilla
        self.carpeta_salida = carpeta_salida
        self.carpeta_fuentes = carpeta_fuentes
        
         # Configuración de estilos de texto con espaciado
        self.estilos = {
            'nombre': {
                'fuente': 'RobotoMono-Bold.ttf',
                'tamanno': 50,
                'color': '#280384',
                'posicion_y': 250,
                'espaciado': -3  # Espaciado negativo para juntar las letras
            },
            'identificacion': {
                'fuente': 'RobotoMono-Bold.ttf',
                'tamanno': 39,
                'color': '#280384',
                'posicion_y': 342,
                'posicion_x': 610,
                'espaciado': -3  # Espaciado negativo para juntar las letras
            }
        }
        
        self.configurar_logging()
        self.crear_carpetas()
        
    def configurar_logging(self):
        """Configura el sistema de logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('generador_certificados.log'),
                logging.StreamHandler()
            ]
        )

    def crear_carpetas(self):
        """Crea las carpetas necesarias si no existen"""
        for carpeta in ['certificados_generados', 'datos', 'plantillas', 'fonts']:
            if not os.path.exists(carpeta):
                os.makedirs(carpeta)
                logging.info(f'Carpeta creada: {carpeta}')

    def obtener_ruta_fuente(self, nombre_fuente):
        """
        Obtiene la ruta completa de una fuente.
        
        Args:
            nombre_fuente (str): Nombre del archivo de la fuente
            
        Returns:
            str: Ruta completa a la fuente
        """
        ruta_fuente = os.path.join(self.carpeta_fuentes, nombre_fuente)
        
        if not os.path.exists(ruta_fuente):
            logging.warning(f'Fuente {nombre_fuente} no encontrada, usando Arial como respaldo')
            return "arial.ttf"
        
        return ruta_fuente

    def cargar_fuente(self, nombre_fuente, tamanno):
        """
        Carga una fuente con el tamaño especificado.
        
        Args:
            nombre_fuente (str): Nombre del archivo de la fuente
            tamanno (int): Tamaño de la fuente
            
        Returns:
            ImageFont: Objeto fuente cargado
        """
        try:
            ruta_fuente = self.obtener_ruta_fuente(nombre_fuente)
            return ImageFont.truetype(ruta_fuente, tamanno)
        except Exception as e:
            logging.error(f'Error al cargar la fuente {nombre_fuente}: {str(e)}')
            logging.info('Usando fuente de sistema como respaldo')
            return ImageFont.load_default()

    def dibujar_texto(self, draw, texto, estilo, width, centrado=True):
        """
        Dibuja texto en la imagen con espaciado personalizado entre letras.
        """
        font = self.cargar_fuente(estilo['fuente'], estilo['tamanno'])
        espaciado = estilo.get('espaciado', 0)
        
        # Calcular el ancho total del texto con el espaciado
        ancho_total = 0
        for i, letra in enumerate(texto):
            bbox = draw.textbbox((0, 0), letra, font=font)
            ancho_letra = bbox[2] - bbox[0]
            if i < len(texto) - 1:
                ancho_total += ancho_letra + espaciado
            else:
                ancho_total += ancho_letra
        
        # Calcular posición inicial
        if centrado:
            posicion_x = (width - ancho_total) // 2
        else:
            posicion_x = estilo.get('posicion_x', 0)
        
        # Dibujar cada letra con el espaciado ajustado
        x_actual = posicion_x
        for letra in texto:
            # Obtener el ancho de la letra actual
            bbox = draw.textbbox((0, 0), letra, font=font)
            ancho_letra = bbox[2] - bbox[0]
            
            # Dibujar la letra
            draw.text(
                (x_actual, estilo['posicion_y']),
                letra,
                font=font,
                fill=estilo['color']
            )
            
            # Mover la posición x para la siguiente letra
            x_actual += ancho_letra + espaciado

    def ajustar_espaciado(self, elemento, espaciado):
        """
        Ajusta el espaciado entre letras para un elemento.
        
        Args:
            elemento (str): Nombre del elemento ('nombre' o 'identificacion')
            espaciado (int): Espaciado en píxeles (negativo para juntar, positivo para separar)
        """
        if elemento in self.estilos:
            self.estilos[elemento]['espaciado'] = espaciado
            logging.info(f'Espaciado de {elemento} ajustado a {espaciado}px')
            
    def generar_certificado(self, nombre, identificacion):
        """
        Genera un certificado individual.
        
        Args:
            nombre (str): Nombre completo del estudiante
            identificacion (str): Número de identificación
        """
        try:
            imagen = Image.open(self.ruta_plantilla)
            draw = ImageDraw.Draw(imagen)
            width, _ = imagen.size
            
            # Generar el nombre del archivo
            fecha_actual = datetime.now().strftime("%Y%m%d")
            nombre_archivo = f"{fecha_actual} {nombre.upper()}"
            
            # Dibujar nombre (centrado)
            self.dibujar_texto(draw, nombre, self.estilos['nombre'], width)
            
            # Dibujar identificación (posición específica)
            self.dibujar_texto(draw, identificacion, self.estilos['identificacion'], width, centrado=False)
            
            # Guardar como imagen
            ruta_imagen = os.path.join(self.carpeta_salida, f'{nombre_archivo}.png')
            imagen.save(ruta_imagen)
            
            # Convertir a PDF
            ruta_pdf = os.path.join(self.carpeta_salida, f'{nombre_archivo}.pdf')
            self.convertir_a_pdf(ruta_imagen, ruta_pdf, imagen.size)
            
            logging.info(f'Certificado generado para {nombre} - {identificacion}')
            
            # Eliminar la imagen temporal PNG
            if os.path.exists(ruta_imagen):
                os.remove(ruta_imagen)
            
        except Exception as e:
            logging.error(f'Error al generar certificado para {nombre}: {str(e)}')
            raise

    def convertir_a_pdf(self, ruta_imagen, ruta_pdf, size):
        """
        Convierte una imagen a PDF.
        
        Args:
            ruta_imagen (str): Ruta de la imagen
            ruta_pdf (str): Ruta donde se guardará el PDF
            size (tuple): Tamaño de la imagen (ancho, alto)
        """
        try:
            c = canvas.Canvas(ruta_pdf, pagesize=size)
            c.drawImage(ruta_imagen, 0, 0, width=size[0], height=size[1])
            c.save()
        except Exception as e:
            logging.error(f'Error al convertir a PDF: {str(e)}')
            raise

    def generar_todos_los_certificados(self):
        """Genera certificados para todos los estudiantes en el archivo Excel"""
        try:
            df = self.cargar_datos()
            total = len(df)
            generados = 0
            errores = 0
            
            logging.info(f'Iniciando generación de {total} certificados')
            
            for _, row in df.iterrows():
                try:
                    self.generar_certificado(
                        nombre=row['nombre_completo'],
                        identificacion=str(row['identificacion'])
                    )
                    generados += 1
                except Exception as e:
                    errores += 1
                    logging.error(f'Error en certificado {row["identificacion"]}: {str(e)}')
                    continue
            
            logging.info(f'Proceso completado: {generados} generados, {errores} errores')
            
        except Exception as e:
            logging.error(f'Error en el proceso de generación: {str(e)}')
            raise

    def cargar_datos(self):
        """
        Carga los datos desde el archivo Excel.
        
        Returns:
            pandas.DataFrame: DataFrame con los datos de los estudiantes
        """
        try:
            return pd.read_excel(self.ruta_excel)
        except Exception as e:
            logging.error(f'Error al cargar el archivo Excel: {str(e)}')
            raise

def main():
    """Función principal"""
    try:
        generador = GeneradorCertificados(
            ruta_excel='datos/estudiantes.xlsx',
            ruta_plantilla='plantillas/plantilla.png',
            carpeta_salida='certificados_generados'
        )
        generador.generar_todos_los_certificados()
        
    except Exception as e:
        logging.error(f'Error en la ejecución principal: {str(e)}')

if __name__ == '__main__':
    main()