import configparser

config = configparser.RawConfigParser()
config.read('../config/config.ini')

class ReadConfig:
    @staticmethod
    def get_app_url():
        url = config.get('common_info', 'base_url')
        return url