import os.path
from configparser import ConfigParser


class ConfigManager:
    """docstring for ConfigManager"""
    __file_path = ''

    def __init__(self, filename):
        # print("ConfigManager obj created")
        _dir = os.path.dirname(os.path.abspath(__file__))
        self.__file_path = os.path.join(os.path.dirname(_dir), filename)

    def read_from_config(self, section):
        config = ConfigParser()
        try:
            with open(self.__file_path) as f:
                config.read_file(f)
                return dict(config._sections[section])
        except Exception as e:
            raise e

    def edit_config_file(self, section, dataDict):
        parser = ConfigParser()
        # ReadFile
        try:
            with open(self.__file_path) as f:
                parser.read_file(f)
        except Exception as e:
            raise e
        # Set new Data to obj parser
        for key in dataDict:
            parser.set(section, key, dataDict[key])
        # Write content to file from obj parser
        try:
            with open(self.__file_path, 'w') as f:
                parser.write(f)
            return 1
        except Exception as e:
            raise e
