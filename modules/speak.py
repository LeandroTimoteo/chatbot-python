import pyttsx3
import os
from langdetect import detect

# 🔍 Detecta idioma do texto
def detectar_idioma(texto):
    try:
        idioma = detect(texto)
        return idioma
    except Exception:
        return "pt"  # padrão para português se falhar

# 🔊 Gera áudio com voz brasileira ou americana
def speak_text(texto, idioma="pt", nome_arquivo="resposta.wav"):
    try:
        engine = pyttsx3.init()

        # Seleciona voz com base no idioma escolhido
        for voz in engine.getProperty('voices'):
            if idioma == "pt" and ("brazil" in voz.name.lower() or "portuguese" in voz.name.lower()):
                engine.setProperty('voice', voz.id)
                break
            elif idioma == "en" and "english" in voz.name.lower():
                engine.setProperty('voice', voz.id)
                break

        engine.setProperty('rate', 150)   # velocidade da fala
        engine.setProperty('volume', 1.0) # volume máximo

        # Salva o áudio em arquivo
        engine.save_to_file(texto, nome_arquivo)
        engine.runAndWait()

        return nome_arquivo if os.path.exists(nome_arquivo) else None

    except Exception as e:
        print(f"Erro ao gerar áudio: {e}")
        return None






