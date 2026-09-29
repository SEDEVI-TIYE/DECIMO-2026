import cv2
import os

# ----- CONFIGURACIÓN (solo cambia esto) -----
NOMBRE_IMAGEN = "radio1.jpg"   # tu imagen, en la misma carpeta que este script
ALTO_VENTANA = 700                  # más pequeño = ventanas más chicas
# --------------------------------------------

# Busca la imagen en la misma carpeta del script
carpeta = os.path.dirname(os.path.abspath(__file__))
ruta = os.path.join(carpeta, NOMBRE_IMAGEN)

img = cv2.imread(ruta)
if img is None:
    raise FileNotFoundError("No se encontró la imagen: " + ruta)


def mostrar(titulo, imagen):
    """Muestra la imagen en una ventana de tamaño razonable."""
    alto, ancho = imagen.shape[:2]
    escala = ALTO_VENTANA / alto
    if escala < 1:  # solo se reduce si la imagen es muy grande
        imagen = cv2.resize(imagen, (int(ancho * escala), int(alto * escala)))
    cv2.imshow(titulo, imagen)
    cv2.waitKey(0)  # presiona cualquier tecla para pasar a la siguiente


# 1. Original
mostrar("Original", img)

# 2. Escala de grises
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mostrar("Escala de grises", gris)

# 3. Suavizado (quita ruido)
suave = cv2.GaussianBlur(gris, (5, 5), 0)
mostrar("Suavizada", suave)

# 4. Bordes con Canny
bordes = cv2.Canny(suave, 50, 150)
mostrar("Bordes (Canny)", bordes)

# 5. Segmentación con Otsu
_, umbral = cv2.threshold(suave, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
mostrar("Segmentacion Otsu", umbral)

# 6. Original + bordes
bordes_color = cv2.cvtColor(bordes, cv2.COLOR_GRAY2BGR)
resultado = cv2.addWeighted(img, 0.7, bordes_color, 0.3, 0)
mostrar("Original + Bordes", resultado)

cv2.destroyAllWindows()