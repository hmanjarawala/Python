# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:07:51 2020

@author: Himanshu.Manjarawala
"""

import os
import json
from flask import make_response


def root_dir():
    """ Returns root director for this project """
    return os.path.dirname(os.path.realpath(__file__ + '/..'))


def nice_json(arg):
    response = make_response(json.dumps(arg, sort_keys = True, indent=4))
    response.headers['Content-type'] = "application/json"
    return response