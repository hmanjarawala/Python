# -*- coding: utf-8 -*-
"""
Created on Mon May  4 11:03:12 2020

@author: Himanshu.Manjarawala
"""

from flask_microservices import MicroServicesApp

app = MicroServicesApp(__name__)
#app.config['SERVER_NAME'] = "http://127.0.0.1:5001/"

enabled_modules = [
        'admin'
        ]

# By default, this will assume your modules directory is "./modules"
# if a second argument is not provided.
app.register_urls(enabled_modules)

#app.config['DEBUG'] = True
#app.config['EXPLAIN_TEMPLATE_LOADING'] = True