from bottle import route, view, request, response, redirect, default_app, run
from pymongo import MongoClient


client = MongoClient(host='192.168.0.13', port=9017, username='jroot', password='qwe123')
notes_db = client.boox_notes
text_prefix = '【content】'
note_prefix = '【note】'


@route('/', method='GET')
@view('index')
def index():
    return dict(message='')


@route('/upload/boox', method='POST')
@view('index')
def upload_boox():
    bfile = request.files.get('boox_file')

    if bfile.content_type != 'text/plain':
        return dict(message='Only text files allowed')

    added_notes = parse_boox_file(bfile)
    return dict(message='Added notes' + str(added_notes))


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
        document['text'] = file_lines[i][len(text_prefix):]
        i += 1
        print(document)
        while not file_lines[i].startswith('【note】'):
            document['text'] += file_lines[i]
            i += 1
        document['note'] = file_lines[i][len(note_prefix):]
        i += 1
        print(document)
        while not file_lines[i].startswith('-------------------'):
            document['note'] += file_lines[i]
            i += 1
        i += 1

        notes_db.notes.insert_one(document)
        count += 1

    return count


run(host='localhost', port=8080, debug=True, reloader=True)
