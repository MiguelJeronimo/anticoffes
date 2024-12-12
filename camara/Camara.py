class Camara:
    def __init__(self, camera, cv2):
        self.camera = camera
        self.cv2 = cv2

    def capture(self, name):
        # Verifica si la cámara está abierta
        if not self.camera.isOpened():
            print("No se puede acceder a la cámara.")
            exit()
        # Leer un frame de la cámara
        ret, frame = self.camera.read()
        # Verifica si se obtuvo la imagen correctamente
        if ret:
            # Muestra la imagen capturada en una ventana
            self.cv2.imshow('Imagen capturada', frame)
            # Guarda la imagen en el disco
            self.cv2.imwrite(f'{name}.jpg', frame)
            print(f"Foto guardada como '{name}.jpg'")
        else:
            print("Error al capturar la imagen.")

    def close(self):
        # Espera a que el usuario presione una tecla y luego cierra la ventana
        print("precione la tecla para salir....")
        self.cv2.destroyAllWindows()
        # Libera la cámara
        self.camera.release()