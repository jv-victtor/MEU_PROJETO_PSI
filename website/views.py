from django.shortcuts import render

elenco = {
    'atletas': [
        {'foto': 'images/ferrerinha.jpg', 'nome': 'Ferreirinha', 'idade': 29, 'posicao': 'Atacante', 'nascimento': 'argentina'},
        {'foto': 'images/leo ortiz.jpg', 'nome': 'léo ortiz', 'idade': 29, 'posicao': 'zagueiro', 'nascimento': 'brasil'},
        {'foto': 'images/leo pereira.jpg', 'nome': 'léo pereira', 'idade': 29, 'posicao': 'zagueiro', 'nascimento': 'brasil'},
        {'foto': 'images/alex sandro.png', 'nome': 'alex sandro', 'idade': 34, 'posicao': 'lateral esquerdo', 'nascimento': 'brasil'},
        {'foto': 'images/wesley.png', 'nome': 'wesley frança', 'idade': 21, 'posicao': 'lateral direito', 'nascimento': 'brasil'},
        {'foto': 'images/erick.png', 'nome': 'erick pulgar', 'idade': 31, 'posicao': 'volante', 'nascimento': 'chile'},
        {'foto': 'images/jorginho.png', 'nome': 'jorginho', 'idade': 33, 'posicao': 'volante', 'nascimento': 'itália'},
        {'foto': 'images/arrascaeta.png', 'nome': 'de arrascaeta', 'idade': 31, 'posicao': 'meia atacante', 'nascimento': 'uruguai'},
        {'foto': 'images/luiz.png', 'nome': 'luiz araújo', 'idade': 29, 'posicao': 'ponta direita', 'nascimento': 'brasil'},
        {'foto': 'images/bh.png', 'nome': 'bruno henrique', 'idade': 34, 'posicao': 'ponta esquerda', 'nascimento': 'brasil'},
        {'foto': 'images/pedro.png', 'nome': 'pedro', 'idade': 28, 'posicao': 'centroavante', 'nascimento': 'brasil'}
    ]
}

info_site = {
    'titulo': 'clubes de regatas do flamengo',
    'historia': 'o flamengo foi fundado em 17 de novembro de 1895 para as disputas de remo. A entrada da equipe de futebol só aconteceu em 1912.',
    'autores': ['João Victor e Elias Renner']
}

def inicio(request):
    return render(request, 'website/inicio.html', {'info': info_site})

def equipe(request):
    return render(request, 'website/equipe.html', elenco)

def sobre(request):
    return render(request, 'website/sobre.html', {'info': info_site})