import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'user_token'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token' : TOKEN}

Create_pokemon = {"name": "generate",
                  "photo": "generate"}
response_create = requests.post(url =f'{URL}/pokemons', headers = HEADER, json = Create_pokemon)
print(response_create.text)

POKEMON_ID = response_create.json()['id']
Rename_pokemon = {"pokemon_id": POKEMON_ID,
    "name": "Petr VI",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"}
response_rename = requests.put(url=f'{URL}/pokemons', headers= HEADER, json = Rename_pokemon)
print(response_rename.text)

Catch_pokemon = {"pokemon_id": POKEMON_ID}
response_catch = requests.post(url=f'{URL}/trainers/add_pokeball', headers= HEADER, json = Catch_pokemon)
print(response_catch.text)