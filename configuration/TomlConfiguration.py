# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:23:08 2020

@author: Himanshu.Manjarawala
"""

from baseclasses import ConfigurationReader, ConfigurationWriter, ConfigurationManager, ConfigurationSettings
from configparser import ConfigParser, ExtendedInterpolation
from config_settings import myConfigurationSettings
import os
import toml

class TomlConfigurationWriter(ConfigurationWriter):
    """This serve as toml file writer class for configuration"""
    
    __config_file_path: str = None
    
    def __init__(self, config_file_path) -> None:
        self.__config_file_path = config_file_path
    
    def write_config_file(self, configSettings: ConfigurationSettings) -> None:
        
        if not os.path.exists(os.path.dirname(self.__config_file_path)):
            os.makedirs(os.path.dirname(self.__config_file_path))
        
        if not os.path.isfile(self.__config_file_path):
            
            data = configSettings.get_settings()
            
            with open(self.__config_file_path, 'w') as f:
                toml.dump(data, f)

class TomlConfigurationReader(ConfigurationReader):
    """This serve as toml file reader class for configuration"""
    
    __config_file_path: str = None
    
    def __init__(self, config_file_path) -> None:
        self.__config_file_path = config_file_path
    
    def read_config_file(self) -> ConfigParser:
        config = ConfigParser(interpolation=ExtendedInterpolation())
        with open(self.__config_file_path, 'r') as f:
            data = toml.load(f)
        config.read_dict(data)
        return config

class TomlConfigurationManager(ConfigurationManager):
    
    __reader: ConfigurationReader = None
    __writer: ConfigurationWriter = None
    
    def __init__(self, config_file_path) -> None:
        self.__reader = TomlConfigurationReader(config_file_path)
        self.__writer = TomlConfigurationWriter(config_file_path)
    
    def write(self, configSettings: ConfigurationSettings) -> None:
        self.__writer.write_config_file(configSettings)
    
    def read(self) -> ConfigParser:
        return self.__reader.read_config_file()

if __name__ == '__main__':
    configFile = os.path.join(os.path.dirname(__file__),'config.toml')
    config = TomlConfigurationManager(configFile)
    settings = myConfigurationSettings()
    config.write(settings)
    cp = config.read()
    
    for sec in cp.sections():
        for key, value in cp.items(sec):
            print(key,value)