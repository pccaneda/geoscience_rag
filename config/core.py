import os 
import yaml


def load_config(path: str):
    with open(path, 'r') as file:
        config = yaml.safe_load(file)
        return config

config = load_config('config/config.yaml')
tools = load_config('config/tools.yaml')