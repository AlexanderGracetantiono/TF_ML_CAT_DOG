# -*- coding: utf-8 -*-
"""
Created on Thu May 13 15:59:14 2021

@author: alexa
"""

from flask import Flask

app =Flask(__name__)

@app.route('/')
def func_hello_world():
    return "hellow rowld"

app.run()