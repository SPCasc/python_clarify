import json,requests

nome = input('Qual o nome que você deseja consultar?\nR: ')


response = requests.get(f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}")

json_data = json.loads(response.text)

print(json_data[0]['res'][0])
