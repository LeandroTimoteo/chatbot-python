import os
from dotenv import load_dotenv
from openai import OpenAI

# 🔐 Carrega variáveis do arquivo .env localizado na pasta 'env'
load_dotenv(dotenv_path=os.path.join("env", ".env"))

# 🔑 Obtém a chave da API
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("❌ Chave de API não encontrada. Verifique o arquivo env/.env e a variável OPENROUTER_API_KEY.")

# 🔗 Inicializa o cliente da OpenRouter
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# 🧠 Histórico de conversa para manter o contexto
conversa = [
    {"role": "system", "content": "Você é um assistente útil que responde em português do Brasil."}
]

def gerar_resposta_online(prompt: str) -> str:
    """
    Gera uma resposta usando o modelo de IA gratuito do OpenRouter.

    Args:
        prompt (str): A pergunta ou mensagem do usuário.

    Returns:
        str: A resposta gerada pela IA ou uma mensagem de erro.
    """
    try:
        # Adiciona a entrada do usuário ao histórico
        conversa.append({"role": "user", "content": prompt})

        # 🔁 Limita o histórico a 20 mensagens (mantém o system + últimas 19)
        if len(conversa) > 20:
            conversa[:] = [conversa[0]] + conversa[-19:]

        # Chamada à API
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct:free",  # ✅ modelo gratuito
            messages=conversa,
            temperature=0.7,
            max_tokens=500
        )

        # Extrai e retorna a resposta
        resposta = response.choices[0].message.content.strip()
        conversa.append({"role": "assistant", "content": resposta})
        return resposta

    except Exception as e:
        return f"⚠️ Erro ao gerar resposta: {str(e)}"










