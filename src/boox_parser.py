import os
import string

from bson import DBRef

text_prefix = '【content】'
note_prefix = '【note】'
title_prefix = 'BOOX note | <<'


def parse_boox_file(bfile, notes_db):
    bfile.save('temp.txt', overwrite=True)
    temp_file = open('temp.txt', encoding='utf-8')
    file_lines = temp_file.readlines()
    book_title = file_lines[0][len(title_prefix):len(file_lines[0]) - 3]

    category = {
        'title': book_title,
        'title_hash': hash(book_title),
        'show_random': True
    }
    category_db = notes_db.category.insert_one(category)

    i = 2
    count = 0
    while i < len(file_lines):
        document = {'location': file_lines[i],
                    'shown': False,
                    'show_random': True,
                    'origin': 'Boox',
                    'category_id': category_db.inserted_id}
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
