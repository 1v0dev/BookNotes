import string

import config as cfg

from bottle import route, view, request, response, redirect, default_app, run
from pymongo import MongoClient

client = MongoClient(host=cfg.mongo_host, port=cfg.mongo_port, username=cfg.mongo_username, password=cfg.mongo_password)
notes_db = client.boox_notes
text_prefix = '【content】'
note_prefix = '【note】'

random_sample = [
    {"$sample": {"size": 1}}
]


@route('/', method='GET')
@view('index')
def index():
    random_note = list(notes_db.notes.aggregate(random_sample))[0]
    return dict(book_title=random_note['book_title'], text=random_note['text'])


@route('/random', method='GET')
def get_random():
    random_note = list(notes_db.notes.aggregate(random_sample))[0]
    return dict(book_title=random_note['book_title'], text=random_note['text'])


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
    # file_lines = bfile.file.readlines()
    bfile.save('temp.txt', overwrite=True)
    file_lines = open('temp.txt', encoding='utf-8').readlines()
    book_title = file_lines[0]
    print("Title: %s", book_title)
    i = 2
    count = 0
    while i < len(file_lines):
        document = {'book_title': book_title, 'location': file_lines[i]}
        i += 1
        document['time'] = file_lines[i]
        i += 1

        # text
        document['text'] = file_lines[i][len(text_prefix):]
        i += 1
        while not file_lines[i].startswith('【note】'):
            document['text'] += file_lines[i]
            i += 1
        document['text'] = ''.join(filter(lambda x: x in string.printable, document['text']))

        # note
        document['note'] = file_lines[i][len(note_prefix):]
        i += 1
        while not file_lines[i].startswith('-------------------'):
            document['note'] += file_lines[i]
            i += 1
        i += 1

        print(document)
        notes_db.notes.insert_one(document)
        count += 1

    return count


run(host='localhost', port=8080, debug=True, reloader=True)
