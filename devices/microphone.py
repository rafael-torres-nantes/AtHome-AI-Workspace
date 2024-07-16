import pyaudio
import wave
import numpy as np
import time

class MicrophoneDevice:
    def __init__(self):
        self.pa = pyaudio.PyAudio()
    
    def list_devices(self):
        """
        Lista dispositivos de entrada de audio disponíveis.
        """
        print("Lista de dispositivos de áudio disponíveis:")
        devices = []
        for i in range(self.pa.get_device_count()):
            dev = self.pa.get_device_info_by_index(i)
            if dev.get('maxInputChannels') > 0:
                devices.append(dev)
                print(f"{i}: {dev.get('name')}")
        return devices
    
    def start_recording(self, duration=5, sample_rate=44100, channels=1, output_filename="outputs/recording.wav", input_device_index=None):
        """
        Inicia a gravação de áudio por uma duração especificada e salva o resultado em um arquivo WAV.

        Parâmetros:
        - duration: Duração da gravação em segundos.
        - sample_rate: Taxa de amostragem em Hz.
        - channels: Número de canais de áudio (1 para mono, 2 para estéreo).
        - output_filename: Nome do arquivo de saída para salvar a gravação.
        """
        print(f"Iniciando gravação por {duration} segundos...")
        
        audio_data = []

        def callback(in_data, frame_count, time_info, status):
            audio_data.append(in_data)
            return (in_data, pyaudio.paContinue)
        
        try:
            stream = self.pa.open(format=pyaudio.paInt16,
                                  channels=channels,
                                  rate=sample_rate,
                                  input=True,
                                  input_device_index=input_device_index,
                                  frames_per_buffer=1024,
                                  stream_callback=callback)
            
            stream.start_stream()

            # Record for the specified duration
            start_time = time.time()
            while time.time() - start_time < duration:
                time.sleep(0.1)  # Let the stream callback continue to fill audio_data
            
            stream.stop_stream()
            stream.close()
            
            audio_array = np.hstack(audio_data)
            
            self.save_recording(audio_array, sample_rate, channels, output_filename)

        except Exception as e:
            print(f"Erro durante a gravação: {e}")

        finally:
            self.pa.terminate()

    def save_recording(self, audio_data, sample_rate, channels, output_filename):
        """
        Salva os dados de áudio gravados em um arquivo WAV.

        Parâmetros:
        - audio_data: Dados de áudio gravados.
        - sample_rate: Taxa de amostragem em Hz.
        - channels: Número de canais de áudio (1 para mono, 2 para estéreo).
        - output_filename: Nome do arquivo de saída para salvar a gravação.
        """
        with wave.open(output_filename, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(self.pa.get_sample_size(pyaudio.paInt16))
            wf.setframerate(sample_rate)
            wf.writeframes(audio_data.tobytes())
        
        print(f"Gravação salva em {output_filename}")


if __name__ == "__main__":
    mic = MicrophoneDevice()
    mic.list_devices()
    
    input_device_index = int(input("Digite o índice do dispositivo de entrada que deseja usar: "))
    
    mic.start_recording(duration=10, output_filename="output.wav", input_device_index=input_device_index)
