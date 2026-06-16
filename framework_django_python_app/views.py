from django.shortcuts import render
import requests

def personagens(request):

    url = "https://last-airbender-api.fly.dev/api/v1/characters"

    response = requests.get(url)

    dados = response.json()

    personagens_traduzidos = []

    # for personagem in dados[:10]:
    for personagem in dados:

        personagens_traduzidos.append({
            'id': personagem.get('_id'),
            'nome': personagem.get('name'),
            'afiliacao': personagem.get('affiliation'),
            'aliados': ', '.join(personagem.get('allies', [])),
            'inimigos': ', '.join(personagem.get('enemies', [])),
            'foto': personagem.get('photoUrl')
        })

    return render(request, 'personagens.html', {
        'personagens': personagens_traduzidos
    })