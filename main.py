import sys
import os
import subprocess
import json


def menu_select(option, root_path, _files_path_):
    """
    :param _files_path_:
    :param option: opção selecionada pelo usuário (download de vídeo, transcrição de vídeo e áudio).
    :param root_path: caminho do diretório root do software.
    :return: chamada do script responsável pela seleção do usuário.
    """
    env = os.environ.copy()
    if option == "1":
        print("Transcrypter - Arquivos no diretório de áudios: ")
        for file in os.listdir(audios):
            print(file)
        mp3file = input("Transcrypter - Insira o nome do arquivo .mp3: ")
        mp3path = os.path.join(audios, mp3file)
        subprocess.run(["python", "audio_transcriptor.py", "1", mp3path, _files_path_], cwd=root_path)
    elif option == "2":
        print("Transcrypter - Arquivos no diretório de áudios: ")
        for file in os.listdir(audios):
            print(file)
        wavfile = input("Transcrypter - Insira o nome do arquivo .wav: ")
        wavpath = os.path.join(audios, wavfile)
        subprocess.run(["python", "audio_transcriptor.py", "2", wavpath, _files_path_], cwd=root_path)
    elif option == "3":
        print("Transcrypter - Arquivos no diretório de vídeos: ")
        for file in os.listdir(audios):
            print(file)
        mp4file = input("Transcrypter - Insira o nome do arquivo .mp4: ")
        mp4path = os.path.join(audios, mp4file)
        subprocess.run(["python", "video_transcriptor.py", mp4path, _files_path_], cwd=root_path)
    elif option == "4":
        subprocess.run(["python", "downloader.py", _files_path_, root_path], cwd=root_path)
    else:
        print(f"Transcrypter - Opção inválida selecionada: {option}")
        sys.exit(1)

#---------------------------------------------------------------------------------------------------------------------------------"
#Diretório raiz
root = os.path.dirname(os.path.abspath(__file__))

#Verifica se o arquivo de configurações está presente, caso contrário, cria um novo com parâmetros pré-definidos
if not os.path.exists(os.path.join(root, "config.json")):
    basic_config = {
    "temperature": 0.5,
    "candidate_count": 1,
    "model_config": "gemini-2.5-flash",
    }
    with open("config.json", "w") as config_file:
        config_file.seek(0)
        json.dump(basic_config, config_file, indent=4)
        config_file.truncate()

#Obtendo configurações previamente utilizadas pelo usuário
with open("config.json", "r+") as js:
    dic = json.load(js)
    if "transcrypter_files_path" not in dic:
        files = input("Transcrypter - Insira o caminho onde os arquivos serão criados (ex: C:/Users/User/Desktop): ")
        files_path = os.path.join(files, "Transcrypter Files")
        dic["transcrypter_files_path"] = files_path
        js.seek(0)
        json.dump(dic, js, indent=4)
        js.truncate()
        print(f"Transcrypter - Os arquivos serão salvos em: {files_path}.")
    else:
        files_path = dic["transcrypter_files_path"]
        print(f"Transcrypter - Os arquivos serão salvos em: {files_path}.")

#Diretórios utilizados pelo software
if not os.path.exists(files_path):
    os.mkdir(files_path)
audios = os.path.join(files_path, "audios")
transcriptions = os.path.join(files_path, "transcriptions")
resumes = os.path.join(files_path, "resumes")
videos = os.path.join(files_path, "videos")

#Caso os diretórios não existam, eles serão criados automaticamente
if not os.path.exists(audios):
    os.mkdir(audios)
    print("Transcrypter - Pasta audios criada pelo sistema.")
if not os.path.exists(transcriptions):
    os.mkdir(transcriptions)
    print("Transcrypter - Pasta transcriptions criada pelo sistema.")
if not os.path.exists(resumes):
    os.mkdir(resumes)
    print("Transcrypter - Pasta resumes criada pelo sistema.")
if not os.path.exists(videos):
    os.mkdir(videos)
    print("Transcrypter - Pasta videos criada pelo sistema.")

#Verifica se já existe um arquivo .env com chaves de API Gemini, caso contrário, verifica o usuário possui uma chave de API gemini, e pede para inserir-la, após isso, cria o arquivo .env automaticamente
if not os.path.exists(os.path.join(root, "chaves.env")):
    api_key = input("Transcrypter - Insira a sua chave de API Gemini (Para mais informações, consulte: https://aistudio.google.com/apikey): ")
    with open("chaves.env", "w") as chaves:
        chaves.write(f"GEMINI_API_KEY={api_key}")


#Início do programa:
if __name__ == '__main__':
    print("Transcrypter - Insira os áudios na pasta de áudios, ou os vídeos na pasta de vídeos")
    while True: #Menu de seleção do usuário
        select_menu = str(input("Insira a opção desejada:\n 1: Transcrever a partir de um áudio .mp3\n 2: Transcrever a partir de um áudio .wav\n 3: Transcrever a partir de um vídeo .mp4\n 4: Baixar um vídeo diretamente do Youtube\n 5: Sair\n :")).strip()
        if select_menu == "5":
            break
        menu_select(select_menu, root, files_path) #Chama a função menu_select(), que direciona o usuário para o script específico.
