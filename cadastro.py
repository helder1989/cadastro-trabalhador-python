
from datetime import datetime # buscando o ano atual, pois assim podemos rodar o programa hoje ou daqui a 10 anos

dados = dict()

dados['nome'] = str(input('Nome: '))

nascimento = int(input('Ano de Nascimento: '))

dados ['idade'] = datetime.now().year - nascimento

dados['ctps'] = int(input('Carteira de Trabalho(0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')



