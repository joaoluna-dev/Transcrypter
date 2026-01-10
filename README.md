# 📦 Transcrypter

## 🌟 Destaques

- Transcrição de arquivos de áudio (.mp3, .wav).
- Extração de áudio de arquivos de vídeo (.mp4) e sua transcrição.
- Download de vídeos do YouTube para transcrição.
- Geração de resumos a partir das transcrições usando a API Gemini.
- Interface de linha de comando simples para facilidade de uso.

## ℹ️ Visão Geral

O Transcryptor é uma ferramenta baseada em Python projetada para automatizar o processo de transcrição de arquivos de áudio e vídeo e gerar resumos concisos a partir das transcrições. Ele utiliza a biblioteca Vosk para reconhecimento de fala offline e a IA Gemini do Google para sumarização. O modelo utilizado está disponível em https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip.

### ✍️ Autores

João Gabriel Barbosa de Luna
joaogabrieldeluna@gmail.com

## ⚠️ Requisitos

* Python 3.x
* ffmpeg (https://www.gyan.dev/ffmpeg/builds/)
* Chave de API Gemini (https://aistudio.google.com/apikey)
* Modelo Vosk para reconhecimento de voz offline (https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip)
  
## 🚀 Uso

*Execute a aplicação a partir do diretório raiz do projeto:*

```bash
python main.py
```
* Os diretórios para os arquivos serão criados automaticamente no caminho inserido. Adicione o arquivo desejado no diretório correspondente
* Siga o menu interativo para selecionar o tipo de arquivo que deseja processar. A saída será salva nas pastas `/transcriptions` e `/resumes`.

## ⬇️ Instalação

1. **Instalar o FFMPEG**
   
   * Windows
     ```powershell
     winget install ffmpeg
     ```

   * Linux
       ```bash
       sudo apt update
       sudo apt get ffmpeg
       ```
       
   * MacOS
       * É necessário realizar a instalação do homebrew anteriormente (https://brew.sh/)
         ```zsh
         brew install ffmpeg
         ```
         
3. **Clonar o repositório:**
   
   ```bash
   git clone https://github.com/joaoluna-dev/Transcrypter.git
   cd Transcrypter
   ```

4. **Instalar as dependências:**
   
   ```bash
   pip install -r requirements.txt
   ```

5. **Instalação do modelo Vosk em português**
   
  * Linux e MacOS
   ```bash
   curl https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip -o vosk-model-small-pt-0.3.zip
   unzip vosk-model-small-pt-0.3.zip
   rm vosk-model-small-pt-0.3.zip
   ```

  * Windows
   ```powershell
   curl https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip -o vosk-model-small-pt-0.3.zip
   tar -xf vosk-model-small-pt-0.3.zip
   del vosk-model-small-pt-0.3.zip
   ```
   
7. **Configurar a Chave de API:**
   
   - Ao executar a aplicação pela primeira vez, você será solicitado a inserir sua chave de API do Google AI.
   
   - A chave será salva automaticamente em um arquivo `chaves.env` para uso futuro.

## 💭 Feedback e Contribuição

Sinta-se à vontade para abrir uma issue para relatar bugs ou solicitar recursos.
