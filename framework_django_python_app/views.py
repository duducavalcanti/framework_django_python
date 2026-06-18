from django.shortcuts import render
from django.core.paginator import Paginator
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

    # Cria páginas com 10 personagens cada
    paginator = Paginator(personagens_traduzidos, 10)

    # Obtém o número da página pela URL (?page=1)
    page_number = request.GET.get('page')

    # Retorna a página solicitada
    page_obj = paginator.get_page(page_number)

    return render(request, 'personagens.html', {
        'page_obj': page_obj
    })