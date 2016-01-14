# -*- coding: utf-8 -*-
'''
File Name: jianshu/db.py
Author: JackeyGao
mail: junqi.gao@shuyun.com
Created Time: 三  1/ 6 15:06:18 2016
'''

from peewee import *

db = SqliteDatabase('note.db')

class Note(Model):
    title = CharField()
    slug = CharField()
    url = CharField()
    content = TextField()
    likes_count = IntegerField()
    views_count = IntegerField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Image(Model):
    slug = CharField()
    url = CharField()
    path = CharField()

    class Meta:
        database = db


def delete_note():
    return Note.delete().execute()

def delete_image():
    return Image.delete().execute()

def init_table():
    db.connect()
    db.create_tables([Note, Image])

if __name__ == '__main__':
    db.connect()
    db.create_tables([Note, Image])
