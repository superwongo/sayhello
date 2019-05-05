#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Administrator
@file: __init__.py
@time: 2019/05/04
@software: PyCharm
@detail: 构造函数
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 为了确保其他扩展或测试框架获得正确的路径值，以硬编码的形式写出包名称作为程序名称
app = Flask(__name__.split('.')[0])
# 配置文件加载
app.config.from_pyfile('settings.py')
# jinja2模板配置，清除模板块两端的空格
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# 初始化flask_sqlalchemy
db = SQLAlchemy(app)

# 在末尾定义其他模块，可以避免在这些模块从构造文件中导入程序实例时循环依赖
from sayhello import views, errors, commands, models
