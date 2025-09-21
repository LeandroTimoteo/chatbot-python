from gtts import gTTS
import os

def speak_text(texto, idioma="pt", nome_arquivo="resposta_audio.wav"):
    try:
        tts = gTTS(text=texto, lang=idioma)
        tts.save(nome_arquivo)
        return nome_arquivo if os.path.exists(nome_arquivo) else None
    except Exception as e:
        print(f"Erro ao gerar áudio: {e}")
        return None





