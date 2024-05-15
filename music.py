musicas = [
    ("Musica 1", "Rock"),
    ("Musica 2", "Pop"),
    ("Musica 3", "Jazz"),
    ("Musica 4", "Rock"),
    ("music 5", "Pop"),
]

# Historico de musicas ouvidas pelo Usuario
Historico_usuario = ["Rock", "jazz", "Pop", "Jazz", "Pop"]


# Função para recomendar musicas 
def recomendar_musica(historico):
    # Contar a frequencia de cada genero no historico
    frequencia = {}
    for genero in historico:
        if genero in frequencia:
            frequencia [genero] += 1
        else:
            frequencia [genero] = 1

    # Encontrar o genero mais frequente
    genero_mais_frequente = max (frequencia, key=frequencia.get)  

    # Recomendar musicas desse genero
    recomendacoes = []      
    for titulo, genero in musicas:
        if genero == genero_mais_frequente:
            recomendacoes.append(titulo) 
            return recomendacoes
        
        # Obter recomendações para o usuario
        recomendacoes_usuario = recomendar_musica(Historico_usuario)
        print("Musicas recomendadas:", recomendacoes_usuario)
        