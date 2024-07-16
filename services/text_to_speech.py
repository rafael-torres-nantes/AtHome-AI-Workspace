from gtts import gTTS
import os

class TextToSpeechService:
    def __init__(self):
        pass
    
    def set_language(self, language='pt-br'):
        """
        Define o idioma para o serviço de texto para fala.

        Parâmetros:
        - language: Código do idioma (padrão: 'pt-br' para Português Brasileiro).
        """
        self.language = language
    
    def set_rate(self, rate):
        """
        Define a taxa de fala.

        Parâmetros:
        - rate: Ajuste da taxa de fala (padrão: 1 para velocidade normal).
        """
        pass  # gTTS não suporta ajuste de velocidade diretamente
    
    def set_volume(self, volume):
        """
        Define o volume da fala.

        Parâmetros:
        - volume: Nível de volume (padrão: 1.0 para volume máximo).
        """
        pass  # gTTS não suporta ajuste de volume diretamente
    
    def speak(self, text, output_filename='output.mp3'):
        """
        Converte o texto em fala usando gTTS e salva como um arquivo de áudio.

        Parâmetros:
        - text: Texto para converter em fala.
        - output_filename: Nome do arquivo de saída para salvar o áudio (padrão: 'output.mp3').
        """
        tts = gTTS(text=text, lang=self.language, slow=False)
        tts.save(output_filename)
        print(f"Texto convertido para fala e salvo como {output_filename}")
        os.system(f"start {output_filename}")  # Abre o arquivo com o aplicativo padrão

if __name__ == "__main__":
    tts = TextToSpeechService()
    
    tts.set_language()  # Definido como Português Brasileiro ('pt-br')
    # Exemplo de configuração de velocidade e volume (não suportado diretamente por gTTS)
    
    text_to_speak = 'gTTS is a Python library and CLI tool to interface with Google Text-to-Speech (TTS) API. It has several features and supports multiple languages, including Brazilian Portuguese.'

    tts.speak(text_to_speak)
