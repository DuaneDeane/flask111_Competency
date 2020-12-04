#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Product Form """

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name = StringField("What is the item name?: ", validators=[DataRequired()])
    price = StringField("How much does it cost?: ", validators=[DataRequired()])
    description = StringField("Enter the description of the item: ", validators=[DataRequired()])
    category = StringField("What category is the item: ", validators=[DataRequired()])
    quantity = StringField("How many is required?: ", validators=[DataRequired()])
    unique_tag = StringField("What is the brand?: ", validators=[DataRequired()])
    submit = SubmitField("Submit")