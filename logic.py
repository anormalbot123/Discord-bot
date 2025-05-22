import random
import requests

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def get_anime_name():
    url = 'https://kitsu.io/api/edge/anime'
    res = requests.get(url)
    data = res.json()
    anime = random.choice(data["data"])
    return (anime["attributes"]["titles"]["en_jp"])
