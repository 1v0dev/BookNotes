import os
import platform
import imgkit
from zipfile import ZipFile

from bottle import view
from bson import ObjectId
from src import db_util

wkhtmltoimage_path_win = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe'


def export_png(html, filename):
    options = {
        'format': 'png',
        'height': '1872',
        'width': '1404',
        'quality': '80',
    }
    if platform.system() == 'Windows':
        config = imgkit.config(wkhtmltoimage=wkhtmltoimage_path_win)
        imgkit.from_string(html, filename, options=options, config=config)
    else:
        imgkit.from_string(html, filename, options=options)


def gen_png_zip(export_dir):
    zip_file = ZipFile('{}/images.zip'.format(export_dir), 'w')
    categories = list(db_util.notes_db.category.find({"show_random": True}))
    for cat in categories:
        cat_id = cat['_id']
        notes = list(db_util.notes_db.notes.find({"category_id": ObjectId(cat_id)}))
        for note in notes:
            note_id = note["_id"]
            file_name = '{}/{}-{}.png'.format(export_dir, cat_id, note_id)
            export_png(single(note_id), file_name)
            zip_file.write(file_name)
            os.remove(file_name)

    zip_file.close()


@view('single_png')
def single(note_id):
    note = db_util.notes_db.notes.find_one({"_id": ObjectId(note_id)})
    note['category'] = db_util.notes_db.category.find_one({"_id": ObjectId(note['category_id'])})
    return dict(note=note)