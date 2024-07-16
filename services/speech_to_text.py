import whisper
import torch
import os
import sys

# Adicione o caminho para o diretório 'visao-computacional'
sys.path.append(os.path.abspath('./'))
from utils.function_timer import time_test

class ClassSpeechToText:
    def __init__(self, model_size='small'):
        """
        Inicializa o serviço de transcrição de fala para texto usando o modelo Whisper.

        Parâmetros:
        - model_size: Tamanho do modelo Whisper (padrão: 'small').
        """
        self.set_model(model_size)
    
    def set_model(self, model_size):
        """
        Define o modelo Whisper a ser utilizado.

        Parâmetros:
        - model_size: Tamanho do modelo Whisper ('tiny', 'base', 'small', 'medium', 'large').
        """
        self.model = whisper.load_model(model_size)
    
    def load_and_trim_audio(self, audio_filename):
        """
        Carrega e ajusta o áudio para caber em 30 segundos.

        Parâmetros:
        - audio_filename: Nome do arquivo de áudio a ser carregado.

        Retorna:
        - Áudio ajustado.
        """
        if not os.path.isfile(audio_filename):
            raise FileNotFoundError(f"O arquivo {audio_filename} não foi encontrado.")
        
        self.audio = whisper.load_audio(audio_filename)
        self.audio = whisper.pad_or_trim(self.audio)
        return self.audio

    def detect_language(self):
        """
        Detecta a linguagem falada no áudio.

        Parâmetros:
        - audio: Áudio ajustado.

        Retorna:
        - Linguagem detectada.
        """
        self.mel = whisper.log_mel_spectrogram(self.audio).to(self.model.device)
        _, probs = self.model.detect_language(self.mel)
        return max(probs, key=probs.get)

    def transcribe(self):
        """
        Decodifica o áudio.

        Parâmetros:
        - audio: Áudio ajustado.

        Retorna:
        - Texto reconhecido.
        """
        options = whisper.DecodingOptions()
        result = whisper.decode(self.model, self.mel, options)
        return result.text
        
    def save_transcription(self, text, output_filename='transcription.txt'):
        """
        Salva a transcrição em um arquivo de texto.

        Parâmetros:
        - text: Texto transcrito a ser salvo.
        - output_filename: Nome do arquivo de saída para salvar a transcrição (padrão: 'transcription.txt').
        """
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Transcrição salva como {output_filename}")



if __name__ == "__main__":
    audio_file = "output.wav"  # Substitua pelo caminho do seu arquivo de áudio

    stt = ClassSpeechToText(model_size='base')

    # Aplicando o decorador time_test nas funções que queremos medir
    load_and_trim_audio = time_test(stt.load_and_trim_audio)
    detect_language = time_test(stt.detect_language)
    transcribe = time_test(stt.transcribe)
    save_transcription = time_test(stt.save_transcription)

    audio = load_and_trim_audio(audio_file)
    language = detect_language()
    print(f"Linguagem detectada: {language}")

    transcription = transcribe()
    print(f"Transcrição: {transcription}")

    output_file = "transcription.txt"  # Substitua pelo nome desejado do arquivo de saída
    save_transcription(transcription, output_file)
