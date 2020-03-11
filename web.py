from src import boox_parser
from bottle import route, view, request, run
from bson.objectid import ObjectId

from src.db_util import find_random_note, notes_db


@route('/', method='GET')
@view('index')
def index():
    return find_random_note()


@route('/random', method='GET')
def get_random():
    note = find_random_note()['note']
    del note['category']
    note['_id'] = str(note['_id'])
    return note


@route('/list', method='GET')
@view('list')
def get_list():
    categories = list(notes_db.category.find({}))
    return dict(categories=categories)


@route('/list/<category_id>', method='GET')
@view('list_notes')
def get_list_category(category_id):
    notes = list(notes_db.notes.find({"category._id": ObjectId(category_id)}))
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
