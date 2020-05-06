# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:32:00 2020

@author: Himanshu.Manjarawala
"""

from setuptools import find_packages, setup

setup(name="cinema",
      version = "0.1",
      description = "Example of Microservices using Flask",
      author = "Umer Mansoor",
      platforms = ["any"],
      license = "BSD",
      packages = find_packages(),
      install_requires = ["Flask==0.10.1", "requests==2.20.0", "wsgiref==0.1.2" ],
      )