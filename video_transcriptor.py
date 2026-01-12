import os
import sys
import subprocess
from pathlib import Path

#Tenta importar os módulos utilizados pelo script atual. Caso algum esteja ausente, o usuário é instado a baixar as biliotecas necessárias
try:
    from moviepy import VideoFileClip
except ModuleNotFoundError:
    print("Transcrypter - Módulos necessários para o video_transcriptor.py: moviepy, os, sys, subprocess, pathlib")
    print("Transcrypter - Instalação: pip install moviepy os sys subprocess pathlib")
    sys.exit(1)

#---------------------------------------------------------------------------------------#
#Verifica se os argumentos foram passados corretamente (arquivo python e caminho do arquivo de vídeo)
if len(sys.argv) != 3:
    print("Transcrypter - Uso: python video_transcriptor.py filename files_path ")
    sys.exit(1)

#Diretórios utilizados pelo programa
root = os.path.dirname(os.path.abspath(__file__))
files_path = sys.argv[2]
audios = os.path.join(files_path, "audios")
transcriptions = os.path.join(files_path, "raw_files")
resumes = os.path.join(files_path, "annotations")
videos = os.path.join(files_path, "videos")


mp4_path = sys.argv[1] #Obtém o caminho do arquivo de vídeo
mp4_filename = os.path.splitext(Path(mp4_path).name)[0] #Obtém apenas o nome do arquivo de vídeo, sem o caminho e a extensão .mp4

#----------------------------------------------------------------------------------------#

print(f"Transcrypter - Lendo arquivo de vídeo {mp4_filename}...")
mp4_file = VideoFileClip(mp4_path) #Passa o caminho do arquivo de vídeo desejado para a biblioteca moviepy, através de uma instância da classe VideoFileClip
mp3_file = os.path.join(audios, f"{mp4_filename}.mp3") #Cria o arquivo vazio .mp3, em que o áudio do vídeo será escrito. Possui o mesmo nome do arquivo de vídeo baixado

print("Transcrypter - Iniciando a conversão de vídeo em áudio...")
audio_clip = mp4_file.audio #Faz a conversão do vídeo em áudio
audio_clip.write_audiofile(mp3_file) #Escreve o áudio no arquivo .mp3 criado

subprocess.run(["python", "audio_transcriptor.py", "1", mp3_file, files_path], cwd=root) #Chama o script de transcrição de áudio em texto, passando o arquivo de áudio criado a partir do vídeo selecionado
