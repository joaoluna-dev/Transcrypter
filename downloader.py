import sys
import os
import subprocess

#Tenta importar os módulos utilizados pelo script atual. Caso algum esteja ausente, o usuário é instado a baixar as biliotecas necessárias
try:
    from pytubefix import YouTube
except ModuleNotFoundError:
    print("Transcrypter - Módulos necessários para o downloader.py: pytubefix")
    print("Transcrypter - Instalação: pip install pytubefix")
    sys.exit(1)

root_path = sys.argv[1] #Diretório root passado como argumento no main.py

# Solicita o link do usuário
video_url = input("Transcrypter - Insira o link do vídeo: ")

#Baixando o vídeo usando o pytubefix
try:
    yt = YouTube(video_url)
    title = yt.title
    # Obtém o material em maior resolução
    stream = yt.streams.get_highest_resolution()
    
    print(f"Transcrypter - Baixando: {title}...")
    stream.download(output_path="./videos") #Salva o vídeo no diretório videos
    print("Transcrypter - Download completo!")

except Exception as e:
    print(f"Transcrypter - Um erro ocorreu durante o download do vídeo: {e}")
    sys.exit(1)

selection = input("Transcrypter - Você deseja transcrever o vídeo baixado? (y/n): ").lower()

if selection == "y":
    mp4file = f"{title}.mp4"
    videos = os.path.join(root_path, "videos")
    mp4path = os.path.join(videos, mp4file)
    subprocess.run(["python", "video_transcriptor.py", mp4path], cwd=root_path)
elif selection == "n":
    sys.exit(1)
else:
    print(f"Transcrypter - Seleção inválida: {selection}")
    sys.exit(1)