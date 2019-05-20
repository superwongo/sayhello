#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Administrator
@file: forms.py
@time: 2019/05/04
@software: PyCharm
@detail: 表单
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField('Submit')
