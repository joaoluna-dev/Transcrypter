#Tenta importar os módulos utilizados pelo script atual. Caso algum esteja ausente, o usuário é instado a baixar as biliotecas necessárias
try:
    from pydub import AudioSegment
    import os
    import sys
    import subprocess
    import json
    from pathlib import Path
    from vosk import Model, KaldiRecognizer, SetLogLevel
except ModuleNotFoundError:
    print("Transcrypter - Módulos necessários para o audio_transcriptor.py: pydub, os, sys, subprocess, pathlib e vosk")
    print("Transcrypter - Instalação: pip install pydub, os, sys, subprocess, pathlib e vosk")

#------------------------------------------------------------------------------------------------------------------------#

def convert_mp3_to_wav(mp3file):
    """
    :param mp3file: nome do arquivo .mp3 que será convertido em .wav
    :return: arquivo .wav
    """
    print("Transcrypter - Convertendo áudio de .mp3 para .wav...")
    sound = AudioSegment.from_mp3(mp3file)
    return sound

def set_sound(sound):
    """
    :param sound: arquivo de áudio .wav original
    :return: arquivo de áudio .wav com canal e frame rate configurados, para melhor eficiência do vosk
    """
    print("Transcrypter - Ajustando canais e frequência do áudio...")
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(16000)
    return sound

def transcript_audio_segment(audio_segment, model_path):
    """
    :param audio_segment: arquivo de áudio .wav configurado com canais e frame rate ideais
    :param model_path: caminho do modelo
    :return: a transcrição do áudio completa
    """
    #Verifica novamente se o modelo está presente
    if not os.path.exists(model_path):
        print(f"Transcrypter - Modelo vosk não encontrado em: '{model_path}'.")
        print(f"Transcrypter - Baixe o modelo e coloque-o no diretório {model_path}.")
        sys.exit(1)

    #Inicializa o modelo
    print("Transcrypter - Inicializando modelo...")
    model = Model(model_path)
    full_text = []

    #Segmenta o áudio em pedaços menores (chunks) com no máximo 10 minutos, para facilitar a transcrição. Depois inicializa a trancrição de cada segmento. Após o término, a transcrição de cada segmento é salva na lista full_text.
    total_ms = len(audio_segment)
    segment_ms = 600_000
    for start_ms in range(0, total_ms, segment_ms):
        end_ms = min(start_ms + segment_ms, total_ms)
        chunk = audio_segment[start_ms:end_ms]

        rec = KaldiRecognizer(model, audio_segment.frame_rate)
        rec.SetWords(True)

        print(f"Transcrypter - Transcrevendo segmento {start_ms / 1000 / 60:.1f}–{end_ms / 1000 / 60:.1f} min…")
        data = chunk.raw_data
        for i in range(0, len(data), 4000):
            rec.AcceptWaveform(data[i:i + 4000])

        result = json.loads(rec.FinalResult())
        full_text.append(result.get("text", ""))

    #Retorna o áudio unido em uma única string
    return " ".join(full_text)

#-------------------------------------------------------------------------------------------------------------------#
#Verifica se os argumentos foram passados corretamente (arquivo python, opção do tipo de áudio (mp3 ou wav) e caminho do arquivo de áudio)
if len(sys.argv) != 3:
    print("Transcrypter - Uso: python video_transcriptor.py option filename")
    sys.exit(1)

#Diretórios usados pelo script
root = os.path.dirname(os.path.abspath(__file__))
audios = os.path.join(root, "audios")
transcriptions = os.path.join(root, "transcriptions")
resumes = os.path.join(root, "annotations")
videos = os.path.join(root, "videos")

#Obtém a opção do tipo de áudio selecionado (mp3 ou wav) e o caminho do arquivo de áudio
file_type = sys.argv[1]
file_name = sys.argv[2]

#Cria os arquivos que serão necessários
filename = os.path.splitext(Path(file_name).name)[0] #Obtém o nome do arquivo de áudio, sem o caminho e a extensão
wav_path = os.path.join(audios, f"{filename}.wav") #Cria o arquivo .wav, que é utilizado pelo vosk. Caso o arquivo de origem seja um mp3, ele será convertido em wav, que será escrito aqui
txt_path = os.path.join(transcriptions, f"{filename}.txt") #Cria o arquivo de texto no qual será escrita a transcrição do áudio
modelpath = os.path.join(root, "vosk-model-small-pt-0.3") #Passa o caminho do modelo Vosk, utilizado para fazer a transcrição

#Caso o o modelo vosk pt-br não exista no diretório
if not os.path.exists(modelpath):
    print("Transcrypter - Modelo de transcrição não localizado. Baixe-o em https://alphacephei.com/vosk/models e extraia seu conteúdo na pasta root")
    sys.exit(1)
#-------------------------------------------------------------------------------------------------------------------------#
#Caso o arquivo de origem seja um .mp3, ele será passado para a função convert_mp3_to_wav(), onde será convertido em .wav, logo após, a função de configuração set_sound() receberá o arquivo .wav criado para definir a frequência e o canal de som ideais para o modelo vosk trabalhar
if file_type == "1":
    wavfile = convert_mp3_to_wav(file_name)
    correct_sound = set_sound(wavfile)
    text = transcript_audio_segment(correct_sound, modelpath)

#Caso o arquivo de origem seja um .wav, ele será passado diretamente para a função de configuração set_sound(), para definir a frequência e o canal de som ideais para o modelo vosk trabalhar
elif file_type == "2":
    wav = AudioSegment.from_file(os.path.join(audios, file_name))
    correct_sound = set_sound(wav)
    text = transcript_audio_segment(correct_sound, modelpath)

#Detecta arquivos de áudio inválidos
else:
    print(f"Transcrypter - Opção file_type inválida: {file_type}.")
    sys.exit(1)

#Após a execução da função de conversão de áudio em texto Transcript_audio_segment(), a transcrição obtida será escrita no arquivo .txt criado anteriormente
print(f"Transcrypter - Salvando transcrição em: {txt_path}")
with open(txt_path, "w+", encoding='utf-8') as transcription:
    transcription.write(text)

#Faz a chamada do script responsável pelo resumo da transcrição criada, passando o arquivo da transcrição em .txt e o nome do arquivo original de áudio
print("Transcrypter - Iniciando processo de resumo...")
subprocess.run(["python", "resume_model.py", txt_path, filename])


