# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:51:46 2020

@author: Himanshu.Manjarawala
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from configparser import ConfigParser


class ConfigurationSettings(ABC):
    """This interface need to implement in order to write configuration"""
    
    @abstractmethod
    def get_settings(self) -> dict:
        pass

class ConfigurationWriter(ABC):
    """This serve as interface for writer class for configuration"""
    
    @abstractmethod
    def write_config_file(self, configSettings: ConfigurationSettings) -> None:
        """Write an configuration to config file."""
        pass

class ConfigurationReader(ABC):
    """This serve as interface for reader class for configuration"""
    
    @abstractmethod
    def read_config_file(self) -> ConfigParser:
        """Read an configuration from config file."""
        pass


class ConfigurationManager(ABC):
    """This serve as interface for configuration manager"""
    
    @abstractmethod
    def write(self, configSettings: ConfigurationSettings) -> None:
        pass
    
    @abstractmethod
    def read(self) -> ConfigParser:
        pass