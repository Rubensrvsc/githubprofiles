from .utils import *
import requests

def profiles(name):
    return requests.get(profile + str(name)).json()

def repositories(name):
    return requests.get(profile + str(name) + '/repos').json()