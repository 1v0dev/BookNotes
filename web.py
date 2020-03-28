import os

from src import boox_parser, db_util, exporter
from bottle import route, view, request, run, static_file, HTTPResponse, redirect
from bson.objectid import ObjectId


@route('/', method='GET')
@view('index')
def index():
    return db_util.find_random_note()


@route('/random', method='GET')
def get_random():
    note = db_util.find_random_note()['note']
    del note['category']
    del note['category_id']
    note['_id'] = str(note['_id'])
    print(note)
    return note


@route('/list', method='GET')
@view('list')
def get_list():
    categories = list(db_util.notes_db.category.find({}))
    return dict(categories=categories)


@route('/list/<category_id>', method='GET')
@view('list_notes')
def get_list_category(category_id):
    category = db_util.notes_db.category.find_one({"_id": ObjectId(category_id)})
    notes = list(db_util.notes_db.notes.find({"category_id": ObjectId(category_id)}))
    return dict(category=category, notes=notes)


@route('/list/<category_id>/toggle/random', method='POST')
def toggle_category_show_random(category_id):
    show_random = request.forms.show_random.lower() == "true"
    db_util.notes_db.category.find_one_and_update({"_id": ObjectId(category_id)},
                                          {"$set": {"show_random": show_random}})
    return HTTPResponse(status=200)


@route('/new/category', method='POST')
def new_category():
    db_util.new_category(request.forms.categoryTitle)
    redirect("/list")


@route('/export/png', method='GET')
def export_png():
    export_dir = './exported'
    if not os.path.exists(export_dir):
        os.mkdir(export_dir)

    exporter.gen_png_zip(export_dir)

    return static_file('images.zip', root=export_dir)


@route('/upload', method='GET')
@view('upload')
def upload():
    return dict(message='')


@route('/upload/boox', method='POST')
@view('upload')
def upload_boox():
    bfile = request.files.get('boox_file')

    if bfile.content_type != 'text/plain':
        return dict(message='Only text files allowed')

    message = boox_parser.parse_boox_file(bfile, db_util.notes_db)
    return dict(message=message)


@route('/icon/<filename>')
def get_image(filename):
    return static_file(filename, root='./icons')


@route('/favicon.ico', method='GET')
def get_favicon():
    return get_image("favicon.png")


run(host='0.0.0.0', port=8080, debug=True, reloader=True)
