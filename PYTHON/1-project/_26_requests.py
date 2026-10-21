import requests

base_url ='https://pokeapi.co/api/v2/'

def get_pokemon_info(name):
    url =f"{base_url}pokemon/{name}"
    response=requests.get(url)
    # print(response.status_code)

    if response.status_code ==200:
        pokemon_data = response.json()
        # print(pokemon_data)
        return pokemon_data
    else :print(f"Failed to retrieve data {response.status_code}")

pokemon_name ='pikachu'
pokemon_info=get_pokemon_info(pokemon_name)
print(f"Name:{pokemon_info['name'].capitalize()}")
print(f"Id:{pokemon_info['id']}")
print(f"Abilities:{pokemon_info['abilities']}")