from .utils import *
import requests

def profile(name):
    return requests.get(profile + str(name)).json()

def repositories(name):
    return requests.get(profile + str(name)+ "/repos").json()