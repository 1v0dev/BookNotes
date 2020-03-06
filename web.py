import os
import string

import config as cfg

from bottle import route, view, request, response, redirect, default_app, run
from pymongo import MongoClient

client = MongoClient(host=cfg.mongo_host, port=cfg.mongo_port, username=cfg.mongo_username, password=cfg.mongo_password)
notes_db = client.boox_notes
text_prefix = '【content】'
note_prefix = '【note】'
title_prefix = 'BOOX note | <<'

random_sample = [
    {"$sample": {"size": 1}}
]


@route('/', method='GET')
@view('index')
def index():
    random_note_list = list(notes_db.notes.aggregate(random_sample))
    if random_note_list:
        return dict(book_title=random_note_list[0]['book_title'],
                    text=random_note_list[0]['text'],
                    location=random_note_list[0]['location'])
    else:
        return dict(book_title='No books', text='', location='')


@route('/random', method='GET')
def get_random():
    random_note = list(notes_db.notes.aggregate(random_sample))[0]
    return dict(book_title=random_note['book_title'], text=random_note['text'])


@route('/list', method='GET')
@view('list')
def get_list():
    notes = list(notes_db.notes.find({}))
    return dict(notes=notes)


@route('/upload', method='GET')
@view('upload')
def index():
    return dict(message='')


@route('/upload/boox', method='POST')
@view('upload')
def upload_boox():
    bfile = request.files.get('boox_file')

    if bfile.content_type != 'text/plain':
        return dict(message='Only text files allowed')

    added_notes = parse_boox_file(bfile)
    return dict(message='Added notes: ' + str(added_notes))


def parse_boox_file(bfile):
    bfile.save('temp.txt', overwrite=True)
    temp_file = open('temp.txt', encoding='utf-8')
    file_lines = temp_file.readlines()
    book_title = file_lines[0][len(title_prefix):len(file_lines[0]) - 3]
    i = 2
    count = 0
    while i < len(file_lines):
        document = {'book_title': book_title,
                    'location': file_lines[i],
                    'shown': False}
        i += 1
        document['time'] = file_lines[i]
        i += 1

        # text
        document['text'] = file_lines[i][len(text_prefix):]
        i += 1
        while not file_lines[i].startswith('【note】'):
            document['text'] += file_lines[i]
            i += 1
        document['text'] = ''.join(filter(lambda x: x in string.printable, document['text'])).replace('\n', '')

        # note
        document['note'] = file_lines[i][len(note_prefix):]
        i += 1
        while not file_lines[i].startswith('-------------------'):
            document['note'] += file_lines[i]
            i += 1
        i += 1

        notes_db.notes.insert_one(document)
        count += 1

    temp_file.close()
    os.remove(temp_file.name)
    return count


run(host='0.0.0.0', port=8080, debug=True, reloader=True)
