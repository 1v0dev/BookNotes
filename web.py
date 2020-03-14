from src import boox_parser
from bottle import route, view, request, run, static_file, HTTPResponse
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
    del note['category_id']
    note['_id'] = str(note['_id'])
    print(note)
    return note


@route('/list', method='GET')
@view('list')
def get_list():
    categories = list(notes_db.category.find({}))
    return dict(categories=categories)


@route('/list/<category_id>', method='GET')
@view('list_notes')
def get_list_category(category_id):
    category = notes_db.category.find_one({"_id": ObjectId(category_id)})
    notes = list(notes_db.notes.find({"category_id": ObjectId(category_id)}))
    return dict(category=category, notes=notes)


@route('/list/<category_id>/toggle/random', method='POST')
def toggle_category_show_random(category_id):
    show_random = request.forms.show_random.lower() == "true"
    notes_db.category.find_one_and_update({"_id": ObjectId(category_id)},
                                          {"$set": {"show_random": show_random}})
    return HTTPResponse(status=200)


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

    message = boox_parser.parse_boox_file(bfile, notes_db)
    return dict(message=message)


@route('/icon/<filename>')
def get_image(filename):
    return static_file(filename, root='./icons')


@route('/favicon.ico', method='GET')
def get_favicon():
    return get_image("favicon.png")


run(host='0.0.0.0', port=8080, debug=True, reloader=True)
