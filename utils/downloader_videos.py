import urllib.request

class Downloader:
    def __init__(self):
        pass

    def download_video(self, video_url, output_filename='video.mp4'):
        """
        Baixa um vídeo da internet usando a URL fornecida.

        Parâmetros:
        - video_url: URL do vídeo a ser baixado.
        - output_filename: Nome do arquivo de vídeo baixado (por padrão, 'video.mp4').

        Retorna:
        - Nome do arquivo de vídeo baixado.
        """
        print(f"Baixando vídeo de {video_url}...")
        
        try:
            # Faz o download do vídeo para o caminho especificado
            urllib.request.urlretrieve(video_url, output_filename)
            
            print(f"Vídeo baixado e salvo como: {output_filename}")
            return output_filename
        
        except Exception as e:
            print(f"Erro ao baixar o vídeo: {e}")
            return None

if __name__ == '__main__':
    downloader = Downloader()
    
    # Exemplo de uso: baixar um vídeo do YouTube
    video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # URL de exemplo
    output_filename = 'rick_astley_never_gonna_give_you_up.mp4'  # Nome do arquivo de saída
    
    downloader.download_video(video_url, output_filename)
