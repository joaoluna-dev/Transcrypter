import os
import sys
import json

#Tenta importar os módulos utilizados pelo script atual. Caso algum esteja ausente, o usuário é instado a baixar as biliotecas necessárias
try:
    from google import genai
    from google.genai.types import GenerateContentConfig, HttpOptions
    from google.genai.errors import ClientError, ServerError
    from dotenv import load_dotenv
    from markdown_pdf import MarkdownPdf, Section

except ModuleNotFoundError:
    print("Transcrypter - Módulos necessários para o resume_model.py: google-genai, os, sys, json, dotenv")
    print("Transcrypter - Instalação: pip install google-genai os sys json dotenv")
    sys.exit(1)


def get_config():
    """
    :return: as configurações do modelo definidas pelo usuário no arquivo config.json, como o modelo gemini de escolha e a temperatura, em um dicionário
    """
    print("Transcrypter - Obtendo as configurações definidas pelo usuário para o resumo...")
    with open("config.json", "r") as js:
        dic = json.load(js)
        return dic

#------------------------------------------------#

def gen_ai(temp, candidate_count, text_transcript, model):
    """
    :param temp: a temperatura do modelo, obtida no arquivo config.json
    :param candidate_count: parâmetro candidate count, obtido no arquivo config.json
    :param text_transcript: transcrição do áudio realizada anteriormente pelo audio_transcriptor.py
    :param model: modelo gemini selecionado pelo usuário no arquivo config.json
    :return: um resumo em tópicos no formato markdown
    """
    print("Transcrypter - Resumindo transcrição...")
    #Chamada do modelo gemini, utilizando as configurações definidas pelo usuário, com a instrução adaptada para criar resumos de transcrições de áudio em estrutura markdown
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    system_instruction = "Você é um modelo especializado em analisar transcrições de áudio, criando arquivos em formato Markdown com todos os elementos das trancrições, com tópicos organizando o conteúdo. Tenha certeza de que todos o conteúdo estará contemplado nos resumos, eles devem estar o mais completos possível, para posterior estudo. Não inclua na resposta trechos como: 'Claro! Aqui está o resumo da transcrição da aula em formato Markdown, contemplando todo o conteúdo abordado.' e semelhantes, adicione apenas o conteúdo fornecido das transcrições."
    try:
        response = client.models.generate_content(model=model,
                                                   contents=[system_instruction, text_transcript],
                                                   config=GenerateContentConfig(
                                                       temperature=temp,
                                                       candidate_count=candidate_count))
        return response.text
    except ClientError as e:
        if e.code == 429:
            print("Transcrypter - Erro: Limite de cota da API atingido. O software não poderá resumir a transcrição.")
            sys.exit(1)
        else:
            print(f"Transcrypter - Erro na API Gemini: {e}")
            sys.exit(1)
    except ServerError as e:
        if e.code == 503:
            print("Transcrypter - Erro: O serviço de IA está temporariamente sobrecarregado. Por favor, tente novamente em alguns minutos.")
            sys.exit(1)
        else:
            print(f"Transcrypter - Erro no servidor Gemini: {e}")
            sys.exit(1)
    except Exception as e:
        print(f"Transcrypter - Um erro inesperado ocorreu: {e}")
        sys.exit(1)

#------------------------------------------------#
#Verifica se os argumentos foram passados corretamente (arquivo python, caminho do arquivo de resumo e caminho do arquivo de transcrição)
if len(sys.argv) != 4:
    print("Transcrypter - Uso: python resume_model.py caminho_transcrição nome_arquivo files_path")
    sys.exit(1)

#Diretórios utilizados pelo script
root = os.path.dirname(os.path.abspath(__file__))
files_path = sys.argv[3]
audios = os.path.join(files_path, "audios")
transcriptions = os.path.join(files_path, "transcriptions")
resumes = os.path.join(files_path, "resumes")
videos = os.path.join(files_path, "videos")

#Carregamento do arquivo com a API key gemini
load_dotenv("chaves.env")


txt_path = sys.argv[1] #Caminho do arquivo de transcrição
filename = sys.argv[2] #Nome do arquivo, sem extensão e caminho
pdf_path = os.path.join(resumes, f"{filename}.pdf") #Cria o arquivo .pdf, para escrita do resumo em markdown

#------------------------------------------------#
#Leitura da transcrição do áudio
with open(txt_path, "r", encoding='utf-8') as transcription:
    text = transcription.read()

config = get_config() #Obtenção das configurações do modelo gemini no arquivo config.json, que serão salvas no dicionário config
resume = gen_ai(config["temperature"], config["candidate_count"], text, config["model_config"]) #Chamada da função que realiza o resumo da transcrição, usando as definições do arquivo config.json carregadas

#Escreve o resumo em markdown no arquivo .pdf criado
try:
    pdf = MarkdownPdf(toc_level=2, optimize=True)
    pdf.add_section(Section(resume))
    pdf.save(pdf_path)
    print("Transcrypter - Resumo escrito.")
except Exception as e:
    print(f"Transcrypter - Erro inesperado durante a escrita do resumo: {e}")
