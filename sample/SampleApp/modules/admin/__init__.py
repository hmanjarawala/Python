# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:06:22 2020

@author: Himanshu.Manjarawala
"""

from flask_microservices import Router
from . import urls

MODULE_NAME = 'admin'
IMPORT_NAME = __name__

blueprint = Router.create_blueprint(MODULE_NAME,IMPORT_NAME)
blueprint.register_urls(urls.urlpatterns)