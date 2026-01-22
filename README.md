# 📦 SummaVox

## 🌟 Destaques

- Transcrição de arquivos de áudio (.mp3, .wav).
- Geração de resumos a partir das transcrições usando a API Gemini.
- Extração de áudio de arquivos de vídeo (.mp4) e sua transcrição.
- Download de vídeos do YouTube para transcrição.
- Interface de linha de comando simples para facilidade de uso.

## ℹ️ Visão Geral

O SummaVox é uma ferramenta baseada em Python projetada para automatizar o processo de transcrição de arquivos de áudio e vídeo e gerar resumos concisos a partir das transcrições. Ele utiliza a biblioteca Vosk para reconhecimento de fala offline e a IA Gemini do Google para sumarização. O modelo utilizado está disponível em https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip. O objetivo deste projeto é ajudar principalmente estudantes e profissionais, que lidam com a tarefa de realizar anotações diariamente.

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

1. Instale o Python, da forma que for da sua preferência. A versão precisa ser a mesma ou a mais recente que a 3.10.
2. **Instalar o FFMPEG**
   
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
   git clone https://github.com/joaoluna-dev/SummaVox.git
   cd SummaVox
   ```
   - Ou, você pode fazer o download do repositório no formato `zip`, na última versão disponível, na página de [Releases](https://github.com/joaoluna-dev/SummaVox/releases)
        - Caso você faça o download desta maneira, extraia o conteúdo da pasta, e acesse ela pelo terminal
          ```bash
          cd caminho_para_a_pasta_do_SummaVox
          ```

4. **Instalar as dependências:**

   - Acesse a pasta do SummaVox pelo terminal e execute:
   ```bash
   pip install -r requirements.txt
   ```

5. **Instalação do modelo Vosk em português**

   - Acesse a pasta do SummaVox pelo terminal e execute:
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

## 🚀 Uso

*Execute a aplicação a partir do diretório raiz do projeto, acessando-o pelo terminal:*

```bash
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
