import os


class Configuration:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
