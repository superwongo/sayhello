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

import click

from sayhello import app, db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)


@app.cli.command()
@click.option('--drop', is_flag=True, help='删除表后重建数据库')
def initdb(drop):
    """初始化数据库"""
    if drop:
        click.confirm('此操作会删除数据库，是否确定继续', abort=True)
        db.drop_all()
        click.echo('删除表完成')
    db.create_all()
    click.echo('初始化数据库完成')
