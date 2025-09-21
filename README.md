![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![OpenRouter](https://img.shields.io/badge/OpenRouter-API-green?logo=openai)
![License](https://img.shields.io/badge/License-MIT-yellow)

# 🤖 ChatBot com Voz e IA — Pity-AI 🇧🇷🇺🇸

<p align="center">
  <a href="https://bit.ly/4gFaLUA" target="_blank">
    <img src="https://github.com/LeandroTimoteo/chatbot-python/blob/main/images/ilustracao-de-icone-de-chatbot-vetorial_1058698-1480.jpg?raw=true" width="800" alt="Imagem de capa do ChatBot com robô e celular" />
  </a>
</p>

Sistema inteligente de conversação com suporte a voz, integração com modelos de IA via OpenRouter e interface interativa via Streamlit. Ideal para aplicações em atendimento, educação, produtividade e acessibilidade.

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

Crie o arquivo .env com sua chave da API:
OPENROUTER_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx

OPENROUTER_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
streamlit run modules/app.py

📦 Estrutura do Projeto
chatbot-python/
├── modules/
│   ├── app.py
│   ├── speak.py
│   ├── transcribe.py
│   ├── online.py
├── env/
│   └── .env
├── images/
│   └── ilustracao-de-icone-de-chatbot-vetorial_1058698-1480.jpg
├── requirements.txt
└── README.md

🧰 Tecnologias Utilizadas
Python 3.10

Streamlit

OpenRouter API

Pyttsx3

SpeechRecognition

dotenv

📘 Sobre o Projeto
O Pity-AI é um chatbot multilíngue com entrada e saída por voz, desenvolvido em Python com Streamlit. Ele utiliza modelos de linguagem via OpenRouter para gerar respostas naturais e contextuais, podendo ser usado em português ou inglês com sotaques ajustáveis.

Este projeto foi criado com foco em acessibilidade, experiência do usuário e integração rápida com APIs modernas.

📄 Licença
Este projeto é open-source sob a licença MIT.

📬 Contato: Analalista de Sistemas  Leandro Timóteo

[![E-mail](https://img.shields.io/badge/-Email-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=FFFFFF)](mailto:leandrinhots6@gmail.com)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=FFFFFF)](https://www.linkedin.com/in/leandro-timóteo-ads/)
[![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=FFFFFF)](https://www.instagram.com/leandrinho_fi/)

🙌 Agradecimentos
Agradeço à comunidade Python e aos desenvolvedores da OpenRouter e Streamlit por fornecerem ferramentas incríveis que tornam projetos como este possíveis.