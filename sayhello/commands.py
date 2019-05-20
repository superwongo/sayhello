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

from sayhello import app, db
from sayhello.models import Message


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


@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    """生成虚拟数据"""
    from faker import Faker

    db.drop_all()
    db.create_all()

    # 默认虚拟数据语言为英文，可以传入第一个参数locale进行定制，简体中文为zh_CN，繁体中文为zh_TW
    fake = Faker()
    click.echo('Working...')

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()
    click.echo(f'Created {count} fake message.')
