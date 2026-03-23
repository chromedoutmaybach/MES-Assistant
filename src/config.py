import os
import yaml

class Config:
    def __init__(self, config_file='config.yaml'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as file:
            config = yaml.safe_load(file)
        self.validate_config(config)
        return config

    def validate_config(self, config):
        required_keys = ['key1', 'key2']  # Define your required keys here
        for key in required_keys:
            if key not in config:
                raise ValueError(f'Missing required configuration key: {key}') 

    def get(self, key):
        return self.config.get(key)

    def get_env(self, key):
        return os.getenv(key)
