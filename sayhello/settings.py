#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Administrator
@file: settings.py
@time: 2019/05/04
@software: PyCharm
@detail: 配置文件
"""

import os

from sayhello import app

dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'db.sqlite3')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
