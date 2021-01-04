from .utils import *
import requests

def repositorio(nome):
    return requests.get(profile + str(nome)).json()