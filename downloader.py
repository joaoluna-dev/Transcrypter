import sys
import os
import subprocess

#Tenta importar os módulos utilizados pelo script atual. Caso algum esteja ausente, o usuário é instado a baixar as biliotecas necessárias
try:
    import yt_dlp as yt
except ModuleNotFoundError:
    print("Transcrypter - Módulos necessários para o downloader.py: pytubefix")
    print("Transcrypter - Instalação: pip install pytubefix")
    sys.exit(1)

if len(sys.argv) != 3:
    print("Transcrypter - Uso: python video_transcriptor.py files_path root_path")
    sys.exit(1)

files_path = sys.argv[1] #Diretório root passado como argumento no main.py
root_path = sys.argv[2]
videos = os.path.join(files_path, "videos")

# Solicitação do link do YouTube ao usuário
while True:
    video_url = input("Transcrypter - Insira o link do vídeo: ")
    if len(video_url) == 0:
        print("Transcrypter - Por favor, insira um link de vídeo do youtube para continuar.")
        continue
    else:
        break

#Solicitação do navegador de preferência do usuário
#Esta opção é necessária para baixar vídeos com restrição de idade e região. \
#Estes dados não são armazenados no Transcrypter após o uso, apenas utilizados pelo yt-dpl para download de conteúdo da plataforma Youtube. \
#Para mais informações, acesse: https://github.com/yt-dlp/yt-dlp.
while True:
    supported_browsers = ['brave', 'chrome', 'chromium', 'edge', 'firefox', 'opera', 'safari', 'vivaldi', 'whale']
    browser = input("Transcrypter - Insira o nome do navegador de internet de preferência do seu computador. Você precisa estar logado em uma conta google neste navegador. (suportados: brave, chrome, chromium, edge, firefox, opera, safari, vivaldi, whale): ").lower()
    if len(browser) == 0:
        print("Transcrypter - Por favor, insira um nome de navegador para continuar.")
        continue
    if browser not in supported_browsers:
        print(f"Transcrypter - o navegador {browser} não é suportado pelo software. Insira outro")
    else:
        break


#Baixando o vídeo usando o yt-dlp
try:
    options = {
        'format': 'best', #O melhor formato para o vídeo, com áudio e vídeo unidos
        'paths': {'home': videos}, #Caminho para o vídeo, no diretório /videos
        'outtmpl': '%(title)s.%(ext)s', #Indica que o nome do arquivo deve ser o nome original do vídeo no YouTube, de extensão .mp4
        'quiet': True, #Não exibe mensagens no console do usuário
        'no_warnings': True, #Não exibe alertas de nível baixo, apenas erros graves
        'restrictfilenames': True, #Remove caracteres especiais do nome do arquivo


        'cookiesfrombrowser': (browser,)
        #Obtenção dos cookies do navegador do usuário para acessar o YouTube. Esta opção é necessária para baixar vídeos com restrição de idade e região. \
        #Estes dados não são armazenados no Transcrypter após o uso, apenas utilizados pelo yt-dpl para download de conteúdo da plataforma Youtube. \
        #Para mais informações, acesse: https://github.com/yt-dlp/yt-dlp.
    }

    with yt.YoutubeDL(options) as ydl:
        info = ydl.extract_info(video_url, download=True)
        mp4file = ydl.prepare_filename(info)

except Exception as e:
    print(f"Transcrypter - Um erro ocorreu durante o download do vídeo: {e}")
    sys.exit(1)

selection = input("Transcrypter - Você deseja transcrever o vídeo baixado? (y/n): ").lower()

if selection == "y":
    videos = os.path.join(files_path, "videos")
    mp4path = os.path.join(videos, mp4file)
    subprocess.run(["python", "video_transcriptor.py", mp4path, files_path], cwd=root_path)
elif selection == "n":
    sys.exit(1)
else:
    print(f"Transcrypter - Seleção inválida: {selection}")
    sys.exit(1)