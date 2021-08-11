from pathlib import Path
PATH = Path(__file__).parents[1]

def config():
    '''Load config file `config.yml` and return dict'''
    
    from yaml import safe_load
    
    config = safe_load(open(PATH.joinpath('config.yml')))
    
    return config

def keys():
    '''Load keys file `api_keys.yml` and return dict'''
    
    from yaml import safe_load
    
    keys = safe_load(open(PATH.joinpath('api_keys.yml')))
    
    return keys