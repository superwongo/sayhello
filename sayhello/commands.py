#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Administrator
@file: commands.py
@time: 2019/05/04
@software: PyCharm
@detail: 自定义flask命令
"""

import click

from sayhello import app, db, models


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
