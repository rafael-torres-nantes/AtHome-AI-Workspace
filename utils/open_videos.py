import cv2

def readVideoFile(video_path):
    """
    Abre um arquivo de vídeo e armazena os frames em uma lista.

    Parâmetros:
    - video_path: Caminho para o arquivo de vídeo a ser aberto.
    
    Retorna:
    - frames: Lista contendo todos os frames do vídeo.
    """
    print(f"Abrindo vídeo em {video_path}...")
    
    # Verifica a extensão do arquivo para determinar o codec correto
    video_extension = video_path.split('.')[-1]
    if video_extension not in ['avi', 'mp4', 'mov']:
        raise ValueError(f"Formato de vídeo não suportado: {video_extension}")
    
    # Inicializa a captura de vídeo com o arquivo especificado
    cap = cv2.VideoCapture(video_path)
    
    # Verifica se o vídeo foi aberto corretamente
    if not cap.isOpened():
        raise RuntimeError("Não foi possível abrir o vídeo.")
    
    # Lista para armazenar os frames do vídeo
    frames = []
    
    # Loop para ler todos os frames do vídeo
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Adiciona o frame à lista
        frames.append(frame)
        
        # Exibe o frame (opcional)
        cv2.imshow('Video', frame)
        
        # Pressione 'q' para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    print(f"Vídeo em {video_path} foi completamente lido. Total de frames: {len(frames)}")
    
    return frames

def unitTesting_readVideoFile(video_path='Jojo - Meme.mp4'):
    
    # Exemplo de uso: abrir um vídeo e armazenar os frames
    try:
        video_frames = readVideoFile(video_path)
        # Agora video_frames contém uma lista de frames do seu vídeo
        print(f"Total de frames no vídeo: {len(video_frames)}")
    except Exception as e:
        print(f"Erro ao ler o vídeo: {e}")

if __name__ == '__main__':
    unitTesting_readVideoFile('teste.mp4')
