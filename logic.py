import random
import requests
import math

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

def do_sine_func(amp=1, per=2 * math.pi, x_shift=0, y_shift=0):
    a = "" if amp == 1 else amp
    b = "" if per == 2 * math.pi else 2 * math.pi / per
    c = "" if x_shift == 0 else f"+ {x_shift * -1}"
    d = "" if y_shift == 0 else f"+ {y_shift}"
    func = f'{a}sine({b}x{c}){d}'
    return func
