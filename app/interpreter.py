def buscar_resposta(pergunta, texto):
    palavras_chave = pergunta.lower().split()
    linhas = texto.split('\n')
    
    for linha in linhas:
        if all(p in linha.lower() for p in palavras_chave):
            return linha
    return None