import random
import discord

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_emodji():
    emodji_list = ['😀', '😂', '😅', '😍', '😎', '🤖', '👻', '🎃', '🚀', '🌟']
    return random.choice(emodji_list)

def flip_coin():
    return random.randint(0, 1) == 0 and "Heads" or "Tails"
