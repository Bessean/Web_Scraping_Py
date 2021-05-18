# A coleta de dados web, ou raspagem web, 
# é uma forma de mineração que permite a extração de dados de sites da web,
# convertendo-os em informação estruturada para posterior análise. 
# O tipo mais básico de coleta é o download manual das páginas, copiando e colando o conteúdo.

import requests

response = requests.get('https://www.python.org/')
print('Status: ', response.status_code)  # cód. 200 significa tudo ok ;)

print('Header') # imprimir o cabeçário em formato dicinário.
print(response.headers)

print('\n Content') # Conteudo da página em HTML
print(response.content)
