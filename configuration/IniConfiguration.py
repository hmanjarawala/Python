# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:07:22 2020

@author: Himanshu.Manjarawala
"""

from baseclasses import ConfigurationReader, ConfigurationWriter, ConfigurationManager, ConfigurationSettings
from configparser import ConfigParser, ExtendedInterpolation
from config_settings import myConfigurationSettings
import os

class IniConfigurationWriter(ConfigurationWriter):
    """This serve as text file writer class for configuration"""
    
    __config_file_path: str = None
    
    def __init__(self, config_file_path) -> None:
        self.__config_file_path = config_file_path
    
    def write_config_file(self, configSettings: ConfigurationSettings) -> None:
        
        if not os.path.exists(os.path.dirname(self.__config_file_path)):
            os.makedirs(os.path.dirname(self.__config_file_path))
        
        if not os.path.isfile(self.__config_file_path):
        
            config = ConfigParser()
        
            data = configSettings.get_settings()
            
            config.read_dict(data)
        
            with open(self.__config_file_path, 'w') as f:
                config.write(f)


class IniConfigurationReader(ConfigurationReader):
    """This serve as text file reader class for configuration"""
    
    __config_file_path: str = None
    
    def __init__(self, config_file_path) -> None:
        self.__config_file_path = config_file_path
    
    def read_config_file(self) -> ConfigParser:
        config = ConfigParser(interpolation=ExtendedInterpolation())
        config.read(self.__config_file_path)
        return config

class IniConfigurationManager(ConfigurationManager):
    
    __reader: ConfigurationReader = None
    __writer: ConfigurationWriter = None
    
    def __init__(self, config_file_path) -> None:
        self.__reader = IniConfigurationReader(config_file_path)
        self.__writer = IniConfigurationWriter(config_file_path)
    
    def write(self, configSettings: ConfigurationSettings) -> None:
        self.__writer.write_config_file(configSettings)
    
    def read(self) -> ConfigParser:
        return self.__reader.read_config_file()
    
    
if __name__ == '__main__':
    configFile = os.path.join(os.path.dirname(__file__),'config.ini')
    config = IniConfigurationManager(configFile)
    settings = myConfigurationSettings()
    config.write(settings)
    cp = config.read()
    
    for sec in cp.sections():
        for key in cp[sec]:
            print(key,cp.get(sec,key))