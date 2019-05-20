#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Administrator
@file: models.py
@time: 2019/05/04
@software: PyCharm
@detail: 数据库模型
"""

from datetime import datetime

from sayhello import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
