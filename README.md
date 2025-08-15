# 📦 Transcryptor

## 🌟 Destaques

- Transcrição de arquivos de áudio (.mp3, .wav).
- Extração de áudio de arquivos de vídeo (.mp4) e sua transcrição.
- Download de vídeos do YouTube para transcrição.
- Geração de resumos a partir das transcrições usando a API Gemini.
- Interface de linha de comando simples para facilidade de uso.

## ℹ️ Visão Geral

O Transcryptor é uma ferramenta baseada em Python projetada para automatizar o processo de transcrição de arquivos de áudio e vídeo e gerar resumos concisos a partir das transcrições. Ele utiliza a biblioteca Vosk para reconhecimento de fala offline e a IA Gemini do Google para sumarização. O modelo utilizado está disponível em https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip .

### ✍️ Autores

João Gabriel Barbosa de Luna
joaogabrieldeluna@gmail.com

## 🚀 Uso

*Execute a aplicação a partir do diretório raiz do projeto:*

```bash
python main.py
```

*Siga o menu interativo para selecionar o tipo de arquivo que deseja processar. A saída será salva nas pastas `/transcriptions` e `/resumes`.*

## ⬇️ Instalação

1. **Clonar o repositório:**
   
   ```bash
   git clone <url_do_repositorio>
   cd Transcryptor
   ```

2. **Instalar as dependências:**
   
   ```bash
   pip install pydub vosk moviepy google-genai python-dotenv pytubefix
   ```

3. **Configurar a Chave de API:**
   
   - Ao executar a aplicação pela primeira vez, você será solicitado a inserir sua chave de API do Google AI.
   
   - A chave será salva automaticamente em um arquivo `chaves.env` para uso futuro.
     *Requer Python 3.x*

## 💭 Feedback e Contribuição

Sinta-se à vontade para abrir uma issue para relatar bugs ou solicitar recursos.
