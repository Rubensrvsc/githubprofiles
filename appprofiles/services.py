from .utils import *
import requests
import json

def profiles(name):
    return requests.get(profile + str(name)).json()

def repositories(name):
    repos = requests.get(profile + str(name) + '/repos').json()
    repository = []
    count = 0
    if len(repos)==2 or len(repos) == 0:
        repository.append(0)
    else:
        while count < 4:
            repository.append(repos[count])
            count = count + 1
    
    return repository