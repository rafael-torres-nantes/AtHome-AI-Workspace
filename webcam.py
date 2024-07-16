import cv2

class ClassWebcamDevice:
    def __init__(self):
        self.cameras = self.list_webcams()

    def list_webcams(self):
        # Listar todas as webcams disponíveis
        num_cameras = 0
        cameras = []
        while True:
            cap = cv2.VideoCapture(num_cameras)
            if not cap.isOpened():
                break
            else:
                cameras.append(f"Camera {num_cameras}")
                cap.release()
                num_cameras += 1
        return cameras

    def start_recording(self, camera_index=0):
        # Iniciar a gravação da webcam específica pelo índice
        if camera_index >= len(self.cameras):
            raise ValueError(f"Índice de câmera inválido. Apenas {len(self.cameras)} câmeras disponíveis.")

        cap = cv2.VideoCapture(camera_index)
        if not cap.isOpened():
            raise RuntimeError("Não foi possível abrir a câmera. Verifique se está conectada corretamente.")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Exemplo de processamento: exibir o frame
            cv2.imshow('Camera', frame)

            # Pressione 'q' para sair do loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    webcam_device = ClassWebcamDevice()

    print("Webcams Disponíveis:")
    for idx, cam in enumerate(webcam_device.cameras):
        print(f"{idx}: {cam}")

    # Iniciar gravação da primeira câmera encontrada
    if webcam_device.cameras:
        webcam_device.start_recording(0)
    else:
        print("Nenhuma câmera encontrada.")
