# 🧠 Correção do bug do PyTorch com Streamlit
import torch
torch.classes.__path__ = []

# 📦 Imports principais
import streamlit as st
import io
import wave
import os
from dotenv import load_dotenv

# 🔐 Carrega variáveis do .env
load_dotenv()

# 🎙️ Módulos locais
from audio_recorder_streamlit import audio_recorder
from transcribe import transcribe_audio
from speak import speak_text, detectar_idioma
from online import gerar_resposta_online

# 🔧 Configuração da página
st.set_page_config(page_title="💬 ChatBot - Brazilian Intelligence", layout="centered")
st.title("🤖 ChatBot Pity-AI")

# 🎨 Fundo azul escuro
st.markdown("""
    <style>
        body, .stApp {
            background-color: #1565c0;
            color: white;
        }
        .stRadio > div {
            flex-direction: row;
        }
    </style>
""", unsafe_allow_html=True)

# 🌍 Bandeiras no topo
st.markdown("""
<div style='text-align: center; font-size: 24px; margin-top: -10px;'>
🇧🇷 <strong>ChatBot</strong> 🇺🇸
</div>
""", unsafe_allow_html=True)


# 🎛️ Seletor de estilo de voz
voz_estilo = st.radio(
    "Escolha o estilo de voz:",
    ["🇧🇷 Brasileiro", "🇺🇸 Americano"],
    horizontal=True
)

idioma_selecionado = "pt" if voz_estilo == "🇧🇷 Brasileiro" else "en"
st.caption(f"🗣️ Estilo de voz selecionado: {'Português 🇧🇷' if idioma_selecionado == 'pt' else 'Inglês 🇺🇸'}")

# 💬 Histórico de conversa
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🗣️ Mensagem de boas-vindas falada (uma vez)
if "boas_vindas" not in st.session_state:
    st.session_state.boas_vindas = True
    st.markdown(
        """
        <script>
        var msg = new SpeechSynthesisUtterance("Olá! Eu sou o ChatBot. Pode falar comigo.");
        msg.lang = "pt-BR";
        window.speechSynthesis.speak(msg);
        </script>
        """,
        unsafe_allow_html=True
    )

# 💬 Exibe histórico de mensagens
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 🎙️ Entrada do usuário
st.write("🎤 Speak or type your question below:")
audio_bytes = audio_recorder()
user_prompt = st.chat_input("Type your question...")

# 🎧 Se não digitou, tenta usar o áudio
if not user_prompt and audio_bytes:
    wav_bytes = io.BytesIO(audio_bytes)
    wav_bytes.name = "audio.wav"

    try:
        with wave.open(wav_bytes, "rb") as wf:
            duration = wf.getnframes() / float(wf.getframerate())
        st.audio(wav_bytes.getvalue(), format="audio/wav")
        st.success(f"🎙️ Áudio gravado com sucesso! Duração: {duration:.2f} segundos")
    except Exception:
        st.warning("⚠️ Não foi possível processar o áudio corretamente.")

    try:
        with open("audio.wav", "wb") as f:
            f.write(wav_bytes.getvalue())

        if os.path.exists("audio.wav"):
            user_prompt = transcribe_audio("audio.wav")
            st.info(f"📝 Transcrição: '{user_prompt}'")
    except Exception as e:
        st.error(f"Erro na transcrição: {e}")
        user_prompt = None

# 🤖 Gera resposta com IA se houver pergunta válida
if user_prompt and user_prompt.strip():
    st.session_state.messages.append({"role": "user", "content": user_prompt.strip()})

    with st.chat_message("user"):
        st.markdown(user_prompt.strip())

    try:
        resposta_texto = gerar_resposta_online(user_prompt.strip())
    except Exception as e:
        resposta_texto = f"⚠️ Erro ao gerar resposta: {e}"
        st.error(resposta_texto)

    with st.chat_message("assistant"):
        st.markdown(resposta_texto)

    st.session_state.messages.append({"role": "assistant", "content": resposta_texto})

    # 🔊 Gera áudio com pyttsx3
    if resposta_texto.strip():
        audio_path = speak_text(resposta_texto, idioma_selecionado)

        if audio_path and os.path.exists(audio_path):
            st.audio(audio_path, format="audio/wav", autoplay=True)

            if st.button("🔁 Ouvir novamente"):
                st.audio(audio_path, format="audio/wav", autoplay=True)
        else:
            st.warning("⚠️ O áudio não foi gerado corretamente.")

        # 🗣️ Fala no navegador (fallback)
        lang_code = "en-US" if idioma_selecionado == "en" else "pt-BR"

        st.markdown(
            f"""
            <script>
            var msg = new SpeechSynthesisUtterance({repr(resposta_texto)});
            msg.lang = "{lang_code}";
            msg.rate = 1.0;
            msg.pitch = 1.0;
            msg.volume = 1.0;
            window.speechSynthesis.speak(msg);
            </script>
            """,
            unsafe_allow_html=True
        )
