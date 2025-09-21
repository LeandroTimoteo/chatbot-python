![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![OpenRouter](https://img.shields.io/badge/OpenRouter-API-green?logo=openai)
![License](https://img.shields.io/badge/License-MIT-yellow)

# 🤖 ChatBot com Voz e IA 🇧🇷🇺🇸

<p align="center">
  <img src="https://github.com/LeandroTimoteo/chatbot-python/blob/main/images/1.png?raw=true" width="800" alt="Imagem de capa do ChatBot com robô e celular" />
</p>

Este projeto é um ChatBot inteligente com suporte a voz, microfone e integração com modelos de IA via OpenRouter. Ele responde em português ou inglês, com sotaque brasileiro ou americano, e possui interface interativa via Streamlit.

🔗 **Acesse o app online:** [https://bit.ly/4gFaLUA](https://bit.ly/4gFaLUA)

---

## 🚀 Funcionalidades

- 🎤 Entrada por voz e texto
- 🧠 Respostas geradas por IA (OpenRouter)
- 🔊 Resposta falada com pyttsx3
- 🌐 Fallback de voz no navegador
- 🇧🇷🇺🇸 Estilo de voz selecionável (brasileiro ou americano)
- 🎨 Interface com fundo azul escuro e bandeiras

---

## 🛠️ Instalação

```bash
git clone https://github.com/LeandroTimoteo/chatbot-python.git
cd chatbot-python
pip install -r requirements.txt

https://bit.ly/4gFaLUA

chatbot-python/
├── modules/
│   ├── app.py
│   ├── speak.py
│   ├── transcribe.py
│   ├── online.py
├── env/
│   └── .env
├── images/
│   └── 1.png
├── requirements.txt
└── README.md

📸 Interface
Fundo azul escuro (#1565c0)

Bandeiras 🇧🇷 e 🇺🇸 no topo

Seletor de estilo de voz

Histórico de conversa com IA

