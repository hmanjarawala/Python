# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:08:19 2020

@author: Himanshu.Manjarawala
"""

from flask import redirect as _redirect, url_for, render_template, g
from functools import wraps

def admin_access_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        
#        if not g.logged_in:
#            return _redirect(url_for('home'))
#        
#        if not g.user.get_role() or g.user.get_role().can_access_admin:
#            return render_template('403.html')
        return f(*args, **kwargs)
    return decorated_function