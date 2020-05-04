# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:52:52 2020

@author: Himanshu.Manjarawala
"""

from flask import render_template
from SampleApp.AdminAccessWrapper import admin_access_required

@admin_access_required
def admin_panel():
    render_template('main.html')