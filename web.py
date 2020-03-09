import config as cfg
import boox_parser

from bottle import route, view, request, response, redirect, default_app, run
from pymongo import MongoClient
from bson import json_util

client = MongoClient(host=cfg.mongo_host, port=cfg.mongo_port, username=cfg.mongo_username, password=cfg.mongo_password)
notes_db = client.book_notes


random_sample = [
    {"$sample": {"size": 1}}
]


@route('/', method='GET')
@view('index')
def index():
    return find_random_note()


@route('/random', method='GET')
def get_random():
    return json_util.dumps(find_random_note())


def find_random_note():
    random_note_list = list(notes_db.notes.aggregate(random_sample))
    if random_note_list:
        return dict(note=random_note_list[0])
    else:
        return dict(note=dict(category=dict(title='No notes'),
                              text='', location=''))


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

    added_notes = boox_parser.parse_boox_file(bfile, notes_db)
    return dict(message='Added notes: ' + str(added_notes))


run(host='0.0.0.0', port=8080, debug=True, reloader=True)
