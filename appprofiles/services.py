from .utils import *
import requests
import json

def profiles(name):
    return requests.get(profile + str(name)).json()

def repositories(name):
    repos = requests.get(profile + str(name) + '/repos').json()
    repository = []
    count = 0
    if repos['message'] == 'Not Found':
        repository = []
    else:
        while count < 4:
            repository.append(repos[count])
            count = count + 1
    
    return repository