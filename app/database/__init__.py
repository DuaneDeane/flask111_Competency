#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Simple database operations """

from flask import g
import sqlite3

DATABASE = "HW3_db"


def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def output_formatter(results: tuple):
    out = {"body": []}
    for result in results:
        res_dict = {}
        res_dict["id"] = result[0]
        res_dict["name"] = result[1]
        res_dict["price"] = result[2]
        res_dict["category"] = result[3]
        res_dict["description"] = result[4]
        res_dict["quantity"] = result[5]
        res_dict["unique_tag"] = result[6]
        res_dict["active"] = result[7]
        out["body"].append(res_dict)
    return out


def scan():
    cursor = get_db().execute("SELECT * FROM product", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def read(prod_id):
    query = """
        SELECT *
        FROM product
        WHERE id = ?
        """

    cursor = get_db().execute(query, (prod_id,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def update(prod_id, fields: dict):
    field_string = ", ".join(
        "%s=\"%s\"" % (key, val)
        for key, val
        in fields.items())
    query = """
            UPDATE product
            SET %s
            WHERE id = ?
            """ % field_string
    cursor = get_db()
    cursor.execute(query, (prod_id,))
    cursor.commit()
    return True


def create(name, price, category, description, quantity, unique_tag, active):
    value_tuple = (name, price, category, description,
                   quantity, unique_tag)
    query = """
                INSERT INTO product (
                        name,
                        price,
                        category,
                        description,
                        quantity,
                        unique_tag)
                VALUES (?, ?, ?, ?, ?, ?)
            """
    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    return last_row_id


def deactivate(prod_id):
    query = "UPDATE product SET active = FALSE WHERE id=%s" % prod_id
    cursor = get_db()
    cursor.execute(query, ())
    cursor.commit()
    return True


def delete(prod_id):
    query = "DELETE FROM product WHERE id=%s" % prod_id
    cursor = get_db()
    cursor.execute(query, ())
    cursor.commit()
    return True
