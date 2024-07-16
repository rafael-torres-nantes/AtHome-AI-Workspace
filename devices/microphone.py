import sounddevice as sd
import numpy as np
import wave

class MicrophoneDevice:
    def __init__(self):
        # Lista os dispositivos de áudio disponíveis
        self.devices = sd.query_devices()
    
    def list_microphones(self):
        """
        Lista os dispositivos de entrada (microfones) disponíveis.
        """
        print("Lista de microfones disponíveis:")
        for idx, device in enumerate(self.devices):
            if device['max_input_channels'] > 0:
                print(f"{idx}: {device['name']}")
    
    def start_recording(self, duration=5, sample_rate=44100, channels=1, output_filename="output.wav"):
        """
        Inicia a gravação de áudio por uma duração especificada e salva o resultado em um arquivo WAV.

        Parâmetros:
        - duration: Duração da gravação em segundos.
        - sample_rate: Taxa de amostragem em Hz.
        - channels: Número de canais de áudio (1 para mono, 2 para estéreo).
        - output_filename: Nome do arquivo de saída para salvar a gravação.
        """
        print(f"Iniciando gravação por {duration} segundos...")
        
        # Função de callback para gravar áudio
        def callback(indata, frames, time, status):
            if status:
                print(status)
            audio_data.extend(indata.copy())
        
        # Cria uma lista para armazenar os dados de áudio
        audio_data = []

        try:
            # Inicia a gravação
            with sd.InputStream(callback=callback, channels=channels, samplerate=sample_rate):
                sd.sleep(int(duration * 1000))

            # Converte a lista de áudio para um array NumPy
            audio_array = np.array(audio_data)

            # Salva os dados de áudio em um arquivo WAV
            with wave.open(output_filename, 'w') as wf:
                wf.setnchannels(channels)
                wf.setsampwidth(2)  # 2 bytes por amostra
                wf.setframerate(sample_rate)
                wf.writeframes(audio_array.tobytes())
            
            print(f"Gravação salva em {output_filename}")

        except Exception as e:
            print(f"Erro durante a gravação: {e}")

if __name__ == "__main__":
    mic = MicrophoneDevice()
    mic.list_microphones()
    
    # Defina o índice do dispositivo de entrada, caso deseje usar um específico
    input_device_index = int(input("Digite o índice do microfone que deseja usar: "))
    
    # Ajuste as configurações de gravação conforme necessário
    mic.start_recording(duration=3, output_filename="output.wav")
