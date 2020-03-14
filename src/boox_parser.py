import hashlib
import os
import string

text_prefix = '【content】'
note_prefix = '【note】'
title_prefix = 'BOOX note | <<'
time_prefix = 'time：'


def parse_boox_file(bfile, notes_db):
    bfile.save('temp.txt', overwrite=True)
    temp_file = open('temp.txt', encoding='utf-8')
    file_lines = temp_file.readlines()
    book_title = file_lines[0][len(title_prefix):len(file_lines[0]) - 3]
    title_hash = hashlib.md5(book_title.encode('utf-8')).hexdigest()

    category = notes_db.category.find_one({"title_hash": title_hash})
    if category_new := category is None:
        category = {
            'title': book_title,
            'title_hash': title_hash,
            'show_random': True
        }
        category_id = notes_db.category.insert_one(category).inserted_id
    else:
        category_id = category['_id']

    i = 2
    count = 0
    skipped = 0
    while i < len(file_lines):
        document = {'location': file_lines[i],
                    'shown': False,
                    'show_random': True,
                    'origin': 'Boox',
                    'category_id': category_id}
        i += 1
        document['time'] = file_lines[i][len(time_prefix):]
        i += 1

        # text
        document['text'] = file_lines[i][len(text_prefix):]
        i += 1
        while not file_lines[i].startswith('【note】'):
            document['text'] += file_lines[i]
            i += 1
        document['text'] = ''.join(filter(lambda x: x in string.printable, document['text'])).replace('\n', '')
        document['text_hash'] = hashlib.md5(document['text'].encode('utf-8')).hexdigest()

        # note
        document['note'] = file_lines[i][len(note_prefix):]
        i += 1
        while not file_lines[i].startswith('-------------------'):
            document['note'] += file_lines[i]
            i += 1
        i += 1

        if category_new:
            notes_db.notes.insert_one(document)
            count += 1
        else:
            note_existing = notes_db.notes.find_one({"text_hash": document['text_hash']})
            if note_existing is None:
                notes_db.notes.insert_one(document)
                count += 1
            else:
                skipped += 1

    temp_file.close()
    os.remove(temp_file.name)
    message = 'Added notes: ' + str(count)
    if skipped > 0:
        message += ' Existing notes: ' + str(skipped)
    return message
