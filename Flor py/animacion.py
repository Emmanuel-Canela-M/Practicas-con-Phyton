import cv2
import numpy as np

salida = cv2.VideoWriter('videosalida.avi', cv2.VideoWriter_fourcc(*'MJPG'), 30, (1920, 720))

imagen = 255 * np.ones(shape=(720, 1280, 3), dtype=np.uint8)

#GRACIAS POR SER PARTE DE MI VIDA, TE AMO MI BEBE !
ge = cv2.imread('g.png')
filas_ge = ge.shape[0]
col_ge = ge.shape[1]

cv2.imshow('Imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

