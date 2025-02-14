from dotenv import load_dotenv
import os 
import yaml


load_dotenv()

def load_config(path: str):
    with open(path, 'r') as file:
        config = yaml.safe_load(file)
        return config

config = load_config('config/config.yaml')
tools = load_config('config/tools.yaml')

# Injects environment variables
config['api_keys'] = {
    'groq': os.getenv("GROQ_API_KEY"),
    'pinecone': os.getenv("PINECONE_API_KEY"),
    'weather': os.getenv("WEATHER_API_KEY")
}