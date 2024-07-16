import cv2
from pygrabber.dshow_graph import FilterGraph

class ClassWebcamDevice:
    def __init__(self):
        pass

    def list_webcams(self):
        """
        Lista todas as webcams disponíveis.
        """
        available_cameras = FilterGraph().get_input_devices()

        cameras = {}
        for device_index, device_name in enumerate(available_cameras):
            cameras[device_index] = device_name

        for index, device_name in cameras.items():
            print(f'{index} : Webcam ({device_name})')

        return cameras

    def start_recording(self, camera_index=0, output_filename="output.avi"):
        """
        Inicia a gravação da webcam específica pelo índice e salva o resultado em um arquivo de vídeo.

        Parâmetros:
        - camera_index: Índice da câmera a ser utilizada.
        - output_filename: Nome do arquivo de saída para salvar a gravação.
        """
        print(f"Iniciando gravação da webcam {camera_index}...")
        
        # Inicializa a captura de vídeo com a câmera especificada pelo índice
        cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
        
        # Verifica se a câmera foi aberta corretamente
        if not cap.isOpened():
            raise RuntimeError("Não foi possível abrir a câmera. Verifique se está conectada corretamente.")
        
        # Define o codec de vídeo e cria o objeto para gravar o vídeo
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(output_filename, fourcc, 20.0, (640, 480))
        
        # Loop principal para capturar e gravar os frames da câmera
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Exemplo de processamento: escrever o frame no arquivo de saída
            out.write(frame)

            # Exibir o frame
            cv2.imshow('Camera', frame)

            # Pressione 'q' para sair do loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        
        print(f"Gravação da webcam {camera_index} salva em {output_filename}")

    def open_camera(self, camera_index=0):
        """
        Abre a câmera específica pelo índice sem iniciar a gravação.

        Parâmetros:
        - camera_index: Índice da câmera a ser utilizada.
        """
        print(f"Abrindo câmera {camera_index}...")

        cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
        if not cap.isOpened():
            raise RuntimeError("Não foi possível abrir a câmera. Verifique se está conectada corretamente.")

        # Configuração do tamanho da tela da webcam
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # Largura personalizada
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Altura personalizada

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Exibir o frame
            cv2.imshow('Camera', frame)

            # Pressione 'q' para sair do loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        
        print(f"A câmera {camera_index} foi fechada!!")

if __name__ == '__main__':
    webcam_device = ClassWebcamDevice()
    webcam_device.list_webcams()
    # Inicia gravação da câmera escolhida pelo usuário
        
    camera_index = int(input("Digite o índice da webcam que deseja usar: "))
    webcam_device.open_camera(camera_index=camera_index)
