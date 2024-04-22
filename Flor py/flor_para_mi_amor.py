from turtle import * 
import colorsys

speed(15)          # Establece la velocidad de dibujo
bgcolor("black")   # Establece el color de fondo de la pantalla

h = 0              # Inicializa el valor de h para la generación de colores

# Ajusta el rango de i para completar un círculo
for i in range(22):                         # Realiza 72 iteraciones para completar un círculo de 360 grados
    for j in range(18):                     # Este bucle interno controla la cantidad de pétalos y su tamaño
        c = colorsys.hsv_to_rgb(h, 0.9, 1)  # Convierte el valor de h a un color RGB
        color(c)                            # Establece el color de la línea
        h += 0.005                          # Incrementa el valor de h para generar un nuevo color en la siguiente iteración
        rt(90)                              # Gira a la derecha 90 grados antes de dibujar
        circle(150 - j * 6, 90)             # Dibuja un arco de círculo con un radio y ángulo dados
        lt(90)                              # Gira a la izquierda 90 grados
        circle(150 - j * 6, 90)             # Dibuja otro arco de círculo
        rt(180)                             # Gira a la derecha 180 grados
        circle(7,11 )                      # Dibuja un pequeño arco de círculo para el centro de la flor 

        #Para cambiar la forma de la flor nesecitamos cambiar el valor de circle  24 que cambian 

# Llama a done() después de completar el dibujo del círculo
done()        # Finaliza el dibujo y cierra la ventana de Turtle