# 🤖 ChatBot com Voz e IA 🇧🇷🇺🇸

Este projeto é um ChatBot inteligente com suporte a voz, microfone e integração com modelos de IA via OpenRouter. Ele responde em português ou inglês, com sotaque brasileiro ou americano, e possui interface interativa via Streamlit.

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
git clone https://github.com/seu-usuario/chatbot-voz-ia.git
cd chatbot-voz-ia
pip install -r requirements.txt

🔐 Configuração
Crie um arquivo .env com sua chave da API:
OPENROUTER_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx

▶️ Como rodar
streamlit run modules/app.py

📦 Estrutura do Projeto
chatbot-voz-ia/
├── modules/
│   ├── app.py
│   ├── speak.py
│   ├── transcribe.py
│   ├── online.py
├── env/
│   └── .env
├── requirements.txt
└── README.md

📸 Interface
Fundo azul escuro (#1565c0)

Bandeiras 🇧🇷 e 🇺🇸 no topo

Seletor de estilo de voz

Histórico de conversa com IA

📄 Licença
Este projeto é open-source sob a licença MIT.

Autor: Analista de Sistemas Leandro Timóteo










