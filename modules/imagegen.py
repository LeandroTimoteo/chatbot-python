import webbrowser

def gerar_imagem(prompt):
    # 🔗 Gera a URL com o prompt formatado
    url = f"https://www.craiyon.com/?prompt={prompt.replace(' ', '+')}"
    
    # 🌐 Abre o navegador com o site Craiyon e o tema solicitado
    webbrowser.open(url)
    
    return "🖼️ Imagem sendo gerada no navegador via Craiyon..."
