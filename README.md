# 📦 SummaVox

## 🌟 Destaques

- Transcrição de arquivos de áudio (.mp3, .wav).
- Geração de resumos a partir das transcrições usando a API Gemini.
- Extração de áudio de arquivos de vídeo (.mp4) e sua transcrição.
- Download de vídeos do YouTube para transcrição.
- Interface de linha de comando simples para facilidade de uso.

## ℹ️ Visão Geral

O SummaVox é uma ferramenta baseada em Python projetada para automatizar o processo de transcrição de arquivos de áudio e vídeo e gerar resumos concisos a partir das transcrições. Ele utiliza a biblioteca Vosk para reconhecimento de fala offline e a IA Gemini do Google para sumarização. O modelo utilizado está disponível em https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip, sob licença Apache 2.0 e autoria de Alpha Cephei. O objetivo deste projeto é ajudar principalmente estudantes e profissionais, que lidam com a tarefa de realizar anotações diariamente.

### ✍️ Autores

João Gabriel Barbosa de Luna
joaogabrieldeluna@gmail.com

## ⚠️ Requisitos e Informações relevantes

* Python >= 3.10 (https://www.python.org/downloads/)
* ffmpeg (https://www.gyan.dev/ffmpeg/builds/)
* Chave de API Gemini (https://aistudio.google.com/apikey)
* Modelo Vosk para reconhecimento de voz offline (https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip)
* ⚠️ Tenha em mente que você deve obter autorização do criador do áudio/vídeo de interesse para transcrever e sumarizar o seu conteúdo. Não nos responsabilizamos por violações de direitos autorais pelos usuários. ⚠️

## ⬇️ Instalação

Antes de começar, certifique-se de ter os pré-requisitos instalados.

### 1. Pré-requisitos

* **Python 3.10+**: Instale a versão mais recente da sua preferência.
* **FFmpeg**: Ferramenta essencial para processamento de áudio. Instale de acordo com seu sistema:

**Windows:**
```powershell
winget install ffmpeg
```
**Linux(Ubuntu/Debian)**
```bash
sudo apt update && sudo apt install ffmpeg
```
**macOS (Necessário ter o homebrew instalado: https://brew.sh/)**
```zsh
brew install ffmpeg
```

### 2. Escolha o método de instalação

Você pode instalar baixando o pacote pronto (mais fácil) ou clonando o código fonte (para desenvolvimento).

#### 📦 Opção A: Via Release (Recomendado)

Ideal para quem quer apenas usar o software. O modelo Vosk já vem incluído e configurado.

1.  Baixe o arquivo `.zip` da versão mais recente na aba de [Releases](https://github.com/joaoluna-dev/SummaVox/releases).
2.  Extraia o conteúdo para uma pasta de sua preferência.
3.  Abra o terminal na pasta extraída e instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4.  Pronto! O SummaVox está pronto para uso.

#### 💻 Opção B: Via Git (Desenvolvimento)

Ideal para desenvolvedores que querem contribuir ou modificar o código.

1.  Clone o repositório:
    ```bash
    git clone https://github.com/joaoluna-dev/SummaVox.git
    cd SummaVox
    ```

2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Baixe e configure o modelo Vosk:** Como esta versão não inclui o modelo, você precisa baixá-lo manualmente. Execute os comandos abaixo conforme seu sistema para baixar e extrair:

    **Linux e MacOS:**
    ```bash
    curl -L https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip -o vosk-model-small-pt-0.3.zip
    unzip -q vosk-model-small-pt-0.3.zip
    rm vosk-model-small-pt-0.3.zip
    ```

    **Windows (PowerShell):**
    ```powershell
    curl https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip -o vosk-model-small-pt-0.3.zip
    tar -xf vosk-model-small-pt-0.3.zip
    del vosk-model-small-pt-0.3.zip
    ```

## 🚀 Uso

*Execute a aplicação a partir do diretório raiz do projeto, acessando-o pelo terminal:*

```bash
cd caminho_para_a_pasta_do_SummaVox
python main.py
```

* Os diretórios para os arquivos serão criados automaticamente no caminho inserido. Adicione o arquivo desejado no diretório correspondente
* Siga o menu interativo para selecionar o tipo de arquivo que deseja processar. A saída será salva nas pastas `/transcriptions` e `/resumes`.
* Ao executar a aplicação pela primeira vez, você será solicitado a inserir sua chave de API do Google Gemini. A chave será salva automaticamente em um arquivo `chaves.env` para uso futuro. NUNCA COMPARTILHE SUA CHAVE COM OUTRAS PESSOAS.
* Ao executar a aplicação pela primeira vez, você também será solicitado a inserir um local para que a aplicação crie os diretórios de áudios, vídeos, transcrições e resumos. Após isso, o local será salvo no arquivo de configurações (`config.json`). Você pode manualmente alterar no próprio arquivo posteriormente, caso saiba o que está fazendo.

## 📄 Arquivos especiais

* `config.json`: arquivo de configuração do modelo Gemini para sumarização das transcrições e do software, com parâmetros de temperatura (nível de criatividade do modelo), candidate_count e model_config (modelo Gemini utilizado). Após o primeiro uso, o arquivo guarda a localização selecionada pelo usuário para guardar os arquivos de transcrição e resumo do software.
* `requirements.txt`: arquivo com os requisitos para o funcionamento do SummaVox.
* `chaves.env`: arquivo criado após a primeira utilização do software, que contém a chave de acesso para o Gemini. NUNCA COMPARTILHE A SUA CHAVE COM OUTRAS PESSOAS.
  
## 💭 Feedback e Contribuição

Sinta-se à vontade para abrir uma issue para relatar bugs ou solicitar recursos. Todos estão convidados à participar e construir este projeto! ❤️
