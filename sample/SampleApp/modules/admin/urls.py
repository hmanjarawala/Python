# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:56:22 2020

@author: Himanshu.Manjarawala
"""

from flask_microservices import url
from . import view

urlpatterns = [
        url('/admin/', view_func=view.admin_panel, name='home'),
        
        
        ]