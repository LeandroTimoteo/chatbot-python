import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    print("🔊 Nome:", voice.name)
    print("🆔 ID:", voice.id)
    print("🌐 Idioma:", voice.languages)
    print("-" * 40)
