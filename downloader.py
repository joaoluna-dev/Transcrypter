import sys
import os
import subprocess

#Tenta importar os módulos utilizados pelo script atual. Caso algum esteja ausente, o usuário é instado a baixar as biliotecas necessárias
try:
    import yt_dlp as yt
except ModuleNotFoundError:
    print("SummaVox - Módulos necessários para o downloader.py: pytubefix")
    print("SummaVox - Instalação: pip install pytubefix")
    sys.exit(1)

if len(sys.argv) != 3:
    print("SummaVox - Uso: python video_transcriptor.py files_path root_path")
    sys.exit(1)

files_path = sys.argv[1] #Diretório root passado como argumento no main.py
root_path = sys.argv[2]
videos = os.path.join(files_path, "videos")

# Solicitação do link do YouTube ao usuário
while True:
    print("SummaVox - Você deve obter autorização do autor do vídeo para poder baixar-lo. Não nos responsabilizamos por violações de direitos autorais cometidas por usuários.")
    video_url = input("SummaVox - Insira o link do vídeo: ")
    if len(video_url) == 0:
        print("SummaVox - Por favor, insira um link de vídeo do youtube para continuar.")
        continue
    else:
        break

#Baixando o vídeo usando o yt-dlp
try:
    options = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', #O melhor formato para o vídeo, que baixa audio e videos separados, e une posteriormente.
        'paths': {'home': videos}, #Caminho para o vídeo, no diretório /videos
        'outtmpl': '%(title)s.%(ext)s', #Indica que o nome do arquivo deve ser o nome original do vídeo no YouTube, de extensão .mp4
        'quiet': True, #Não exibe mensagens no console do usuário
        'no_warnings': True, #Não exibe alertas de nível baixo, apenas erros graves
        'restrictfilenames': True, #Remove caracteres especiais do nome do arquivo

        'extractor_args': {
        'youtube': {
            'player_client': ['android', 'web'] #Simula que o pedido vem de um app Android ou Web player legítimo
            }
        },

        'retries': 10, #Tenta novamente o download 10 vezes se der erro durante à conexão
        'fragment_retries': 10, #Tenta novamente o download 10 vezes se ele falhar num pedaço específico do video
        'socket_timeout': 30 #Espera 30s antes de retornar um Time out, em caso de conexões lentas.
    }

    with yt.YoutubeDL(options) as ydl:
        info = ydl.extract_info(video_url, download=True)
        mp4file = ydl.prepare_filename(info)

except Exception as e:
    e = str(e)
    if 'confirm your age' in e:
        print("SummaVox - Vídeo com restrição de idade detectado. Atualmente, o SummaVox não possui suporte à download direto de vídeos desta modalidade.")
        sys.exit(1)
    elif 'country' in e:
        print("SummaVox - Vídeo com restrição de região (geoblock) detectado. Atualmente, o SummaVox não possui suporte à download direto de vídeos desta modalidade.")
        sys.exit(1)
    elif 'This helps protect our community' in e:
        print("SummaVox - Proteção antibots detectada. Tente novamente em alguns minutos, ou use uma VPN.")
        sys.exit(1)
    elif "player responses are invalid" in e:
        print("SummaVox - Provável bloqueio de IP do usuário. Tente novamente em alguns minutos, ou use uma VPN.")
        sys.exit(1)
    elif "DRM" in e or "drm" in e:
        print("SummaVox - Vídeo com proteção anti-pirataria. Tente novamente com outro vídeo.")
        sys.exit(1)
    elif "truncated_id" in e:
        print("SummaVox - Vídeo com URL incompleta. Tente novamente.")
        sys.exit(1)
    elif "unavailable" in e:
        print("SummaVox - Vídeo indisponível. Cheque o link inserido e tente novamente.")
        sys.exit(1)
    elif "HTTP error" in e:
        if "404" in e:
            print("SummaVox - Vídeo não encontrado. Tente novamente com outro vídeo.")
            sys.exit(1)
        if "403" in e:
            print("SummaVox - Acesso negado. Tente novamente mais tarde, em outro dispositivo, ou utilizando uma VPN.")
            sys.exit(1)
        if "502" in e or "503" in e or "504" in e:
            print("SummaVox - Erro de servidor. Tente novamente mais tarde, em outro dispositivo, ou utilizando uma VPN.")
            sys.exit(1)
        else:
            print(f"SummaVox - Erro desconhecido durante a requisição: {e}.")
            sys.exit(1)
    else:
        print(f"SummaVox - Um erro desconhecido ocorreu durante o download do vídeo: {e}")
        sys.exit(1)

selection = input("SummaVox - Você deseja transcrever o vídeo baixado? (y/n): ").lower()

if selection == "y":
    videos = os.path.join(files_path, "videos")
    mp4path = os.path.join(videos, mp4file)
    subprocess.run(["python", "video_transcriptor.py", mp4path, files_path], cwd=root_path)
elif selection == "n":
    sys.exit(1)
else:
    print(f"SummaVox - Seleção inválida: {selection}")

    sys.exit(1)